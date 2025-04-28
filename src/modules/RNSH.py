import os
import re
import importlib
import subprocess
from datetime import datetime, timedelta
import time
import signal
from .lolcat import lolcat
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)
def clear():
    os.system("clear")
def run_command(command):
    result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.strip(), result.stderr.strip()

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")
def selisihhari(tglxp):
    try:
        hari = datetime.now()
        data_exp = datetime.strptime(tglxp, "%Y-%m-%d:%H")
        delta = data_exp - hari
        return delta.days, data_exp.hour
    except ValueError:
        return none,
        
def masaaktif12(username, tambahan_hari):
    exp_date_str = subprocess.getoutput(f"chage -l {username} | grep 'Account expires' | awk -F': ' '{{print $2}}'")

    if "never" in exp_date_str or exp_date_str.strip() == "":
        current_exp_date = datetime.now()
    else:
        try:
            current_exp_date = datetime.strptime(exp_date_str.strip(), "%b %d, %Y")
        except ValueError:
            return(" \033[91mUnrecognized Format \n Please Contact Defloper / community\033[0m")
            return
    new_exp_date = current_exp_date + timedelta(days=tambahan_hari)
    new_exp_date_str = new_exp_date.strftime("%Y-%m-%d")
    subprocess.run(["chage", "-E", new_exp_date_str, username])

    return(f" \033[92mSsh Active Period {username} Extended to {new_exp_date_str}\033[0m")

