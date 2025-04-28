import os
import re
from datetime import datetime, timedelta
import time
import signal
from .lolcat import lolcat
import importlib
import json
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)
def clear_screen():
    os.system("clear")
def convert(bytesvaule):
    units = ["Bytes", "KB", "MB", "GB", "TB"]
    size = bytesvaule
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f" {size:.2f}{units[index]}"

def RNT_main():
    back = importlib.import_module("modules.tt")
    pathfil1 = '/etc/qos/xray/trojan.txt'
    gmelist = []
    with open(pathfil1, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('###'):
                gmelist.append(line)

    if gmelist:
        exittol = False
        while not exittol:
            clear_screen()
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m \033[94m          RENEWAL TROJAN USER          \033[0m\033[91m ┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            lolcat(f"  \033[93m{'No.':<5}{'User':<13}{'Expired':<15}{'Status':<20}\033[0m")
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
                    else:
                        status = f"\033[91m{abs(remaining_days)} Expired\033[0m"
                    print(f"  \033[93m{idx:<5}{nama_user:<13}{exp_format:<15}\033[0m{status:<20}")
                except (IndexError, ValueError):
                    print(f"  \033[91m{idx:<5}{nama_user:<13}{'N/A':<15}{'Invalid Date':<20}\033[0m")

            print(f" \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress 'X' to go back to TROJAN menu or (Ctrl + X) to exit.\n")
            listnum = input("\033[93mEnter the user number to renew (or 'x' to exit):\033[0m ").strip()

            if listnum.lower() == 'x':
                print(" \033[93mExiting renewal process.\033[0m")
                time.sleep(0.5)
                back.trojan_menu()
                break
            elif listnum.isdigit() and 1 <= int(listnum) <= len(gmelist):
                selected_user = gmelist[int(listnum) - 1].strip()
                nama_user = selected_user.split()[1]
                expiration_date_str = selected_user.split()[2]
                pathfils2 = f"/etc/qos/xray/usage/{nama_user}"
                with open(pathfils2, "r") as f:
                    bytesvaule = f.read().strip()
                if bytesvaule.lower() == "unlimited":
                    bapakmu = "unlimited"
                else:
                    try:
                        bytesvaule = int(bytesvaule)
                        bapakmu = convert(bytesvaule)
                    except ValueError:
                        bapakmu = "invalid"
                print("     \033[34m#############-\033[0m")
                print("     \033[31m-------------------------------\033[0m")
                print(f"  \033[94mSelected User Details:\033[0m")
                print(f"  \033[93mUsername  : {nama_user}\033[0m")
                print(f"  \033[93mExpiration: {expiration_date_str}\033[0m")
                print(f"  \033[93mQuota : {bapakmu}")
                print("     \033[34m-------------------------------\033[0m")
                print("     \033[31m##############-\033[0m")

                while not exittol:
                    pathfilse2 = f"/etc/qos/xray/usage/{nama_user}"
                    confirm = input(f" \033[93mConfirm renew for user '{nama_user}'? (y/n):\033[0m ").strip().lower()
                    if confirm == 'y':
                        print(f" \033[92mRenewing account for user '{nama_user}'...\033[0m")
                        with open(pathfilse2, "r") as f:
                            dataquo = f.read().strip().lower()
                        if dataquo == "unlimited":
                            quota = ""
                            exittol = True
                            break
                        while True:
                            lolcat("\nPress 'X' to go back to TROJAN menu/cancel or (Ctrl + X) to exit.\n")
                            lolcat("  \nAdd Quotaa \n")
                            try:
                                quota = input(" \033[93mInput quota (GB): \033[0m ").strip().lower()
                                if quota == "":
                                    print(f" \033[92m Not Adding Quota on confirmation\033[0m")
                                    exittol = True
                                    break
                                if quota == "x":
                                    print(f" \033[93mExiting the TROJAN renewal process.\033[0m")
                                    time.sleep(0.5)
                                    back.trojan_menu()
                                    return
                                quota_gb = int(quota)
                                print(f" \033[92mQuota added.\033[0m")
                                exittol = True
                                break
                            except ValueError:
                                    print(" \033[91mInvalid input. Please enter a number.\033[0m")
                    elif confirm == 'n':
                        print(" \033[93mReturning to user list...\033[0m")
                        time.sleep(1)
                        RNT_main()
                        break
                    else:
                        print(" \033[91mInvalid choice. Returning to user list...\033[0m")
                        time.sleep(1)
                while True:
                    lolcat("\nPress 'X' to go back to TROJAN menu/cancel or (Ctrl + X) to exit.\n")
                    lolcat(" \nAdd Active Period\n")
                    try:
                        masaaktif = input(" \033[93m Input duration (Day): \033[0m").strip()
                        if masaaktif == "x":
                            print(" \033[93mExiting the TROJAN renewal process.\033[0m")
                            time.sleep(0.5)
                            back.trojan_menu()
                            return
                        masaaktif_days = int(masaaktif)
                        if masaaktif_days > 10000:
                            print(" \033[91mDuration too large! Maximum allowed is 10000 days.\033[0m")
                        else:
                            print(" \033[92mDuration added.\033[0m")
                            exittol = True
                            break
                    except ValueError:
                        print(" \033[91mInvalid input. Please enter a number.\033[0m")
            else:
                print("\033[91mInvalid selection. Please try again.\033[0m")
                time.sleep(1)
        pathfil2 = f"/etc/qos/xray/usage/{nama_user}"
        pathfil3 = '/etc/xray/config.json'
        if os.path.exists(pathfil2):
            with open(pathfil2, "r") as file:
                data = file.read().strip()
                current_quota = int(data) if data.isdigit() else 0
        else:
            current_quota = 0
            print(f"Current quota: {current_quota} bytes")
            
        quotauupdate = ""
        for _ in range(1):
            if quota:
                if quota.isdigit():
                    new_quota = int(quota) * 1024 * 1024 * 1024
                    total_quota = current_quota + new_quota
                    quotauupdate += str(total_quota) + " "
                    quotauupdate = quotauupdate.strip()
                    with open(pathfil2, "w") as file:
                        file.write(str(total_quota))
                        print(f"New total quota: {total_quota} bytes")
                else:
                    print("Invalid input. No changes made.")
            else:
                print("No quota input. No changes made.")
        if quota:
            with open(pathfil3, "r") as file:
                config_data = json.load(file)
            client_list = config_data["inbounds"][1]["settings"]["clients"]
            for client_data in client_list:
                if client_data.get("email") == nama_user:
                    client_data["quota"] = quotauupdate
            with open(pathfil3, "w") as f:
                json.dump(config_data, f, indent=4)
        else:
            print(" no quota input1.")
        
        with open(pathfil1, "r") as file:
            lines = file.readlines()
        updated1lines = []
        masaaktif = int(masaaktif)
        updatexp = ""
        user_found = False
        for line in lines:
            if line.startswith(f"### {nama_user} "):
                user_found = True
                strdatasatini = line.split()[2]
                datasatini = datetime.strptime(strdatasatini, "%Y-%m-%d:%H")
                databaru = datasatini + timedelta(days=masaaktif)
                strdatabaru = databaru.strftime("%Y-%m-%d:%H")
                updatedline = f"### {nama_user} {strdatabaru}\n"
                updated1lines.append(updatedline)
                updatexp += strdatabaru + " "
                updatexp = updatexp.strip()
            else:
                updated1lines.append(line)
        with open(pathfil1, "w") as file:
            file.writelines(updated1lines)
        if user_found:
            print(f"Masa aktif untuk pengguna '{nama_user}' telah diperbarui.")
        else:
            print(f"Pengguna '{nama_user}' tidak ditemukan dalam file.")
        indexs = [1, 2,]
        with open(pathfil3, "r") as file:
            users = json.load(file)
        for index in indexs:
            user = users["inbounds"][index]["settings"]["clients"]
            for client in user:
                if client.get("email") == nama_user:
                    client["expiry"] = updatexp
                    print("berhasil json")
        with open(pathfil3, "w") as f:
            json.dump(users, f, indent=4)
        with open(pathfils2, "r") as f:
            bytesvaule = f.read().strip()
        if bytesvaule.lower() == "unlimited":
            quota_bytes = int(data) if data.isdigit() else 0
            quotagb1 = "unlimited"
        else:
            try:
                with open(pathfils2, "r") as file:
                    data = file.read().strip()
                quota_bytes = int(data) if data.isdigit() else 0
                quotagb1 = quota_bytes / (1024 ** 3)
            except FileNotFoundError:
                quota_bytes = 0
        os.system("systemctl restart xray")
        clear_screen()
        print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
        print(f" \033[91m┃\033[0m \033[94m      Renewal Account  Succesfully   \033[0m\033[91m ┃\033[0m")
        print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
        print("")
        print(f" \033[94m#########\033[0m\033[93m Trojan Account \033[0m\033[91m#########\033[0m")
        print(f" \033[94m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐\033[0m")
        print(f" \033[93mClient Name : \033[0m\033[92m{nama_user}\033[0m")
        print(f" \033[93mUsage Qouta :\033[0m \033[92m{quotagb1}\033[0m")
        print(f" \033[93mAdd quota :\033[0m\033[92m {quota}\033[0m")
        print(f" \033[93mExpired On :\033[0m\033[92m {updatexp}\033[0m")
        print(f" \033[93mAdd active period On :\033[0m\033[92m {masaaktif}\033[0m")
        print( "")
        print(f" \033[94m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\033[0m")
        print(f" \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
        lolcat("\n Press Enter to return to renewal account or type 'x' to exit...\n")
        while True:
            action = input(" \033[93mInput Options:\033[0m ").strip().lower()
            if action == "x":
                print(f"\033[93mExiting the TROJAN renewal process.\033[0m")
                time.sleep(0.5)
                os.system("clear")
                back.trojan_menu()
                return
            elif action == "":
                os.system("clear")
                RNT_main()
                return
            else:
                print("\033[91mPlease enter 'x' to exit or press Enter to return.\033[0m")
    else:
        while True:
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m\033[94m          RENEWAL TROJAN USER          \033[0m \033[91m┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            print("")
            print("             \033[91m Empty Member\033[0m")
            print("")
            print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress Enter to go back to TROJAN menu or ( Ctrl + X )to exit.\n")
            user_input = input(" \033[93mPress Enter.. \033[0m").strip()
            if user_input.lower() == "":
                print(f"\033[93mExiting the TROJAN renewal process.\033[0m")
                time.sleep(0.5)
                clear_screen()
                back.trojan_menu()
                return
            else:
                print("\033[91m What are you doing? Please enter\033[0m")