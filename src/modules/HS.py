import os
import subprocess
from datetime import datetime
import signal
import time
from .lolcat import lolcat
import importlib
    
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)
def clear():
    os.system("clear")
def prints(text, color):
    print(f"\033[{color}m{text}\033[0m")
    
def get_server_date():
    try:
        result = subprocess.check_output(
            ["curl", "-sI", "https://google.com"], stderr=subprocess.DEVNULL
        ).decode("utf-8")
        for line in result.splitlines():
            if line.startswith("Date:"):
                return datetime.strptime(line.split("Date: ")[1], "%a, %d %b %Y %H:%M:%S GMT")
    except Exception:
        pass
    return datetime.now()

def clear_console():
    os.system("clear")

def list_users():
    back = importlib.import_module("modules.mmxsh")
    path1 = '/etc/qos/ssh/sshadmin.txt'
    gmelist = []
    usrdel =[]
    with open(path1, 'r') as f:
        a = f.readlines()
        for b in a:
            if b.startswith('###'):
                gmelist.append(b)
    if gmelist:
        while True:
            clear()
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m \033[94m          DELETE SSH USER            \033[0m\033[91m ┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            lolcat(f"  \033[93m{'No.':<5}{'User':<10}{'Expired':<15}{'Status':<20}\033[0m")
            print(f"  \n\033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            for idx, line in enumerate(gmelist, 1):
                nama_user = line.split()[1]
                try:
                    expiration_date_str = line.split()[2]
                    expiration_date = datetime.strptime(expiration_date_str, "%Y-%m-%d:%H")
                    today = datetime.now()
                    remaining_time = expiration_date - today
                    remaining_days = remaining_time.days
                    exp_format = expiration_date.strftime("%Y-%m-%d")
                    exp_hour = expiration_date.strftime("%H:%M")
                    if remaining_days > 0:
                        status = f"\033[93m{remaining_days}\033[0m \033[92manother day\033[0m"
                    elif remaining_days == 0:
                        status = f"\033[92mExpired Today at \033[0m\033[91m{exp_hour} \033[0m\033[92mo'clock\033[0m"
                    elif remaining_days < 0:
                        status = f"\033[91m{remaining_days} Expired \033[0m"
                    else:
                        status = f"\033[91mExpired\033[0m "
                    print(f"  \033[93m{idx:<5}{nama_user:<10}{exp_format:<15}\033[0m{status:<20}")
                except (IndexError, ValueError):
                    print(f"  \033[91m{idx:<5}{nama_user:<10}{'N/A':<15}{'Invalid Date':<20}\033[0m")

            print(f" \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress 'X' to go back to SSH menu or ( Ctrl + X )to exit.\n")
            listnum = input("\033[93mEnter the user number you want to delete (or 'x' to exit):\033[0m ").strip()
            if listnum.lower() == "x":
                print(f"\033[93mExiting the SSH delete process.\033[0m")
                time.sleep(0.5)
                clear()
                back.ssh_menu()
                return
            try:
                listnumb = [int(x.strip()) for x in listnum.split(',')]
                if any(baris <= 0 or baris > len(gmelist) for baris in listnumb):
                    print("\033[91mInvalid user number.\033[0m")
                    continue
                listhap = [gmelist[baris - 1].strip() for baris in listnumb]
            except (ValueError, UnboundLocalError):
                print(" \033[91mPlease enter the correct input\033[0m")
                continue 
            print(f" \033[94m┌───────────────────────────────────┐\033[0m")
            print(f"           \033[91m User to be deleted\033[0m")
            print(f" \033[94m└───────────────────────────────────┘\033[0m")
            for list1, baris in zip(listnumb, listhap):
                nama_user = baris.split()[1]
                usrdel.append(nama_user)
                print(f"                \033[93m{list1}: {nama_user}\033[0m")
            print(f"   \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            while True:
                konfirmasi = input(f"\033[93m Are you sure to delete the {len(usrdel)} users above?(y/n): \033[0m").strip().lower()
                if konfirmasi == "y":
                    print(f" \033[92m The process of deleting\033[0m")
                    time.sleep(0.5)
                    for baris in sorted(listnumb, reverse=True):
                        gmelist.pop(baris - 1)
                    with open(path1, 'r') as file:
                        baris = file.readlines()
                    with open(path1, 'w') as file:
                        for line in baris:
                            if not any(f"### {user} " in line for user in usrdel):
                                file.write(line)
                    print("Delete Successful")
                    for user in usrdel:
                        checkusr = subprocess.run(["id", user], capture_output=True, text=True)
                        if checkusr.returncode == 0:
                            print(f"Delete {user}")
                            subprocess.run(["userdel", "-r", user])
                        else:
                            print(f"User Not Found {user}")
                    for file1 in usrdel:
                        b = [f"/etc/xraylog/log-ssh-{file1}.txt"]
                        for a in b:
                            if os.path.exists(a):
                                os.remove(a)
                                print(f" {a} successfully deleted")
                            else:
                                print(f" {a} User not found")
                    pathfiles12 = "/etc/qos/ssh/limituserssh.txt"
                    with open(pathfiles12, 'r') as f:
                        lines = f.readlines()
                    lines_new = [
                        line for line in lines
                        if not any(line.strip().startswith(name_user) for name_user in usrdel)
                        ]
                    with open(pathfiles12, 'w') as file:
                        file.writelines(lines_new)
                    print("process Successful")
                    clear()
                    print(f" \033[94m┌───────────────────────────────────┐\033[0m")
                    for user in usrdel:
                        print(f" \033[92m        User \033[0m \033[91m {user} \033[0m \033[92m Deleted\033[0m ")
                    print(f" \033[94m└───────────────────────────────────┘\033[0m")
                    print(f"      \033[93m Amount Deleted : \033[0m\033[93m{len(usrdel)}\033[0m")
                    print(f"   \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
                    print(f" \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
                    lolcat("\nPress Enter to go back to SSH menu or ( Ctrl + X )to exit.\n")
                    while True:
                        action = input("\033[93mInput Options:\033[0m ").strip().lower()
                        if action == "x":
                            print("\033[93m Exiting SSH Account Delete Process\033[0m")
                            time.sleep(0.5)
                            os.system("clear")
                            back.ssh_menu()
                            break
                        elif action == "":
                            os.system("clear")
                            list_users()
                            return
                        else:
                            print("\033[91mPlease enter 'x' to exit or press Enter to return.\033[0m")
                elif konfirmasi == 'n':
                    print("\033[92m cancel delete user\033[0m")
                    time.sleep(0.5)
                    clear()
                    list_users()
                    return
                else:
                    print( "\033[91m Please Select According to Option\033[0m")
    else:
        while True:
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m \033[94m          DELETE SSH USER            \033[0m\033[91m ┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            print("")
            print("             \033[91m Empty Member\033[0m")
            print("")
            print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress Enter to go back to SSH menu or ( Ctrl + X )to exit.\n")
            user_input = input(" \033[93mPress Enter.. \033[0m").strip()
            if user_input.lower() == "":
                print(f"\033[93mExiting the SSH Delete process.\033[0m")
                time.sleep(0.5)
                back.ssh_menu()
                return
            else:
                print("\033[91m What are you doing ?\033[0m")
                time.sleep(0.5)