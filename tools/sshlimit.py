import os
from datetime import datetime, timedelta
import subprocess 
import time
from collections import defaultdict
logssh = '/var/log/limitssh.log'
logssws = '/var/log/sshbanned.log'
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
def check(paths):
    if os.path.exists(paths):
        print(" File ada")
        return
    else:
        print("file Tidak ada")
        with open(paths, 'w') as f:
            pass
        return
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
        gme_log(" \033[91m Error003: If there is a problem, please contact Defloper or Community\033[0m")
    return users
def banned():
    userss = infoonline()
    pathfile1 = "/etc/qos/ssh/limituserssh.txt"
    alluser = []
    hasill = []
    hasil1 = []
    pathfiles1 = "/etc/qos/ssh/alllimitssh"
    pathfiles = "/etc/qos/ssh/waktussh"
    with open(pathfile1, 'r') as file:
        baris = file.readlines()
    for line in baris:
        semua = line.strip().split()
        if len(semua) == 2 and semua[1].isdigit():
            alluser.append(line.strip())
    for line in alluser:
        alll = line.strip().split()
        if len(alll) == 2:
            user = alll[0]
            limit = alll[1]
            total = userss.get(user, {}).get("last_connections", 0)
            if int(limit) < int(total):
                gme_log1(f" \033[91mBanned\nUser : \033[0m\033[92m{user}\033[0m\n\033[91mlimit : \033[0m\033[92m{limit}\033[0m\n\033[91m Total: \033[0m\033[92m{total}\033[0m")
                gme_log(f" \033[91mBanned\nUser : \033[0m\033[92m{user}\033[0m\n\033[91mlimit : \033[0m\033[92m{limit}\033[0m\n\033[91m Total: \033[0m\033[92m{total}\033[0m")
                hasill.append(user)
            else:
                hasil1.append(user)
    if hasill:
        print(f"hasill")
        for user in hasill:
            print(f"ya {user}")
            subprocess.run(["passwd", "-l", user], check=True)
            gme_log(f" \033[93mUser \033[91m{user}\033[0m\033[93m has been locked\033[0m ")
        with open(pathfiles, 'r') as file:
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
        print("mengecek file")
        check(pathfiles1)
        for usr in hasill:
            try:
                with open(pathfiles1, 'r') as a:
                    lines = a.readlines()
            except FileNotFoundError:
                lines = []
            lines.append(str(usr) + ' ' + str(waktu1) + '\n')
            with open(pathfiles1, 'w') as f:
                f.writelines(lines)
            gme_log(f" \033[93mUser Unlock Time \033[0m\033[92m{usr} {waktu1}\033[0m")
    else:
        gme_log(" \033[93m No users are exceeding the limit at this time\033[0m ")

    if hasil1:
        print("hasil1")
        for userr in hasil1:
            print(f"tidak {userr}")

def unbanned():
    pathfiles1 = "/etc/qos/ssh/alllimitssh"
    sekarang = datetime.now()
    userno = []
    userya = []
    with open(pathfiles1, 'r') as f:
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
                        gme_log(f" \033[91m User {user} can't be unbanned yet\033[0m")
                        userno.append(user)
                    else:
                        gme_log1(f"\033[92mUnbanned\033[0m\033[92m User : \033[0m ")
                        gme_log(f"\033[92mUnbanned\033[0m\033[92m User : \033[0m ")
                        userya.append(user)
                except ValueError:
                    gme_log(f"\033[91m Error 1001: Unsupported Format: {lines.strip} Please Contact Defloper\033[0m")
    if userya:
        for user in userya:
            subprocess.run(["passwd", "-u", user], check=True)
            gme_log(f" \033[93m{user} \033[0m\033[92m successfully unblocked\033[0m")
            gme_log1(f" \033[93m{user} \033[0m\033[92m successfully unblocked\033[0m")
        with open(pathfiles1, 'r') as file:
            lines = file.readlines()
        new_lines = [
            line for line in lines
            if not any(line.strip().startswith(name_user) for name_user in userya)
            ]
        with open(pathfiles1, 'w') as file:
            file.writelines(new_lines)
    else:
        gme_log("\033[93m There are no users to unblock yet\033[0m")
        gme_log1("\033[93m There are no users to unblock yet\033[0m")
        
        

def main():
    wak = 1
    nit = wak * 60
    while True:
        gme_log(f"\033[92mINFO : \033[0m\033[93m---SSH limit Logs---\033[0m")
        banned()
        unbanned()
        gme_log(f"\033[92mINFO : \033[0m\033[93m{wak} minutes Time Break To Restart\033[0m")
        time.sleep(nit)
if __name__ == "__main__":
    main()
    