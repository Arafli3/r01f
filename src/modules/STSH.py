import subprocess
from collections import defaultdict
from .lolcat import lolcat
import time
import os
import importlib
def clear():
    os.system("clear")
def gmeuser(uid_target):
    usernames = []
    try:
        with open('/etc/passwd', 'r') as file:
            for baris in file:
                parts = baris.strip().split(':')
                if len(parts) >= 7:
                    username = parts[0]
                    uid = int(parts[2])
                    if uid >= uid_target and username != "nobody":
                        usernames.append(username)
    except FileNotFoundError:
        print(" \033[91m Error001: If there is a problem, please contact Defloper or Community\033[0m")
    return usernames

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

def statussUserSSH():
    clear
    uid_target = 1000
    usernames = gmeuser(uid_target)
    users_online = infoonline()
    back = importlib.import_module("modules.mmxsh")
    if not usernames:
        print("\033[34m╔═─────────────────────────────────────═╗\033[0m")
        print("\033[31m┃\033[0m \033[1;31;44;1m            SSH ONLINE USER           \033[0m\033[31m ┃\033[0m")
        print("\033[34m╚═─────────────────────────────────────═╝\033[0m")
        print("\033[34m┌────────────────────────────────────────────┐\033[0m")
        print("")
        print("             \033[91m Empty Member\033[0m")
        print("")
        print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
        print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
        lolcat("\nPress Enter to go back to SSH menu or ( Ctrl + X )to exit.\n")
        while True:
            opsi = input(" \033[91m Please Enter...\033[0m")
            if opsi == "":
                print(" \033[91m Back to Ssh menu\033[0m")
                time.sleep(0.5)
                clear()
                back.ssh_menu()
                return
            else:
                print(" \033[91m what are you doing? please enter\033[0m")
    while True:
        clear()
        print("  \033[34m╔═─────────────────────────────────────═╗\033[0m")
        print("  \033[31m┃\033[0m \033[1;31;44;1m           SSH ONLINE USER           \033[0m\033[31m ┃\033[0m")
        print("  \033[34m╚═─────────────────────────────────────═╝\033[0m")
        print(f"    \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
        print("\033[34m ┌────────────────────────────────────────────┐\033[0m")
        for i, username in enumerate(usernames, start=1):
            status_online = "\033[92mOnline\033[0m" if users_online.get(username, {}).get("connected", False) else "\033[91mOffline\033[0m"
            status_lock = status_gmeuser(username)
            jumlah_koneksi = users_online.get(username, {}).get("last_connections", 0)
            prinst = (f"""
   \033[94m<\033[0m\033[91m──────────────────────\033[0m\033[94m>\033[0m
     \033[93mUser SSH No \033[0m{i}. \033[93m{username}\033[0m
     \033[93mStatus User :\033[0m {status_online}
     \033[93mStatus Lock User :\033[0m {status_lock}
     \033[93mConnected Users :\033[0m {jumlah_koneksi}
   \033[91m<\033[0m\033[94m──────────────────────\033[0m\033[91m>\033[0m""")
            print(  prinst)
        print("\033[34m └────────────────────────────────────────────┘\033[0m")
        print("")
        lolcat(" Select Number Each user, can select more than 1, \n or (x) to exit the ssh User Status menu\n")
        opsi = input("\033[93m Select option : \033[0m").strip()
        if opsi.lower() == "x":
            print(" \033[91m Back to Ssh menu\033[0m")
            time.sleep(0.5)
            clear()
            back.ssh_menu()
            return
        pilihanmu = [int(x.strip()) - 1 for x in opsi.split(",") if x.strip().isdigit()]
        if pilihanmu:
            break
        else:
            time.sleep(0.5)
            print(" \033[91m Please select the correct option\033[0m")
    while True:
        clear()
        selected_users = []
        print(" \033[94m<\033[0m\033[91m──────────────────────\033[0m\033[94m>\033[0m")
        for index in pilihanmu:
            if 0 <= index < len(usernames):
                selected_users.append(usernames[index])
                print(f"   \033[92m- {usernames[index]}\033[0m")
        print(" \033[91m<\033[0m\033[94m──────────────────────\033[0m\033[91m>\033[0m")
        lolcat(" Select Unlock or Lock to change the status of the User ssh account\n Or (x) To cancel")
        action = input("\n \033[93m Select (unlock/lock) : \033[0m").strip().lower()
        try:
            if action == "x":
                clear()
                statussUserSSH()
                return
            elif action == "unlock":
                while True:
                    clear()
                    print(" \033[94m<\033[0m\033[91m──────────────────────\033[0m\033[94m>\033[0m")
                    for username in selected_users:
                        subprocess.run(["passwd", "-u", username], check=True)
                        print(f" \033[92mAccount \033[0m\033[93m{username} \033[0m\033[92mSuccessfully Unlocked.\033[0m")
                    print(" \033[91m<\033[0m\033[94m──────────────────────\033[0m\033[91m>\033[0m")
                    opsi1 = input(" \033[91mPlease Enter...\033[0m")
                    if opsi1 == "":
                        clear()
                        statussUserSSH()
                        return
                    else:
                        print(" \033[91m what are you doing? please enter\033[0m")
            elif action == "lock":
                while True:
                    clear()
                    print(" \033[94m<\033[0m\033[91m──────────────────────\033[0m\033[94m>\033[0m")
                    for username in selected_users:
                        subprocess.run(["passwd", "-l", username], check=True)
                        print(f" \033[92mAccount \033[0m\033[93m{username} \033[0m\033[92mSuccessfully locked.\033[0m")
                    print(" \033[91m<\033[0m\033[94m──────────────────────\033[0m\033[91m>\033[0m")
                    opsi1 = input(" \033[91mPlease Enter...\033[0m")
                    if opsi1 == "":
                        clear()
                        statussUserSSH()
                        return
                    else:
                        print(" \033[91m what are you doing? please enter\033[0m")
            else:
                print(" \033[91m Please select according to the options\033[0m")
        except subprocess.CalledProcessError:
            print(" \033[91m Error004: If there is a problem, please contact Defloper or Community\033[0m")