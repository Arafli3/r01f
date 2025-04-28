import json
import os
import time
from datetime import datetime
configurasi_gme = "/etc/xray/config.json"
logxpxray = "/var/log/gmexray.log"
allxray = "/etc/qos/xray/xrayall.txt"
xray = ["/etc/qos/xray/vmess.txt", "/etc/qos/xray/trojan.txt", "/etc/qos/xray/vless.txt"]

if not os.path.exists(logxpxray):
    with open(logxpxray, "w") as log:
        log.write("\033[92m=== \033[0m\033[93mLOG STARTED\033[0m\033[92m ===\033[0m\n" + "\033[92m-\033[0m" * 50 + "\n")

def gme_log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    xraylogg = f"{timestamp} {message}\n" + "\033[92m-\033[0m" * 50 + "\n"
    with open(logxpxray, "a") as log:
        log.write(xraylogg)
    print(xraylogg, end="")

def toexp():
    xrayxp = set()
    siki = datetime.now().strftime("%Y-%m-%d:%H")
    if os.path.exists(allxray):
        with open(allxray, "r") as f:
            a = f.readlines()
        d = []
        for b in a:
            if b.startswith("### "):
                c = b.split()
                if len(c) >= 3:
                    e = c[1]
                    g = c[2]
                    try:
                        a1 = datetime.strptime(g, "%Y-%m-%d:%H")
                        b1 = datetime.strptime(siki, "%Y-%m-%d:%H")
                        if a1 <= b1:
                            xrayxp.add(e)
                        else:
                            d.append(b)
                    except ValueError:
                        gme_log(f"\033[91mWARNING: The time format in this line is incorrect: {b.strip()}\033[0m")
                        d.append(b)
        with open(allxray, "w") as f:
            f.writelines(d)
    return xrayxp

def rmxraygme(xrayxp):
    for a in xray:
        try:
            if os.path.exists(a):
                with open(a, "r") as f:
                    b = f.readlines()
                d = [c for c in b if not any(f"### {user} " in c for user in xrayxp)]
                if len(d) != len(b):
                    with open(a, "w") as f:
                        f.writelines(d)
                    gme_log(f"\033[92mSUCCESS:\033[0m Successfully deleted expired User {a}")
                else:
                    gme_log(f"\033[93mINFO:\033[0m There is no user exp in {a}")

        except Exception as e:
            gme_log(f"\033[91mERROR:\033[0m Failed to Delete user in {a} - {e}")

def xrayjson(xrayxp):
    try:
        with open(configurasi_gme, "r") as f:
            a = json.load(f)

        b = a.get("inbounds", [])
        i = False
        for e in b:
            if "settings" in e and "clients" in e["settings"]:
                g = e["settings"]["clients"]
                d = [c for c in g if c["email"] not in xrayxp]
                if len(d) != len(g):
                    e["settings"]["clients"] = d
                    i = True
        if i:
            with open(configurasi_gme, "w") as f:
                json.dump(a, f, indent=2)
            gme_log(f"\033[92mSUCCESS: \033[0m Successfully deleted User from config.json")
        else:
            gme_log("\033[93mINFO: \033[0m There are no users in config.json")

    except json.JSONDecodeError as e:
        gme_log(f"\033[91mERROR:\033[0m Failed to read JSON - {e}")
    except Exception as e:
        gme_log(f"\033[91mERROR: \033[0mUpdate Failed config.json - {e}")
        
def load_config(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_user_credentials(config):
    user_data = {}

    for inbound in config.get("inbounds", []):
        protocol = inbound.get("protocol")
        clients = inbound.get("settings", {}).get("clients", [])

        for client in clients:
            email = client.get("email")
            if email:
                if protocol in ["vmess", "vless"]:
                    user_data[email] = client.get("id")
                elif protocol == "trojan":
                    user_data[email] = client.get("password")

    return user_data

def remove_lines_from_file(file_path, target_value):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            lines = f.readlines()

        with open(file_path, "w") as f:
            for line in lines:
                if target_value not in line.strip():
                    f.write(line)
                else:
                    print(f"Removed {target_value} from {file_path}")

def clean_user_logs(user_list):
    config_file = "/etc/xray/config.json"
    uuid_file = "/etc/qos/xray/uuid.txt"

    config_data = load_config(config_file)
    user_data = get_user_credentials(config_data)

    for user in user_list:
        if user in user_data:
            remove_lines_from_file(uuid_file, user_data[user])

def rmalluser(xrayxp):
    for user in xrayxp:
        rmfile = [
            f"/etc/xraylog/log-vless-{user}.txt",
            f"/etc/xraylog/log-vmess-{user}.txt",
            f"/etc/xraylog/log-trojan-{user}.txt",
            f"/var/www/html/vless-{user}",
            f"/var/www/html/vmess-{user}",
            f"/var/www/html/trojan-{user}",
            f"/etc/qos/usage/{user}",
        ]
        for a in rmfile:
            try:
                if os.path.exists(a):
                    os.remove(a)
                    gme_log(f"\033[92mSUCCESS:\033[0m Successfully Deleted Files {a}")
            except Exception as e:
                gme_log(f"\033[91mERROR:\033[0m Failed to Delete file {a} - {e}")

def main():
    while True:
        gme_log("\033[93mINFO: \033[0mStart Processing User Expired.... ")
        xrayxp = toexp()
        men = 1
        nit = men * 60
        if xrayxp:
            gme_log(f"\033[93mINFO:\033[0m Found {len(xrayxp)} user expired: {', '.join(xrayxp)}")
            rmxraygme(xrayxp)
            clean_user_logs(xrayxp)
            xrayjson(xrayxp)
            rmalluser(xrayxp)
            os.system("systemctl restart xray")
        else:
            gme_log("\033[93mINFO:\033[0m No User Expired.")
        gme_log(f"\033[93mINFO:\033[0m Wait {men} minutes for the next process.\n")
        time.sleep(nit)
if __name__ == "__main__":
    main()