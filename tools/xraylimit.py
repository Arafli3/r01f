import re
from datetime import datetime, timedelta
import os
import json
import time
logssh = '/var/log/limitxray.log'
logssws = '/var/log/xraybanned.log'
if not os.path.exists(logssh):
    with open(logssh, "w") as log:
        log.write("\033[92m=== \033[0m\033[93mLOG STARTED\033[0m\033[92m ===\033[0m\n" + "\033[92m-\033[0m" * 50 + "\n")
def gme_log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    sshlog = f"{timestamp} {message}\n" + "\033[92m-\033[0m" * 50 + "\n"
    with open(logssh, "a") as log:
        log.write(sshlog)
    print(logssh, end="")
def gme_log1(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    sshlog = f"{timestamp} {message}\n" + "\033[92m-\033[0m" * 50 + "\n"
    with open(logssws, "a") as log:
        log.write(sshlog)
    print(logssws, end="")
def waktu(teks):
    pola = r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
    return re.match(pola, teks) is not None
def userxray():
    hasill = []
    pathfile = "/etc/qos/xray/limitxray"
    with open(pathfile, 'r') as file:
        baris = file.readlines()
    for line in baris:
        semua = line.strip().split()
        if len(semua) == 2 and semua[1].isdigit():
            hasill.append(line.strip())
    return hasill
"""def gmer01fuser():
    user_file = "/etc/qos/xray/vmess.txt"
    users = []
    if not os.path.exists(user_file):
        print(f"File user {user_file} tidak ditemukan.")
        return users

    with open(user_file, 'r') as file:
        for line in file:
            if line.startswith("###"):
                parts = line.split()
                if len(parts) >= 2:
                    users.append(parts[1])
    return users
"""
def infouser():
    namaa = userxray()
    nama = [f"{user.split()[0]}" for user in namaa]
    paths = "/var/log/xray/access.log"
    hasil = []
    data = {}
    data1 = {}
    with open(paths, 'r') as f:
        for baris in f:
            if any(name in baris for name in nama):
                bagian = baris.split()
                bagianwaktu = " ".join([bagian[0], bagian[1]])
                if waktu(bagianwaktu):
                    mengecek = datetime.strptime(bagianwaktu, "%Y/%m/%d %H:%M:%S")
                    sekarang = datetime.now()
                    satumen = sekarang - timedelta(minutes=1)
                    if mengecek >= satumen and mengecek < sekarang:
                        hasil.append(baris.strip())
                else:
                    gme_log(f"\033[91m format Not valid\033[0m")
    userip = [f"{line.split()[-1]} {line.split()[2]}" for line in hasil]
    for hasile in userip:
        jawa = hasile.split()
        user = jawa[0]
        ip = jawa[-1].replace("tcp", " ").replace(":0", " ").replace("udp:", " ").replace(":", " ").strip()
        if user not in data:
            data[user] = set()
        data[user].add(ip)
    for user, ip in data.items():
        data1[user] = len(ip)
    return data1
def checkjson(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                gme_log(f" \033[91m Banned file not found\033[0m")
                return data
        except json.JSONDecodeError:
            gme_log(" \033[91m The banned.json file was found, but the JSON format is invalid. Creating a new file.\033[0m")
    else:
        gme_log(" \033[91mFile banned tidak ada, dah lagi maless ngoding gak ada semangat\033[0m")
    
    with open(file_path, 'w') as file:
        default_data = []
        json.dump(default_data, file, indent=4)
    return default_data

def banned():
    info = infouser()
    user = userxray()
    hasiluser = []
    for alll in user:
        line = alll.strip().split()
        if len(line) == 2:
            user = line[0]
            limit = int(line[1])
            valuelimit = info.get(user)
            if valuelimit is not None:
                valuelimit = int(valuelimit)
                if limit < valuelimit:
                    gme_log(f" \033[92m Users who will be banned :\033[0m \033[91m{user}\033[0m \033[92mConnected : \033[0m\033[91m{valuelimit}")
                    hasiluser.append(user)
                else:
                    gme_log(f" \033[92m Without violating :\033[0m\033[93m{user}\033[0m")
            else:
                gme_log(f" \033[92m Without violating :\033[0m\033[93m{user}\033[0m")
    if hasiluser:
        databackup = "/etc/qos/xray/banned.json"
        pathfiles1 = "/etc/xray/config.json"
        removeclint = checkjson(databackup)
        with open(pathfiles1, 'r') as file:
            data = json.load(file)
        for inbound in data['inbounds']:
            if 'settings' in inbound and 'clients' in inbound['settings']:
                clients = inbound['settings']['clients']
                for client in clients:
                    if client['email'] in hasiluser:
                        removeclint.append({
                            'inbound_tag': inbound['tag'],
                            'client': client
                        })
                inbound['settings']['clients'] = [client for client in clients if client['email'] not in hasiluser]

        with open(pathfiles1, 'w') as file:
            json.dump(data, file, indent=4)
        with open(databackup, 'w') as file:
            json.dump(removeclint, file, indent=4)
        gme_log(f" \033[92memail \033[0m\033[92m{hasiluser}\033[0m\033[92m Successful banned\033[0m")
        pathfile = "/etc/qos/xray/waktulimit"
        with open(pathfile, 'r') as file:
            line = file.readlines()
        hasil2 = []
        digri = []
        for lines in line:
            All = lines.strip().split()
            if len(All) == 2:
                digit = All[0]
                dig = All[1]
                hasil2.append(digit)
                digri.append(dig)
        angka = int(hasil2[0])
        digiri = digri[0].lower()
        sekrng = datetime.now()
        try:
            if digiri == "minute":
                waktu1 = sekrng + timedelta(minutes=angka)
            elif digiri == "o'clock":
                waktu1 = sekrng + timedelta(hours=angka)
            elif digiri == "day":
                waktu1 = sekrng + timedelta(day=angka)
        except ValueError:
            gme_log(f"\033[91m Unsupported Format: {lines.strip} Please Contact Defloper\033[0m")
        filepath = "/etc/qos/xray/waktubanned"
        with open(filepath, 'r') as file:
            lines = file.readlines()
        new_lines = [
            line for line in lines
            if not any(line.strip().startswith(name_user) for name_user in hasiluser)
            ]
        with open(filepath, 'w') as file:
            file.writelines(new_lines)
        for usr in hasiluser:
            try:
                with open(filepath, 'r') as a:
                    lines = a.readlines()
            except FileNotFoundError:
                lines = []
            lines.append(str(usr) + ' ' + str(waktu1) + '\n')
            with open(filepath, 'w') as f:
                f.writelines(lines)
            gme_log(f" \033[93mUser Unlock Time \033[0m\033[92m{usr} {waktu1}\033[0m")
        os.system("systemctl restart xray")
    else:
        gme_log(" \033[91m There are no violating users at this time!!\033[0m")

def unbanned():
    databackup = "/etc/qos/xray/banned.json"
    pathfiles1 = "/etc/xray/config.json"
    pathfiles = "/etc/qos/xray/waktubanned"
    sekarang = datetime.now()
    userno = []
    emails = []
    with open(pathfiles, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            data = line.split()
            if len(data) >= 2:
                user = data[0]
                waktuuser = ' '.join(data[1:])
                try:
                    waktu = datetime.strptime(waktuuser, "%Y-%m-%d %H:%M:%S.%f")
                    if waktu >= sekarang:
                        print(f" \033[91m User {user} can't be unbanned yet\033[0m")
                        userno.append(user)
                    else:
                        print(f"\033[92mUnbanned\033[0m\033[92m User :{user} \033[0m ")
                        emails.append(user)
                except ValueError:
                    print(f"\033[91m Error 1001: Unsupported Format: {lines.strip} Please Contact Defloper\033[0m")
    if emails:
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
                    gme_log(f" \033[92mUser \033[0m\033[91m{client['email']}\033[0m \033[92mwhich will be Unblocked.\033[0m")
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
        gme_log(f" \033[92mUnblock User \033[0m\033[92m{emails}\033[0m\033[92m Completed \033[0m")
        os.system("systemctl restart xray")
    else:
        gme_log("\033[93m There are no users to unblock yet\033[0m")
def main():
    wak = 1
    nit = wak * 60
    while True:
        print("Start")
        gme_log(f"\033[92mINFO : \033[0m\033[93m---XRAY limit Logs---\033[0m")
        banned()
        unbanned()
        gme_log(f"\033[92mINFO : \033[0m\033[93m{wak} minutes Time Break To Restart\033[0m")
        time.sleep(nit)
if __name__ == "__main__":
    main()