def list_ssh_members():
    back = importlib.import_module("modules.mmxsh")
    path1 = '/etc/qos/ssh/sshadmin.txt'
    gmelist = []
    with open(path1, 'r') as f:
        a = f.readlines()
        for b in a:
            if b.startswith('###'):
                gmelist.append(b)
    if gmelist:
        exittol = False
        while not exittol:
            clear()
            print_colored("╔══════════════════════════════════════════╗", "34")
            print_colored("┃            SSH Member List               ┃", "31")
            print_colored("╚══════════════════════════════════════════╝", "34")
            lolcat(f"  \033[93m{'No.':<5}{'User':<13}{'Expired':<15}{'Status':<20}\033[0m")
            print(f"  \n\033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

            for idx, line in enumerate(gmelist, 1):
                nama_user = line.split()[1]
                try:
                    expdatastring = line.split()[2]
                    data_exp = datetime.strptime(expdatastring, "%Y-%m-%d:%H")
                    hariini = datetime.now()
                    exp_time = data_exp - hariini
                    exp_days = exp_time.days
                    exp_format = data_exp.strftime("%Y-%m-%d:%H")
                    exp_hour = data_exp.strftime("%H:%M")
                    if exp_days > 0:
                        status = f"\033[93m{exp_days}\033[0m \033[92manother day\033[0m"
                    elif exp_days == 0:
                        status = f"\033[92mExpired Today at \033[0m\033[91m{exp_hour} \033[0m\033[92mo'clock\033[0m"
                    else:
                        status = f"\033[91m{abs(exp_days)} Expired\033[0m"
                    print(f"  \033[93m{idx:<5}{nama_user:<13}{exp_format:<15}\033[0m{status:<20}")
                except (IndexError, ValueError):
                    print(f"  \033[91m{idx:<5}{nama_user:<13}{'N/A':<15}{'Invalid Date':<20}\033[0m")

            print(f" \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress 'X' to go back to SSH menu or (Ctrl + X) to exit.\n")
            listnum = input("\033[93mEnter the user number to renew (or 'x' to exit):\033[0m ").strip()
            if listnum.lower() == 'x':
                print(" \033[93mExiting renewal process.\033[0m")
                time.sleep(0.5)
                back.ssh_menu()
                clear()
                break
            elif listnum.isdigit() and 1 <= int(listnum) <= len(gmelist):
                selected_user = gmelist[int(listnum) - 1].strip()
                nama_user = selected_user.split()[1]
                expiration_date_str = selected_user.split()[2]
                print("     \033[34m#############-\033[0m")
                print("     \033[31m-------------------------------\033[0m")
                print(f"  \033[94mSelected User Details:\033[0m")
                print(f"  \033[93mUsername  : {nama_user}\033[0m")
                print(f"  \033[93mExpiration: {exp_format}\033[0m")
                print("     \033[34m-------------------------------\033[0m")
                print("     \033[31m##############-\033[0m")
                while True:
                    confirm = input(f" \033[93mConfirm renew for user '{nama_user}'? (y/n):\033[0m ").strip().lower()
                    if confirm == 'y':
                        print(f" \033[92mRenewing account for user '{nama_user}'...\033[0m")
                        exittol = True
                        break
                    elif confirm == 'n':
                        print(f" \033[92m Back To Ssh Renewal\033[0m")
                        time.sleep(0.5)
                        clear()
                        back.ssh_menu()
                        return
                    else:
                        print("\033[91m Please select Y/N \033[0m")
                while True:
                    lolcat("\nPress 'X' to go back to SSH menu/cancel or (Ctrl + X) to exit.\n")
                    lolcat(" \nAdd Active Period\n")
                    try:
                        masaaktif = input(" \033[93m Input duration (Day): \033[0m").strip()
                        if masaaktif == "x":
                            print(" \033[93mExiting the SSH renewal process.\033[0m")
                            time.sleep(0.5)
                            back.ssh_menu()
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
        memk = 'mkejjs'
        with open(path1, "r") as file:
            baris = file.readlines()
        updated1lines = []
        masaaktif = int(masaaktif)
        updatexp = ""
        user_found = False
        for line in baris:
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
        with open(path1, "w") as file:
            file.writelines(updated1lines)
        if user_found:
            print(f"Masa aktif untuk pengguna '{nama_user}' telah diperbarui.")
        else:
            print(f"Pengguna '{nama_user}' tidak ditemukan dalam file.")
        masaaktif12(nama_user, masaaktif)
        print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
        print(f" \033[91m┃\033[0m \033[94m      Renewal Account  Succesfully   \033[0m\033[91m ┃\033[0m")
        print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
        print("")
        print(f" \033[94m#########\033[0m\033[93m SSH Account \033[0m\033[91m#########\033[0m")
        print(f" \033[94m┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐\033[0m")
        print(f" \033[93mClient Name : \033[0m\033[92m{nama_user}\033[0m")
        print(f" \033[93mExpired On :\033[0m\033[92m {updatexp}\033[0m")
        print(f" \033[93mAdd active period On :\033[0m\033[92m {masaaktif}\033[0m")
        print( "")
        print(f" \033[94m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘\033[0m")
        print(f" \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
        lolcat("\n Press Enter to return to renewal account or type 'x' to exit...\n")
        while True:
            action = input(" \033[93mInput Options:\033[0m ").strip().lower()
            if action == "x":
                print(f"\033[93mExiting the SSH renewal process.\033[0m")
                time.sleep(0.5)
                os.system("clear")
                back.ssh_menu()
                return
            elif action == "":
                os.system("clear")
                list_ssh_members()
                return
            else:
                print("\033[91mPlease enter 'x' to exit or press Enter to return.\033[0m")
    else:
        while True:
            print_colored("╔══════════════════════════════════════════╗", "34")
            print_colored("┃            SSH Member List               ┃", "31")
            print_colored("╚══════════════════════════════════════════╝", "34")
            print("")
            print("             \033[91m Empty Member\033[0m")
            print("")
            print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress Enter to go back to SSH menu or ( Ctrl + X )to exit.\n")
            user_input = input(" \033[93mPress Enter.. \033[0m").strip()
            if user_input.lower() == "":
                print(f"\033[93mExiting the SSH renewal process.\033[0m")
                time.sleep(0.5)
                clear()
                back.ssh_menu()
                return
            else:
                print("\033[91m What are you doing? Please enter\033[0m")