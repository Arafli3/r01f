from .lolcat import lolcat
import os
from collections import defaultdict
import time
import importlib
import subprocess
from .lolfig import lolfig
tampilan = f"""
    \033[34m╔═\033[0m\033[31m─────────────────────────────────────\033[0m\033[34m═╗\033[0m
    \033[31m┃\033[0m \033[1;31;44;1m         Menu Limit User SSH         \033[0m\033[31m ┃\033[0m
    \033[34m╚═\033[0m\033[31m─────────────────────────────────────\033[0m\033[34m═╝\033[0m"""
def clear():
    os.system("clear")
def check():
    pathfile = "/etc/qos/ssh/waktussh"
    try:
        with open(pathfile, 'r') as f:
            isiini = f.read()
            isi = isiini.strip().split()
            if len(isi) == 2:
                ang = isi[0]
                teks = isi[1]
                return f"\033[92m{ang}\033[0m \033[93m{teks}\033[0m"
            else:
                return "\033[91mNot Found\033[0m"
    except FileNotFoundError:
        with open(pathfile, 'w') as f:
            clear()
            sshlimit()
            return
def addtime():
    bann = check()
    pathfiles = "/etc/qos/ssh/waktussh"
    print(f"  \n\033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    print(f"  Time Status : {bann}")
    print(f"  \n\033[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    lolcat("\nPress 'X' to go back to Menu Limit User SSH or ( Ctrl + X )to exit.\n")
    print("")
    while True:
        opsi = input(" \033[92mAdd Time Unbanned: \033[0m").strip()
        if opsi.lower() == "x":
            clear()
            sshlimit()
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
    with open(pathfiles, 'w') as file:
        file.write(str(opsi) + ' ' + option)
    while True:
        print("Successful")
        opsil = input("\033[92m Please Enter...\033[0m")
        if opsil == "":
            os.system("clear")
            sshlimit()
            return 
        else:
            print("enter lur")
            
def status_gmeuser(username):
    try:
        hasildari = subprocess.run(["passwd", "-S", username], capture_output=True, text=True, check=True)
        O = hasildari.stdout.split()[1]
        return "\033[92mUNLOCK\033[0m" if O == "P" else "\033[91mLOCK\033[0m"
    except subprocess.CalledProcessError:
        return "\033[91m Error002: If there is a problem, please contact Defloper or Community\033[0m"
def infoonline():
    users = defaultdict(lambda: {"connected": False, "connections": 0, "last_connections": 0})
    try:
        iniresult = subprocess.run(
            ["grep", "dropbear", "/var/log/auth.log"],
            capture_output=True, text=True, check=True
        )
        login = iniresult.stdout.splitlines()
        for line in login:
            if "Password auth succeeded for" in line:
                username = line.split("'")[1]
                users[username]["connected"] = True
                users[username]["connections"] += 1
                users[username]["last_connections"] += 1
            elif "Exit (" in line:
                username = line.split("(")[1].split(")")[0]
                users[username]["connected"] = False
                users[username]["last_connections"] = 0
    except subprocess.CalledProcessError:
        print(" \033[91m Error003: If there is a problem, please contact Defloper or Community\033[0m")
    return users
def lockunlock():
    clear()
    pathfiles = '/etc/qos/ssh/limituserssh.txt'
    usergme = []
    userlockunlock = []
    users_online = infoonline()
    with open(pathfiles, 'r') as f:
        f = f.readlines()
    for a in f:
        usergme.append(a)
    if usergme:
        while True:
            clear()
            print("  \033[34m╔═─────────────────────────────────────═╗\033[0m")
            print("  \033[31m┃\033[0m \033[1;31;44;1m           SSH Limit USER           \033[0m\033[31m ┃\033[0m")
            print("  \033[34m╚═─────────────────────────────────────═╝\033[0m")
            print(f"    \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            print("\033[34m ┌────────────────────────────────────────────┐\033[0m")
            for nom, line in enumerate(usergme, 1):
                nama_user = line.split()[0]
                try:
                    limituser = line.split()[1]
                    
                    lockunlocks = status_gmeuser(nama_user)
                    jumlah_koneksi = users_online.get(nama_user, {}).get("last_connections", 0)
                    status_online = "\033[92mOnline\033[0m" if users_online.get(nama_user, {}).get("connected", False) else "\033[91mOffline\033[0m"
                    print(" \033[94m<\033[0m\033[91m──────────────────────\033[0m\033[94m>\033[0m")
                    print(f"  \033[93m>_ {nom:<5}{nama_user}\033[0m")
                    print("  \033[92m SETATUS :\033[0m")
                    print(f"    \033[92m>_ Setatus : \033[0m\033[93m{lockunlocks}\033[0m")
                    print(f"    \033[92m>_ On/off : \033[0m\033[93m{status_online}\033[0n")
                    print(f"    \033[92m>_ Limit : \033[0m\033[93m{limituser}\033[0m")
                    print(f"    \033[92m>_ Connection :  \033[0m\033[93m{jumlah_koneksi}")
                    print(" \033[91m<\033[0m\033[94m──────────────────────\033[0m\033[91m>\033[0m")
                except (IndexError, ValueError):
                    print(f"  \033[91mError 1001: Invalid Format Please Contact Developer/Community\033[0m")
            print(f" \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress 'X' to go back to SSH menu or ( Ctrl + X )to exit.\n")
            listnum = input("\033[93m Select user to unblock/block: \033[0m ").strip()
            if listnum.lower() == "x":
                print(f"\033[93mExiting the SSHlimit process.\033[0m")
                time.sleep(0.5)
                clear()
                sshlimit()
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
                    while True:
                        print(" \033[94m<\033[0m\033[91m──────────────────────\033[0m\033[94m>\033[0m")
                        for user in userlockunlock:
                            subprocess.run(["passwd", "-u", user], check=True)
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
                    while True:
                        print(" \033[94m<\033[0m\033[91m──────────────────────\033[0m\033[94m>\033[0m")
                        for user in userlockunlock:
                            subprocess.run(["passwd", "-l", user], check=True)
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
            print(f" \033[91m┃\033[0m \033[94m          LIMIT SSH USER            \033[0m\033[91m ┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            print("")
            print("             \033[91m Empty Member\033[0m")
            print("")
            print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress Enter to go back to SSH menu or ( Ctrl + X )to exit.\n")
            user_input = input(" \033[93mPress Enter.. \033[0m").strip()
            if user_input.lower() == "":
                print(f"\033[93mExiting the SSHlimit process.\033[0m")
                time.sleep(0.5)
                sshlimit()
                return
            else:
                print("\033[91m What are you doing ?\033[0m")
                time.sleep(0.5)
def renewlimit():
    clear()
    pathfiles = '/etc/qos/ssh/limituserssh.txt'
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
            lolcat("\nPress 'X' to go back to SSH menu or (Ctrl + X) to exit.\n")
            listnum = input("\033[93mEnter the user number to renew (or 'x' to exit):\033[0m ").strip()
            if listnum.lower() == 'x':
                print(" \033[93mExiting renewal process.\033[0m")
                time.sleep(0.5)
                sshlimit()
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
                            sshlimit()
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
                                print(f"  \033[94mRenewal Ssh Limit Successful:\033[0m")
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
                                print(f"  \033[94mRenewal Ssh Limit Successful:\033[0m")
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
                                        print(f"  \033[94mRenewal Ssh Limit Successful:\033[0m")
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
                                sinden = input("\033[92m  SSH user limit reduction : \033[0m")
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
                                        print(f"  \033[94mRenewal Ssh Limit Successful:\033[0m")
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
            clear()
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m \033[94m          LIMIT User Renewal         \033[0m\033[91m ┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            print("")
            print("             \033[91m Empty Member\033[0m")
            print("")
            print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress Enter to go back to SSH menu or ( Ctrl + X )to exit.\n")
            user_input = input(" \033[93mPress Enter.. \033[0m").strip()
            if user_input.lower() == "":
                print(f"\033[93mExiting the SSHlimit process.\033[0m")
                time.sleep(0.5)
                clear()
                sshlimit()
                return
            else:
                print("\033[91m What are you doing ?\033[0m")
                time.sleep(0.5)
def aktif():
    pathsfile = "/etc/systemd/system/sshlimit.service"
    jasum = """\
[Unit]
Description=Monitor User auto banned&unbanned Ssh account by GME
After=network.target

[Service]
ExecStart=/usr/bin/python3 /usr/local/bin/sshlimit.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
    """
    with open(pathsfile, 'w') as f:
        f.write(jasum)
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl enable sshlimit.service")
    os.system("sudo systemctl start sshlimit.service")
def nonaktif():
    os.system("sudo systemctl stop sshlimit.service")
    os.system("sudo systemctl disable sshlimit.service")
    os.system('sudo find / -name "sshlimit.service"')
    os.system("sudo rm /etc/systemd/system/sshlimit.service")
def checkingg():
    service_name = "sshlimit"
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
        return(f" Error: {e}")
def onoffautoban():
    clear()
    service_name = "sshlimit"
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
                        print(" \033[92mSsh Limit Status Active\033[0m")
                        java = input("\033[93mPlease enter...\033[0m")
                        if java == "":
                            clear()
                            sshlimit()
                            return
                        else:
                            print(" \033[91m Please Enter!!!...\033[0m")
                elif jawa.lower() == "n":
                    clear()
                    sshlimit()
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
                        print(" \033[92mSsh Limit Status Offline\033[0m")
                        java = input("\033[93mPlease enter...\033[0m")
                        if java == "":
                            clear()
                            sshlimit()
                            return
                        else:
                            print(" \033[91m Please Enter!!!...\033[0m")
                elif sumatra.lower() == "n":
                    clear()
                    sshlimit()
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
                            print(" \033[92mSsh Limit Status Offline\033[0m")
                            java = input("\033[93mPlease enter...\033[0m")
                            if java == "":
                                clear()
                                sshlimit()
                                return
                            else:
                                print(" \033[91m Please Enter!!!...\033[0m")
                    elif sumatra.lower() == "n":
                        clear()
                        sshlimit()
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
                            print(" \033[92mSsh Limit Status Offline\033[0m")
                            java = input("\033[93mPlease enter...\033[0m")
                            if java == "":
                                clear()
                                sshlimit()
                                return
                            else:
                                print(" \033[91m Please Enter!!!...\033[0m")
                    elif sumatra.lower() == "n":
                        clear()
                        sshlimit()
                        return
                    else:
                        print(" \033[91m Please enter as instructed\033[0m")
    except Exception as e:
        print(f" Error: {e}")
def tdkmelangar():
    pathfile = "/etc/qos/ssh/alllimitssh"
    pathfile1 = "/etc/qos/ssh/limituserssh.txt"
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
    pathfile = "/etc/qos/ssh/alllimitssh"
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
def sshlimit():
    clear()
    cheks = checkingg()
    bann = check()
    jum = melangar()
    jum1 = tdkmelangar()
    back = importlib.import_module("modules.mmxsh")
    while True:
        print("     ", tampilan)
        print(f"    \033[91m>\033[0m\033[94m_\033[0m \033[93mviolate : \033[0m\033[91m{jum}\033[0m\033[93m user\033[0m \033[91m>\033[0m\033[94m_\033[0m \033[93m No violation :\033[0m\033[92m {jum1}\033[0m \033[93mUser\033[0m")
        print(f"    \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
        print(f"    \033[91m>\033[0m\033[94m_\033[0m \033[93mStatus :\033[0m {bann} \033[91m>\033[0m\033[94m_\033[0m \033[93mSetatus limit : \033[0m{cheks}")
        print(f"    \033[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
        print(f"    \033[31m| |\033[0m [\033[31m01\033[0m] Change Auto Banned Status")
        print(f"    \033[31m| |\033[0m [\033[31m02\033[0m] Change Unbanned Time")
        print(f"    \033[31m| |\033[0m [\033[31m03\033[0m] Unbanned / Banned manually")
        print(f"    \033[31m| |\033[0m [\033[31m04\033[0m] Renewal Limit SSH User")
        print(f"    \033[31m| |\033[0m [\033[31m05\033[0m] Stubborn user cleaner")
        print(f"    \033[91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
        print(f"    \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
        lolcat("\n  Press 'X' to go back to SSH menu or ( Ctrl + X )to exit.\n")
        opsi = input("  \033[93m Please Select Options: \033[0m").strip()
        if opsi.lower() == "x":
            clear()
            back.ssh_menu()
            return
        elif opsi == "1":
            clear()
            onoffautoban()
            return
        elif opsi == "2":
            os.system("clear")
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
        elif opsi == "5":
            clear()
            print("\033[93m Tunggu om/tante Sedang membersihkan Penguna yang membandel\033[0m")
            time.sleep(2)
            os.system("sudo systemctl restart ws-stunnel")
            os.system("sudo systemctl restart ws-dropbear")
            clear()
            lolfig("    Done Om")
            clear()
            sshlimit()
            return
        else:
            print("masukan opsi dek")