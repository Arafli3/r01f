from datetime import datetime, timedelta
import json
import os
def checkfile(pathfile):
    if os.path.exists(pathfile):
        with open(pathfile, 'w') as f:
            f.write("")
            return f"\033[91mNot Found\033[0m"
    else:
        return "\033[92mFound\033[0m"

def checkjson(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except json.JSONDecodeError:
            print(" \033[91m The banned.json file was found, but the JSON format is invalid. Creating a new file.\033[0m")
    else:
        print(" \033[91mFile banned tidak ada, dah lagi maless ngoding gak ada semangat\033[0m")
    
    with open(file_path, 'w') as file:
        default_data = []
        json.dump(default_data, file, indent=4)
    return default_data

def fungunlock(emails):
    databackup = "/etc/qos/xray/banned.json"
    pathfiles1 = "/etc/xray/config.json"
    pathfiles = "/etc/qos/xray/waktubanned"
    sekarang = datetime.now()
    with open(databackup, 'r') as file:
        banned_data = json.load(file)
    with open(pathfiles1, 'r') as file:
        config_data = json.load(file)
    clients_to_restore = [entry for entry in banned_data if entry['client']['email'] in emails]
    
    if not clients_to_restore:
            #print(f"Tidak ada email {emails} di {databackup}.")
        return
    for entry in clients_to_restore:
        inbound_tag = entry['inbound_tag']
        client = entry['client']
        for inbound in config_data['inbounds']:
            if inbound['tag'] == inbound_tag:
                if 'settings' in inbound and 'clients' in inbound['settings']:
                    inbound['settings']['clients'].append(client)
                else:
                    inbound['settings'] = {'clients': [client]}
                break
    with open(pathfiles1, 'w') as file:
        json.dump(config_data, file, indent=4)
    updated_banned_data = [entry for entry in banned_data if entry['client']['email'] not in emails]
    with open(databackup, 'w') as file:
        json.dump(updated_banned_data, file, indent=4)
        #print(f"Klien dengan email {emails} telah dihapus dari {databackup}.")
    with open(pathfiles, 'r') as file:
        lines = file.readlines()
    new_lines = [
        line for line in lines
        if not any(line.strip().startswith(name_user) for name_user in emails)
    ]
    with open(pathfiles, 'w') as file:
        file.writelines(new_lines)
    os.system("systemctl restart xray")
user = ['fufufafa', 'erpinsan', 'ForyoU1']
fungunlock(user)