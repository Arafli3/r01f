import os
from .lolcat import lolcat
import time
from datetime import datetime, timedelta
import importlib
import signal
def shampo_clear():
    os.system("clear")
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)
def trojan_data():
    back = importlib.import_module("modules.tt")
    pathfil1 = "/etc/qos/xray/trojan.txt"
    gmelist = []
    with open(pathfil1, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('###'):
                gmelist.append(line)
    if gmelist:
        while True:
            shampo_clear()
            print("\033[34m╔═\033[0m\033[31m─────────────────────────────────────\033[0m\033[34m═╗\033[0m")
            print("\033[31m┃\033[0m \033[1;31;44;1m       LOG CREATE TROJAN ACCOUNTS     \033[0m\033[31m ┃\033[0m")
            print("\033[34m╚═\033[0m\033[31m─────────────────────────────────────\033[0m\033[34m═╝\033[0m")
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
            lolcat("\nPress 'X' to go back to TROJAN menu or ( Ctrl + X )to exit.\n")
            print("\033[93m Select Number To View Account Data Log (or 'x' to exit):\033[0m \n")
            listnum = input("\033[93m Input Number: \033[0m").strip()
            if listnum.lower() == "x":
                print(f"\033[93mExiting the TROJAN log data process.\033[0m")
                time.sleep(0.5)
                shampo_clear()
                back.trojan_menu()
                return
            elif listnum == "":
                trojan_data()
            elif listnum.isdigit() and 1 <= int(listnum) <= len(gmelist):
                selected_user = gmelist[int(listnum) - 1].strip()
                nama_user = selected_user.split()[1]
                expiration_date_str = selected_user.split()[2]
                pathfile2 = f"/etc/xraylog/log-trojan-{nama_user}.txt"
                while True:
                    try:
                        with open(pathfile2, "r") as memex:
                            duar = memex.read()
                            shampo_clear()
                            print(duar)
                    except FileNotFoundError:
                        print("\033[91m Please contact Defloper or the community \033[0m")
                    print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
                    lolcat("\n Press Enter to return to log data account or type 'x' to exit...\n")
                    userada = input("\033[93mEnter Options :\033[0m").strip()
                    if userada.lower() == "x":
                        print(f"\033[93mExiting the Trojan log data process.\033[0m")
                        time.sleep(0.5)
                        shampo_clear()
                        back.trojan_menu()
                        return
                    elif userada == "":
                        trojan_data()
                    else:
                        print("\033[91m What are you doing Please Enter\033[0m")
                        time.sleep(0.5)
                        shampo_clear()
            else:
                print(f"\033[91m Please enter correctly\033[0m")
    else:
        while True:
            print("\033[34m╔═\033[0m\033[31m─────────────────────────────────────\033[0m\033[34m═╗\033[0m")
            print("\033[31m┃\033[0m \033[1;31;44;1m       LOG CREATE TROJAN ACCOUNTS     \033[0m\033[31m ┃\033[0m")
            print("\033[34m╚═\033[0m\033[31m─────────────────────────────────────\033[0m\033[34m═╝\033[0m")
            print("")
            print("              \033[33mYou have no existing clients!\033[0m")
            print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress Enter to go back to TROJAN menu or ( Ctrl + X )to exit.\n")
            nouser = input("\033[93m Please Press Enter\033[0m")
            if nouser == "":
                print(f"\033[93mExiting the TROJAN log data process.\033[0m")
                time.sleep(0.5)
                shampo_clear()
                back.trojan_menu()
                return
            else:
                print("\033[91m What are you doing Please Enter\033[0m")
                time.sleep(0.5)
                shampo_clear()