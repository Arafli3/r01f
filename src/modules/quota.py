import json
pathr01fquota = "/etc/qos/limit/quota.json"
def bacauser(file_path):
    users = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("###"):
                user = line.split()[1]
                users.append(user)
    return users
def bacajson():
    with open(pathr01fquota, 'r') as file:
        return json.load(file)
def konversibyts(bytes_value):
    if bytes_value >= 1_073_741_824:
        return f"{bytes_value / 1_073_741_824:.2f} GB"
    elif bytes_value >= 1_048_576:
        return f"{bytes_value / 1_048_576:.2f} MB"
    elif bytes_value >= 1024:
        return f"{bytes_value / 1024:.2f} KB"
    else:
        return f"{bytes_value} Bytes"
import subprocess

def statusxray(user):
    try:
        result = subprocess.run(
            ["xray", "api", "statsquery", "--server=127.0.0.1:10085", "--pattern=user>>>"+user+">>>traffic>>>uplink"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        #print(f"Output Xray: {result.stdout.strip()}")
        if result.returncode == 0:
            output = result.stdout.strip()
            try:
                data = json.loads(output)
                if "stat" in data:
                    for item in data["stat"]:
                        if "uplink" in item["name"] and user in item["name"]:
                            return "\033[92monline\033[0m"
                return "\033[91moffline\033[0m"
            except json.JSONDecodeError:
                print("Error decoding JSON")
                return "\033[91moffline\033[0m"
        else:
            print(f"Error: {result.stderr}")
            return "\033[91moffline\033[0m"
    
    except Exception as e:
        print(f"Exception occurred: {e}")
        return "\033[91moffline\033[0m"
def fungsiquota(path):
    users_file = bacauser(path)
    data_json = bacajson()
    hasil = []

    for user in users_file:
        found = False
        for key in data_json:
            for item in data_json[key]:
                if isinstance(item, dict) and item.get("user") == user:
                    found = True
                    file_path = f"/etc/qos/xray/usage/{user}"
                    try:
                        with open(file_path, 'r') as file:
                            file_content = file.read().strip()
                            if file_content.lower() == "unlimited":
                                limit = "unlimited"
                            else:
                                limit = konversibyts(int(file_content))
                    except FileNotFoundError:
                        limit = None
                    status = statusxray(user)
                    hasil.append({
                        "user": user,
                        "uplink": konversibyts(item["uplink"]),
                        "downlink": konversibyts(item["downlink"]),
                        "total": konversibyts(item["total"]),
                        "limit": limit,
                        "status": status,
                    })
                    break
            if found:
                break

        if not found:
            hasil.append({
                "user": user,
                "uplink": None,
                "downlink": None,
                "total": None,
                "status": "offline",
            })

    return hasil