import os
import time
from .lolcat import lolcat
from .lolfig import lolfig
import subprocess
import importlib
import re
from datetime import datetime, timedelta
import json
tampilan = f"""
    \033[34m╔═\033[0m\033[31m─────────────────────────────────────\033[0m\033[34m═╗\033[0m
    \033[31m┃\033[0m \033[1;31;44;1m         Menu Limit User Xray          \033[0m\033[31m ┃\033[0m
    \033[34m╚═\033[0m\033[31m─────────────────────────────────────\033[0m\033[34m═╝\033[0m"""
def clear():
    os.system("clear")
def checkfile(pathfile):
    if os.path.exists(pathfile):
        with open(pathfile, 'w') as f:
            pass
            return f"\033[91mNot Found\033[0m"
    else:
        return "\033[92mFound\033[0m"
def waktu(teks):
    pola = r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
    return re.match(pola, teks) is not None
def check():
    pathfile = "/etc/qos/xray/waktulimit"
    try:
        with open(pathfile, 'r') as f:
            file = f.read()
            lines = file.split()
            if len(lines) == 2:
                angka = lines[0]
                wak = lines[-1]
                return f"\033[92m{angka}\033[0m \033[93m{wak}\033[0m"
            else:
                return "\033[91mNot Found\033[0m"
    except FileNotFoundError:
        with open(pathfile, 'w') as f:
            pass
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
def addtime():
    chec = check()
    pathfile = "/etc/qos/xray/waktulimit"
    print(f"  \n\033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    print(f"  Time Status : {chec}")
    print(f"  \n\033[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    lolcat("\nPress 'X' to go back to Menu Limit All xray or ( Ctrl + X )to exit.\n")
    print("")
    while True:
        opsi = input(" \033[92mAdd Time Unbanned: \033[0m").strip()
        if opsi.lower() == "x":
            clear()
            xraylimit()
            return
        elif opsi.isdigit():
            opsi = int(opsi)
            print(f" \033[93mAdd time {opsi} Success\033[0m")
            break
        else:
            print(" \033[91mPlease Use valid Numbers\033[0m")
    while True:
        print(f" \033[91m>_1.\033[0m\033[92m Minute\033[0m")
        print(f" \033[91m>_2.\033[0m\033[92m O'clock\033[0m")
        print(f" \033[91m>_3.\033[0m\033[92m Days\033[0m")
        option = input("\033[92m Select the Option Above: \033[0m")
        if option.lower() == "x":
            pass
        elif option == "1":
            option = "Minute"
            print(f" \033[93mAdd time Minute Success\033[0m")
            break
        elif option == "2":
            option = "O'clock"
            print(f" \033[93mAdd time O'clock Success\033[0m")
            break
        elif option == "3":
            option = "Days"
            print(f" \033[93mAdd time days Success\033[0m")
            break
        else:
            print(" \033[91mPlease input opsi\033[0m")
    with open(pathfile, 'w') as file:
        file.write(str(opsi) + ' ' + option)
    while True:
        print("Successful")
        opsil = input("\033[92m Please Enter...\033[0m")
        if opsil == "":
            os.system("clear")
            xraylimit()
            return 
        else:
            print("enter lur")
def aktif():
    pathsfile = "/etc/systemd/system/xraylimit.service"
    jasum = """\
[Unit]
Description=Monitor User auto banned&unbanned Xray/V2ray account by GME
After=network.target

[Service]
ExecStart=/usr/bin/python3 /usr/local/bin/xraylimit.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
    """
    with open(pathsfile, 'w') as f:
        f.write(jasum)
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl enable xraylimit.service")
    os.system("sudo systemctl start xraylimit.service")
def nonaktif():
    os.system("sudo systemctl stop xraylimit.service")
    os.system("sudo systemctl disable xraylimit.service")
    os.system('sudo find / -name "xraylimit.service"')
    os.system("sudo rm /etc/systemd/system/xraylimit.service")
def onoffautoban():
    clear()
    service_name = "xraylimit.service"
    try:
        active_status = subprocess.run(
            ["systemctl", "is-active", service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        status_output = subprocess.run(
            ["systemctl", "status", service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if active_status.returncode == 0:
            while True:
                clear()
                lolfig("    Online")
                print(" \033[92m Online status do you want to change it? y/n\033[0m")
                jawa = input("  \033[93mEnter y/n :\033[0m")
                if jawa.lower() == "y":
                    nonaktif()
                    clear()
                    while True:
                        lolfig(" Done!")
                        print(" \033[92mXray Limit Status Active\033[0m")
                        java = input("\033[93mPlease enter...\033[0m")
                        if java == "":
                            clear()
                            xraylimit()
                            return
                        else:
                            print(" \033[91m Please Enter!!!...\033[0m")
                elif jawa.lower() == "n":
                    clear()
                    xraylimit()
                    return
                else:
                    print(" \033[91m Please enter as instructed\033[0m")
        elif active_status.returncode == 3:
            while True:
                lolfig("    Offline")
                print("\033[92m  Offline status do you want to change it? y/n\033[0m")
                sumatra = input("  \033[93mEnter y/n : \033[0m")
                if sumatra.lower() == "y":
                    aktif()
                    clear()
                    while True:
                        lolfig(" Done!")
                        print(" \033[92mXray Limit Status Offline\033[0m")
                        java = input("\033[93mPlease enter...\033[0m")
                        if java == "":
                            clear()
                            xraylimit()
                            return
                        else:
                            print(" \033[91m Please Enter!!!...\033[0m")
                elif sumatra.lower() == "n":
                    clear()
                    xraylimit()
                    return
                else:
                    print(" \033[91m Please enter as instructed\033[0m")
        else:
            if "could not be found" in status_output.stderr:
                while True:
                    lolfig("    Offline")
                    print("\033[92m  Offline status do you want to change it? y/n\033[0m")
                    sumatra = input("  \033[93mEnter y/n : \033[0m")
                    if sumatra.lower() == "y":
                        aktif()
                        clear()
                        while True:
                            lolfig(" Done!")
                            print(" \033[92mXray Limit Status Offline\033[0m")
                            java = input("\033[93mPlease enter...\033[0m")
                            if java == "":
                                clear()
                                xraylimit()
                                return
                            else:
                                print(" \033[91m Please Enter!!!...\033[0m")
                    elif sumatra.lower() == "n":
                        clear()
                        xraylimit()
                        return
                    else:
                        print(" \033[91m Please enter as instructed\033[0m")
            else:
                while True:
                    lolfig("    Offline")
                    print("\033[92m  Offline status do you want to change it? y/n\033[0m")
                    sumatra = input("  \033[93mEnter y/n : \033[0m")
                    if sumatra.lower() == "y":
                        aktif()
                        clear()
                        while True:
                            lolfig(" Done!")
                            print(" \033[92mXray Limit Status Offline\033[0m")
                            java = input("\033[93mPlease enter...\033[0m")
                            if java == "":
                                clear()
                                xraylimit()
                                return
                            else:
                                print(" \033[91m Please Enter!!!...\033[0m")
                    elif sumatra.lower() == "n":
                        clear()
                        xraylimit()
                        return
                    else:
                        print(" \033[91m Please enter as instructed\033[0m")
    except Exception as e:
        print(f" Error: {e}")
def checkingg():
    service_name = "xraylimit.service"
    try:
        active_status = subprocess.run(
            ["systemctl", "is-active", service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        status_output = subprocess.run(
            ["systemctl", "status", service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if active_status.returncode == 0:
            return " \033[92mONLINE\033[0m"
        elif active_status.returncode == 3:
            return " \033[91mOFFLINE\033[0m"
        else:
            if "could not be found" in status_output.stderr:
                return " \033[91mOFFLINE\033[0m"
            else:
                return " \033[91mOFFLINE\033[0m"
    except Exception as e:
        return f"Eror: {e}"
def tdkmelangar():
    pathfile = "/etc/qos/xray/waktubanned"
    pathfile1 = "/etc/qos/xray/limitxray"
    hasil1 = []
    hasil = []
    with open(pathfile, 'r') as f:
        for lines in f:
            hasil.append(lines.strip())
    with open(pathfile1, 'r') as f:
        for line in f:
            hasil1.append(line.strip())
    hasil2 = int(len(hasil1)) - int(len(hasil))
    return hasil2
def melangar():
    pathfile = "/etc/qos/xray/waktubanned"
    hasil = []
    with open(pathfile, 'r') as f:
        line = f.readlines()
    for lines in line:
        lines.split()
        hasil.append(lines)
    if hasil:
        return len(hasil)
    else:
        return 0
def funglock(hasiluser):
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
    filepath = "/etc/qos/xray/waktubanned"
    sekrng = datetime.now()
    angka = int(9999)
    waktu1 = sekrng + timedelta(days=angka)
    with open(filepath, 'r') as file:
        line = file.readlines()
    new_lines = [
        lines for lines in line
        if not any(lines.strip().startswith(nama_user) for nama_user in hasiluser)
    ]
    with open(filepath, 'w') as files:
        files.writelines(new_lines)
    for usr in hasiluser:
        try:
            with open(filepath, 'r') as a:
                lines = a.readlines()
        except FileNotFoundError:
            lines = []
        lines.append(str(usr) + ' ' + str(waktu1) + '\n')
        with open(filepath, 'w') as f:
            f.writelines(lines)
        os.system("systemctl restart xray")
    return
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
        
def setatuskey(user):
    filepath = "/etc/qos/xray/waktubanned"
    try:
        with open(filepath, 'r') as file:
            banned_users = [line.strip().split()[0] for line in file if line.strip()]
            return "\033[91mlock\033[0m" if user in banned_users else "\033[92munlock\033[0m"
    except FileNotFoundError:
        return "\033[92munlock\033[0m"
    except Exception as e:
        return "\033[92munlock\033[0m"

def infouser(namaa):
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
                    print(f"\033[91m format Not valid\033[0m")
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
    try:
        user = namaa.split()[0]
        valuelimit = data1.get(user)
            
        if valuelimit is not None:
            return int(valuelimit)
        else:
            return 0
                
    except (IndexError, ValueError) as e:
        print(f"Error memproses baris '{alll}': {e}")
def lockunlock():
    clear()
    pathfiles = '/etc/qos/xray/limitxray'
    databackup = "/etc/qos/xray/banned.json"
    pathfiles1 = "/etc/xray/config.json"
    usergme = []
    userlockunlock = []
    with open(pathfiles, 'r') as f:
        f = f.readlines()
    for a in f:
        usergme.append(a)
    if usergme:
        while True:
            clear()
            print("  \033[34m╔═─────────────────────────────────────═╗\033[0m")
            print("  \033[31m┃\033[0m \033[1;31;44;1m           XRAY Limit USER           \033[0m\033[31m ┃\033[0m")
            print("  \033[34m╚═─────────────────────────────────────═╝\033[0m")
            print(f"    \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            print("\033[34m ┌────────────────────────────────────────────┐\033[0m")
            for nom, line in enumerate(usergme, 1):
                nama_user = line.split()[0]
                keystaus = setatuskey(nama_user)
                coneck = infouser(nama_user)
                try:
                    limituser = line.split()[1]
                    
                    print(" \033[94m<\033[0m\033[91m──────────────────────\033[0m\033[94m>\033[0m")
                    print(f"  \033[93m>_ {nom:<5}{nama_user}\033[0m")
                    print("  \033[92m SETATUS :\033[0m")
                    print(f"    \033[92m>_ Setatus : \033[0m\033[93m{keystaus}\033[0m")
                    print(f"    \033[92m>_ Limit : \033[0m\033[93m{limituser}\033[0m")
                    print(f"    \033[92m>_ Connection : {coneck} \033[0m")
                    print(" \033[91m<\033[0m\033[94m──────────────────────\033[0m\033[91m>\033[0m")
                except (IndexError, ValueError):
                    print(f"  \033[91mError 1001: Invalid Format Please Contact Developer/Community\033[0m")
            print(f" \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress 'X' to go back to VPN menu or ( Ctrl + X )to exit.\n")
            listnum = input("\033[93m Select user to unblock/block: \033[0m ").strip()
            if listnum.lower() == "x":
                print(f"\033[93mExiting the Xraylimit process.\033[0m")
                time.sleep(0.5)
                clear()
                xraylimit()
                return
            try:
                listnumb = [int(x.strip()) for x in listnum.split(',')]
                if any(baris <= 0 or baris > len(usergme) for baris in listnumb):
                    print("\033[91mInvalid user number.\033[0m")
                    continue
                listhap = [usergme[baris - 1].strip() for baris in listnumb]
            except (ValueError, UnboundLocalError):
                print(" \033[91mPlease enter the correct input\033[0m")
                continue 
            print(f" \033[94m┌───────────────────────────────────┐\033[0m")
            print(f"           \033[91m User to be Unlock/lock\033[0m")
            print(f" \033[94m└───────────────────────────────────┘\033[0m")
            for list1, baris in zip(listnumb, listhap):
                nama_user = baris.split()[0]
                userlockunlock.append(nama_user)
                print(f"                \033[93m{list1}: {nama_user}\033[0m")
            print(f"   \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            while True:
                opsii = input(" \033[93mInput Unlock or lock :\033[0m ").strip()
                if opsii.lower() == "x":
                    print(" \033[0mcancelled \033[0m")
                    time.sleep(0.5)
                    clear()
                    lockunlock()
                    return
                elif opsii.lower() == "unlock":
                    fungunlock(userlockunlock)
                    while True:
                        print(" \033[94m<\033[0m\033[91m──────────────────────\033[0m\033[94m>\033[0m")
                        for user in userlockunlock:
                            print(f" \033[92mAccount \033[0m\033[93m{user} \033[0m\033[92mSuccessfully Unlocked.\033[0m")
                        print(" \033[91m<\033[0m\033[94m──────────────────────\033[0m\033[91m>\033[0m")
                        ops1 = input(" \033[93mPlease Enter...\033[0m").strip()
                        if ops1 == "":
                            clear()
                            lockunlock()
                            return
                        else:
                            print(" \033[91m what are you doing? please enter\033[0m")
                elif opsii.lower() == "lock":
                    print(userlockunlock)
                    funglock(userlockunlock)
                    while True:
                        print(" \033[94m<\033[0m\033[91m──────────────────────\033[0m\033[94m>\033[0m")
                        for user in userlockunlock:
                            print(f" \033[92mAccount \033[0m\033[93m{user} \033[0m\033[92mSuccessfully locked.\033[0m")
                        print(" \033[91m<\033[0m\033[94m──────────────────────\033[0m\033[91m>\033[0m")
                        ops = input(" \033[93mPlease Enter...\033[0m")
                        if ops == "":
                            clear()
                            lockunlock()
                            return
                        else:
                            print(" \033[91m what are you doing? please enter\033[0m")
                else:
                    print("\033[91m  Please select the options as instructed.\033[0m")
    else:
        while True:
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m \033[94m          LIMIT XRAY USER            \033[0m\033[91m ┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            print("")
            print("             \033[91m Empty Member\033[0m")
            print("")
            print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress Enter to go back to vpn menu or ( Ctrl + X )to exit.\n")
            user_input = input(" \033[93mPress Enter.. \033[0m").strip()
            if user_input.lower() == "":
                print(f"\033[93mExiting the Xray limit process.\033[0m")
                time.sleep(0.5)
                xraylimit()
                return
            else:
                print("\033[91m What are you doing ?\033[0m")
                time.sleep(0.5)
def renewlimit():
    clear()
    pathfiles = '/etc/qos/xray/limitxray'
    usergme = []
    with open(pathfiles, 'r') as f:
        file = f.readlines()
    for a in file:
        usergme.append(a)
    if usergme:
        while True:
            clear()
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m \033[94m          LIMIT User Renewal         \033[0m\033[91m ┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            print("")
            print(f" \033[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            for idx, line in enumerate(usergme, 1):
                try:
                    user = line.split()[0]
                    limit = line.split()[1]
                    print(f"\033[93m >_ {idx}.\033[0m \033[92m{user}\033[0m  \033[93mLimituser: \033[0m\033[92m{limit}\033[0m")
                except (IndexError, ValueError):
                    print(f"  \033[91mError 1001: Invalid Format Please Contact Developer/Community\033[0m")
            print(f"  \n\033[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress 'X' to go back to Xray menu or (Ctrl + X) to exit.\n")
            listnum = input("\033[93mEnter the user number to renew (or 'x' to exit):\033[0m ").strip()
            if listnum.lower() == 'x':
                print(" \033[93mExiting renewal process.\033[0m")
                time.sleep(0.5)
                xraylimit()
                clear()
                break
            elif listnum.isdigit() and 1 <= int(listnum) <= len(usergme):
                selected_user = usergme[int(listnum) - 1].strip()
                nama_user = selected_user.split()[0]
                limit = selected_user.split()[1]
                print("     \033[34m>________________<\033[0m")
                print("     \033[31m-------------------------------\033[0m")
                print(f"  \033[94mSelected User Details:\033[0m")
                print(f"  \033[93mUsername  : {nama_user}\033[0m")
                print(f"  \033[93mExpiration: {limit}\033[0m")
                print("     \033[34m-------------------------------\033[0m")
                print("     \033[31m>________________<\033[0m")
                if limit.lower() == "unlimited":
                    print(f" \033[93m User {nama_user} unlimited Do you want to change it to limit?\033[0m")
                    print(" \033[93m Input( x )to cancel or enter a number to enter the limit amount\033[0m")
                    while True:
                        inpt = input("\033[92m Input Options : \033[0m")
                        if inpt.lower() == "x":
                            print(" \033[93mExiting renewal process.\033[0m")
                            time.sleep(0.5)
                            xraylimit()
                            clear()
                            break
                        elif inpt.isdigit():
                            limits = int(inpt)
                            with open(pathfiles, 'r') as f:
                                lines = f.readlines()
                            with open(pathfiles, 'w') as files:
                                for line in lines:
                                    data = line.strip()
                                    if data.startswith(nama_user):
                                        data1 = data.split()
                                        if len(data1) >= 2:
                                            data1[1] = str(limits)
                                            line = ' '.join(data1) + "\n"
                                    files.write(line)
                            while True:
                                print("     \033[34m>________________<\033[0m")
                                print("     \033[31m-------------------------------\033[0m")
                                print(f"  \033[94mRenewal xray Limit Successful:\033[0m")
                                print(f"  \033[93mUsername  : {nama_user}\033[0m")
                                print(f"  \033[93mExpiration: {limits}\033[0m")
                                print("     \033[34m-------------------------------\033[0m")
                                print("     \033[31m>________________<\033[0m")
                                inptr = input("\033[92m Please Enter...\033[0m")
                                if inptr == "":
                                    clear()
                                    renewlimit()
                                    return
                                else:
                                    print(" \033[91mYang bener lah masukin nyaa, gw dah cape bikin ini\033[0m")
                            else:
                                print(" \033[91m Please please enter the input correctly\033[0m")
                else:
                    while True:
                        print(" \033[92m Enter x for cancel, leave blank for unlimited,\n and enter a number for the limit, + option for addition and - option for subtraction\033[0m")
                        sindi = input(" \033[93mInput Options :\033[0m")
                        if sindi.lower() == "x":
                            print(" \033[93mExiting renewal process.\033[0m")
                            time.sleep(0.5)
                            clear()
                            renewlimit()
                            return
                        elif sindi == "":
                            limitess = "unlimited"
                            with open(pathfiles, 'r') as f:
                                lines = f.readlines()
                            with open(pathfiles, 'w') as file:
                                for jawa in lines:
                                    jawa = jawa.strip()
                                    if jawa.startswith(nama_user):
                                        data = jawa.split()
                                        if len(data) >= 2:
                                            data[1] = str(limitess)
                                            jawa = ' '.join(data)
                                    file.write(jawa + "\n")
                            while True:
                                print("     \033[34m>________________<\033[0m")
                                print("     \033[31m-------------------------------\033[0m")
                                print(f"  \033[94mRenewal xray Limit Successful:\033[0m")
                                print(f"  \033[93mUsername  : {nama_user}\033[0m")
                                print(f"  \033[93mExpiration: {limitess}\033[0m")
                                print("     \033[34m-------------------------------\033[0m")
                                print("     \033[31m>________________<\033[0m")
                                inptr = input("\033[92m Please Enter...\033[0m")
                                if inptr == "":
                                    clear()
                                    renewlimit()
                                    return
                                else:
                                    print(" \033[91mYang bener lah masukin nyaa, gw dah cape bikin ini\033[0m")
                                        
                        elif sindi == "+":
                            while True:
                                tidar = input("\033[93m  Add Limit User :\033[0m")
                                if tidar.lower() == "x":
                                    print(" \033[93mExiting renewal process.\033[0m")
                                    time.sleep(0.5)
                                    clear()
                                    renewlimit()
                                    return
                                if tidar.isdigit():
                                    userin = int(tidar)
                                    limited = int(limit) + userin
                                    with open(pathfiles, 'r') as f:
                                        lines = f.readlines()
                                    with open(pathfiles, 'w') as files:
                                        for baris in lines:
                                            if baris.startswith(nama_user):
                                                data = baris.split()
                                                if len(data) >= 2:
                                                    data[1] = str(limited)
                                                    baris = ' '.join(data) + "\n"
                                            files.write(baris)
                                    while True:
                                        print("     \033[34m>________________<\033[0m")
                                        print("     \033[31m-------------------------------\033[0m")
                                        print(f"  \033[94mRenewal xray Limit Successful:\033[0m")
                                        print(f"  \033[93mUsername  : {nama_user}\033[0m")
                                        print(f"  \033[93mExpiration: {limited}\033[0m")
                                        print("     \033[34m-------------------------------\033[0m")
                                        print("     \033[31m>________________<\033[0m")
                                        inptr = input("\033[92m Please Enter...\033[0m")
                                        if inptr == "":
                                            clear()
                                            renewlimit()
                                            return
                                        else:
                                            print(" \033[91mYang bener lah masukin nyaa, gw dah cape bikin ini\033[0m")
                                else:
                                    print(" \033[91m Please please enter the input correctly\033[0m")
                        elif sindi == "-":
                            while True:
                                sinden = input("\033[92m  Xray user limit reduction : \033[0m")
                                if sinden.lower() == "x":
                                    print(" \033[93mExiting renewal process.\033[0m")
                                    time.sleep(0.5)
                                    clear()
                                    renewlimit()
                                if sinden.isdigit():
                                    userin = int(sinden)
                                    limited = int(limit) - userin
                                    with open(pathfiles, 'r') as f:
                                        lines = f.readlines()
                                    with open(pathfiles, 'w') as files:
                                        for baris in lines:
                                            if baris.startswith(nama_user):
                                                data = baris.split()
                                                if len(data) >= 2:
                                                    data[1] = str(limited)
                                                    baris = ' '.join(data) + "\n"
                                            files.write(baris)
                                    while True:
                                        print("     \033[34m>________________<\033[0m")
                                        print("     \033[31m-------------------------------\033[0m")
                                        print(f"  \033[94mRenewal xray Limit Successful:\033[0m")
                                        print(f"  \033[93mUsername  : {nama_user}\033[0m")
                                        print(f"  \033[93mExpiration: {limited}\033[0m")
                                        print("     \033[34m-------------------------------\033[0m")
                                        print("     \033[31m>________________<\033[0m")
                                        inptr = input("\033[92m Please Enter...\033[0m")
                                        if inptr == "":
                                            clear()
                                            renewlimit()
                                            return
                                        else:
                                            print(" \033[91mYang bener lah masukin nyaa, gw dah cape bikin ini\033[0m")
            else:
                print("\033[91m  Please select the options as instructed.\033[0m")
    else:
        while True:
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m\033[94m          RENEWAL XRAY USER           \033[0m \033[91m┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            print("")
            print("             \033[91m Empty Member\033[0m")
            print("")
            print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress Enter to go back to limit Xray menu or ( Ctrl + X )to exit.\n")
            user_input = input(" \033[93mPress Enter.. \033[0m").strip()
            if user_input.lower() == "":
                print(f"\033[93mExiting the VMESS renewal process.\033[0m")
                time.sleep(0.5)
                clear()
                xraylimit()
                return
            else:
                print("\033[91m What are you doing? Please enter\033[0m")
def xraylimit():
    clear()
    bann = check()
    cheks = checkingg()
    jum1 = tdkmelangar()
    jum = melangar()
    back = importlib.import_module("modules.VAK")
    while True:
        print("     ", tampilan)
        print(f"    \033[91m>\033[0m\033[94m_\033[0m \033[93mviolate : \033[0m\033[91m{jum}\033[0m\033[93m user\033[0m \033[91m>\033[0m\033[94m_\033[0m \033[93m No violation :\033[0m\033[92m {jum1}\033[0m \033[93mUser\033[0m")
        print(f"    \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
        print(f"    \033[91m>\033[0m\033[94m_\033[0m \033[93mStatus :\033[0m {bann} \033[91m>\033[0m\033[94m_\033[0m \033[93mSetatus limit : \033[0m{cheks}")
        print(f"    \033[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
        print(f"    \033[31m| |\033[0m [\033[31m01\033[0m] Change Auto Banned Status")
        print(f"    \033[31m| |\033[0m [\033[31m02\033[0m] Change Unbanned Time")
        print(f"    \033[31m| |\033[0m [\033[31m03\033[0m] Unbanned / Banned manually")
        print(f"    \033[31m| |\033[0m [\033[31m04\033[0m] Renewal Limit Xray User")
        print(f"    \033[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
        print(f"    \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
        lolcat("\n  Press 'X' to go back to VPN menu or ( Ctrl + X )to exit.\n")
        opsi = input("  \033[93m Please Select Options: \033[0m").strip()
        if opsi.lower() == "x":
            clear()
            back.vpn_menu()
            return
        elif opsi == "1":
            clear()
            onoffautoban()
            return
        elif opsi == "2":
            clear()
            addtime()
            return
        elif opsi == "3":
            clear()
            lockunlock()
            return
        elif opsi == "4":
            clear()
            renewlimit()
            return
        else:
            print("\033[91m Tau lah salah nya dimana!!\033[0m")