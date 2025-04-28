import json
from datetime import datetime, timedelta
from pathlib import Path
import os
import re
import subprocess
import time
import importlib
from .lolcat import lolcat
import signal
def run(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"\033[91m An error occurred while executing the command {e}\033[0m")
        print(e.stderr.decode())
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)
signal.signal(signal.SIGINT, handle_sigint)
def clear_screen():
    os.system('clear')
def Delete_vmess():
    pathfil1 = '/etc/qos/xray/vmess.txt'
    pathfil2 = '/etc/qos/xray/xrayall.txt'
    pathfil3 = '/etc/xray/config.json'
    uuidpath = '/etc/qos/xray/uuid.txt'
    gmelist = []
    usrdel = []
    back = importlib.import_module("modules.vevek")
    clear_screen()
    with open(pathfil1, 'r') as file1:
        lines = file1.readlines()
        for line in lines:
            if line.startswith('###'):
                gmelist.append(line)
    
    if gmelist:
        while True:
            clear_screen()
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m \033[94m          DELETE VMESS USER          \033[0m\033[91m ┃\033[0m")
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
            lolcat("\nPress 'X' to go back to VMESS menu or ( Ctrl + X )to exit.\n")
            listnum = input("\033[93mEnter the user number you want to delete (or 'x' to exit):\033[0m ").strip()
            if listnum.lower() == "x":
                print(f"\033[93mExiting the VMESS delete process.\033[0m")
                time.sleep(0.5)
                clear_screen()
                back.vmess_menu()
                return
            try:
                listnumb = [int(x.strip()) for x in listnum.split(',')]
                if any(baris <= 0 or baris > len(gmelist) for baris in listnumb):
                    print("\033[91mInvalid user number.\033[0m")
                    continue
                listhap = [gmelist[baris - 1].strip() for baris in listnumb]
            except (ValueError, UnboundLocalError):
                print("harap masukan yang benar")
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
                    with open(pathfil1, 'w') as file1:
                        file1.writelines(gmelist)
                    with open(pathfil2, 'r') as file2:
                        file2_lines = file2.readlines()
                    updatedfile2 = [line for line in file2_lines if line.strip() not in listhap]
                    with open(pathfil2, 'w') as file2:
                        file2.writelines(updatedfile2)
                    with open(pathfil3, 'r') as json_file:
                        config_data = json.load(json_file)
                    user_delete = [line.split()[1] for line in listhap]
                    uuid_delete = []
                    clients_ws = config_data["inbounds"][1]["settings"]["clients"]
                    for client in clients_ws:
                        if client["email"] in user_delete:
                            uuid_delete.append(client["id"])
                    clients_grpc = config_data["inbounds"][2]["settings"]["clients"]
                    for client in clients_grpc:
                        if client["email"] in user_delete:
                            uuid_delete.append(client["id"])
                    with open(uuidpath, 'r') as uuid_file:
                        uuid_lines = uuid_file.readlines()
                    updated_uuid = [line for line in uuid_lines if line.strip() not in uuid_delete]
                    with open(uuidpath, 'w') as uuid_file:
                        uuid_file.writelines(updated_uuid)
                    clientsws = [client for client in clients_ws if client["email"] not in user_delete]
                    config_data["inbounds"][1]["settings"]["clients"] = clientsws
                    updatedgrpc = [client for client in clients_grpc if client["email"] not in user_delete]
                    config_data["inbounds"][2]["settings"]["clients"] = updatedgrpc
                    with open(pathfil3, 'w') as json_file:
                        json.dump(config_data, json_file, indent=2)
                        user_delete = [line.split()[1] for line in listhap]
                    for nama_user in user_delete:
                        relatedfiles = [
                            f"/etc/xraylog/log-vmess-{nama_user}.txt",
                            f"/var/www/html/vmess-{nama_user}",
                            f"/etc/qos/xray/usage/{nama_user}",
                        ]
                        for filess in relatedfiles:
                            file = Path(filess)
                            if file.is_file():
                                try:
                                    file.unlink()
                                    print(f"\033[92m Successfully Delete...\033[0m.")
                                    clear_screen()
                                except Exception as e:
                                    print(f"\033[91mError Please Contact Defloper/community : {e}\033[0m")
                            else:
                                print(f"\033[91mError Please Contact Defloper/community.\033[0m")
                    pathfile = "/etc/qos/xray/limitxray"
                    with open(pathfile, 'r') as f:
                        lines = f.readlines()
                    lines_new = [
                        line for line in lines
                        if not any(line.strip().startswith(name_user) for name_user in usrdel)
                        ]
                    with open(pathfile, 'w') as file:
                        file.writelines(lines_new)
                    run("systemctl restart xray")
                    print(f" \033[94m┌───────────────────────────────────┐\033[0m")
                    for user in usrdel:
                        print(f" \033[92m        User \033[0m \033[91m {user} \033[0m \033[92m Deleted\033[0m ")
                    print(f" \033[94m└───────────────────────────────────┘\033[0m")
                    print(f"      \033[93m Amount Deleted : \033[0m\033[93m{len(usrdel)}\033[0m")
                    print(f"   \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
                    print(f" \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
                    lolcat("\nPress Enter to go back to VMESS menu or ( Ctrl + X )to exit.\n")
                    while True:
                        action = input("\033[93mInput Options:\033[0m ").strip().lower()
                        if action == "x":
                            print("\033[93m Exiting VMESS Account Delete Process\033[0m")
                            time.sleep(0.5)
                            os.system("clear")
                            back.vmess_menu()
                            break
                        elif action == "":
                            os.system("clear")
                            Delete_vmess()
                            return
                        else:
                            print("\033[91mPlease enter 'x' to exit or press Enter to return.\033[0m")
                elif konfirmasi == "n":
                    usrdel.clear()
                    break
                elif konfirmasi == "":
                    print("\033[91m Please enter according to the instructions \033[0m")
                    time.sleep(0.5)
                else:
                    print("\033[91m what do you do, input according to the command \033[0m")
                    time.sleep(0.5)
            else:
                print("\033[91m Please enter according to the instructions \033[0m")
    else:
        while True:
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m \033[94m          DELETE VMESS USER          \033[0m \033[91m┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            print("")
            print("             \033[91m Empty Member\033[0m")
            print("")
            print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress Enter to go back to VMESS menu or ( Ctrl + X )to exit.\n")
            user_input = input(" \033[93mPress Enter.. \033[0m").strip()
            if user_input.lower() == "":
                print(f"\033[93mExiting the VMESS Delete process.\033[0m")
                time.sleep(0.5)
                back.vmess_menu()
                return
            else:
                print("\033[91m What are you doing ?\033[0m")
                time.sleep(0.5)
                clear_screen()