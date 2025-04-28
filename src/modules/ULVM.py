import re
import os
from datetime import datetime, timedelta
from .lolcat import lolcat
import importlib
import time
import signal
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)
def clear_screen():
    os.system("clear")
def waktu(teks):
    pola = r"\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}"
    return re.match(pola, teks) is not None
signal.signal(signal.SIGINT, handle_sigint)
def gmer01fuser():
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

def connect(user):
    hasillog = []
    pathfile = "/var/log/xray/access.log"
    if not os.path.exists(pathfile):
        print(f"\033[91mError :{pathfile} \033[0m")
        return hasillog
    with open(pathfile, 'r') as file:
        for line in file:
            if any(nama in line for nama in user):
                baris = line.split()
                bagian = " ".join([baris[0], baris[1]])
                if waktu(bagian):
                    sekarang = datetime.now()
                    cek = datetime.strptime(bagian, "%Y/%m/%d %H:%M:%S")
                    wakterten = sekarang - timedelta(seconds=50)
                    if cek >= wakterten and cek < sekarang:
                        hasillog.append(line.strip())
                else:
                    return "\033[91m Format not Falid\033[0m"
    return hasillog

def vmess_on():
    os.system("clear")
    back = importlib.import_module("modules.vevek")
    users_check = gmer01fuser()
    if not users_check:
        while True:
            print("\033[34m╔═─────────────────────────────────────═╗\033[0m")
            print("\033[31m┃\033[0m \033[1;31;44;1m          VMESS ONLINE USER          \033[0m\033[31m ┃\033[0m")
            print("\033[34m╚═─────────────────────────────────────═╝\033[0m")
            print("")
            print("             \033[91m Empty Member\033[0m")
            print("")
            print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            lolcat("\nPress Enter to go back to VMESS menu or ( Ctrl + X )to exit.\n")
            user_input = input(" \033[93mPress Enter.. \033[0m").strip()
            if user_input.lower() == "":
                print(f"\033[93mExiting the VMESS User Online process.\033[0m")
                time.sleep(0.5)
                back.vmess_menu()
                return
            else:
                print("\033[91m What are you doing ?\033[0m")
                time.sleep(0.5)
                clear_screen()
    else:
        gmelog = connect(users_check)
        if gmelog:
            print("\033[34m╔═─────────────────────────────────────═╗\033[0m")
            print("\033[31m┃\033[0m \033[1;31;44;1m          VMESS ONLINE USER          \033[0m\033[31m ┃\033[0m")
            print("\033[34m╚═─────────────────────────────────────═╝\033[0m")
            print(f" \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            print("\033[34m┌────────────────────────────────────────────┐\033[0m")
            hasil = {}
            hasil1 = [f"{lines.split()[-1]} {lines.split()[2]}" for lines in gmelog]
            for line in hasil1:
                lines = line.split()
                ip = lines[-1].replace("tcp", " ").replace(":0", " ").replace("udp:", " ").replace(":", " ").strip()
                user = lines[0]
                if user not in hasil:
                    hasil[user] = set()
                hasil[user].add(ip)
            for user, ip, in hasil.items():
                print("       \033[31m-------------------------------\033[0m")
                print(f"           USER     : \033[32;1m{user}\033[0m")
                print(f"           Total IP : \033[31;1m{len(ip)}\033[0m")
                for ips in ip:
                    print(f"               IP   : \033[36;1m{ips}\033[0m")
                print("       \033[31m-------------------------------\033[0m")
            print("\033[34m└────────────────────────────────────────────┘\033[0m")
            print("")
            lolcat("\n Press Enter to return to User Online account or type 'x' to exit...\n")
            while True:
                action = input(" \033[93mInput Options:\033[0m ").strip().lower()
                if action == "x":
                    print(f"\033[93mExiting the VMESS User Online process.\033[0m")
                    time.sleep(0.5)
                    os.system("clear")
                    back.vmess_menu()
                    return
                elif action == "":
                    os.system("clear")
                    vmess_on()
                    return
                else:
                    print("\033[91mPlease enter 'x' to exit or press Enter to return.\033[0m")
        else:
            while True:
                print("\033[34m╔═─────────────────────────────────────═╗\033[0m")
                print("\033[31m┃\033[0m \033[1;31;44;1m          VMESS ONLINE USER          \033[0m\033[31m ┃\033[0m")
                print("\033[34m╚═─────────────────────────────────────═╝\033[0m")
                print("")
                print("             \033[91m Empty Member\033[0m")
                print("")
                print(f"      \033[94m━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
                print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
                lolcat("\n Input X to go back to VMESS menu or ( Ctrl + X )to exit.\n")
                user_input = input(" \033[93mInput Options : \033[0m").strip()
                if user_input.lower() == "":
                    vmess_on()
                    return
                elif user_input.lower() == "x":
                    print(f"\033[93mExiting the VMESS User Online process.\033[0m")
                    time.sleep(0.5)
                    os.system("clear")
                    back.vmess_menu()
                else:
                    print("\033[91m What are you doing ?\033[0m")
                    time.sleep(0.5)
                    clear_screen()