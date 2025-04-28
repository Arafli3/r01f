import os
import time
import signal
import importlib 
from .lolcat import lolcat
from .AVL import vless_main
from .RVL import RVL_main
from .DAVL import Delete_vless
from .ULVL import vless_data
from .CDLVA import vless_on
from .QUUVL import vless_q
def clear_screen():
    os.system("clear")

def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)

def vless_menu():
    vak = importlib.import_module("modules.VAK")
    while True:
        try:
            clear_screen()
            print(" \033[34m╔─╗\033[0m\033[34m┌────────────────────────────────────────┐\033[0m")
            print(" \033[31m| |\033[0m                V̳L̳E̳S̳S̳ ̳M̳E̳N̳U̳")
            print(" \033[31m| |\033[0m\033[34m└────────────────────────────────────────┘\033[0m")
            print(" \033[31m| |\033[0m [\033[31m01\033[0m] Create a VLESS Account")
            print(" \033[31m| |\033[0m [\033[31m02\033[0m] Renew VLESS Account")
            print(" \033[31m| |\033[0m [\033[31m03\033[0m] Delete VLESS Account")
            print(" \033[31m| |\033[0m [\033[31m04\033[0m] Check VLESS Account Online")
            print(" \033[31m| |\033[0m [\033[31m05\033[0m] View VLESS User Account Data")
            print(" \033[31m| |\033[0m [\033[31m06\033[0m] Check Qouta Usage VLESS User")
            print(" \033[34m╚─╝\033[0m\033[34m└────────────────────────────────────────┘\033[0m")
            print("\n [\033[31m•0\033[0m] \033[31mBACK TO MENU\033[0m")
            lolcat("\n Press Ctrl+c to exit\n")
            print("")

            option = input("\033[93mPlease select an option: \033[0m").strip()
            if option == "1":
                clear_screen()
                vless_main()
                return
            elif option == "2":
                clear_screen()
                RVL_main()
                return
            elif option == "3":
                clear_screen()
                Delete_vless()
                return
            elif option == "4":
                clear_screen()
                vless_on()
                return
            elif option == "5":
                clear_screen()
                vless_data()
                return
            elif option == "6":
                clear_screen()
                vless_q()
                return
            elif option == "0":
                clear_screen()
                vak.vpn_menu()
                return
            else:
                print("\033[91mYou pressed the wrong button, please try again.\033[0m")
                time.sleep(1)
                continue 
        except KeyboardInterrupt:
            pass
            
            break
            