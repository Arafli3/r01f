from .quota import fungsiquota
from .lolcat import lolcat
import importlib
import time
import signal
import os
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)
path = "/etc/qos/xray/trojan.txt"
data_user = fungsiquota(path)
def trojan_q():
    os.system("clear")
    os.system("systemctl restart xray")
    back = importlib.import_module("modules.tt")
    print("\033[34m╔═\033[0m\033[31m─────────────────────────────────────\033[0m\033[34m═╗\033[0m")
    print("\033[31m┃\033[0m \033[1;31;44;1m       Current User Quota Usage      \033[0m\033[31m ┃\033[0m")
    print("\033[34m╚═\033[0m\033[31m─────────────────────────────────────\033[0m\033[34m═╝\033[0m")
    print(f" \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
    for data in data_user:
        limit = data.get("limit")
        status = data.get("status")
        if data["uplink"] is not None:
            print(f"\033[34m»»»»»»»»»»««««««««««\033[0m")
            print(f"\033[93mUser: {data['user']}\033[0m")
            print(f"\033[93mUplink: {data['uplink']}\033[0m")
            print(f"\033[93mDownlink: {data['downlink']}\033[0m")
            print(f"\033[93mTotal: {data['total']}\033[0m")
            print(f"\033[93mlimit: {limit}\033[0m")
            print(f"\033[93mstatus: \033[0m{status}")
            print(f"\033[31m»»»»»»»»»»««««««««««\033[0m")
        else:
            print(f"\033[34m»»»»»»»»»»««««««««««\033[0m")
            print(f" \033[91m Heyyy you don't have a User\033[0m.")
            print(f"\033[31m»»»»»»»»»»««««««««««\033[0m")
    lolcat("\nPress X to go back to TROJAN menu or ( Ctrl + c )to exit.\n")
    while True:
        option = input("\n\033[93mInput Options : \033[0m")
        if option == "x":
            os.system("clear")
            back.trojan_menu()
            return
        elif option == "":
            os.system("clear")
            trojan_q()
            return
        else:
            print("\033[91mPlease enter 'x' to exit or press Enter to return.\033[0m")