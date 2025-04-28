import os
import importlib
import time
import signal
from .lolcat import lolcat
from .AVM import vmess_main
from .RVM import RVM_main
from .DLVM import Delete_vmess
from .ULVM import vmess_on
from .DUVM import vmess_data
from .QUVM import vmess_q

def clear_screen():
    os.system("clear")

def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)

def vmess_menu():
    vak = importlib.import_module("modules.VAK")
    while True:
        try:
            clear_screen()
            print(" \033[34m╔─╗\033[0m\033[34m┌────────────────────────────────────────┐\033[0m")
            print(" \033[31m| |\033[0m                V̳M̳E̳S̳S̳ ̳M̳E̳N̳U̳")
            print(" \033[31m| |\033[0m\033[34m└────────────────────────────────────────┘\033[0m")
            print(" \033[31m| |\033[0m [\033[31m01\033[0m] Create a VMESS Account")
            print(" \033[31m| |\033[0m [\033[31m02\033[0m] Renew VMESS Account")
            print(" \033[31m| |\033[0m [\033[31m03\033[0m] Delete VMESS Account")
            print(" \033[31m| |\033[0m [\033[31m04\033[0m] Check VMESS Account Online")
            print(" \033[31m| |\033[0m [\033[31m05\033[0m] View VMESS User Account Data")
            print(" \033[31m| |\033[0m [\033[31m06\033[0m] Check Qouta Usage VMESS User")
            print(" \033[34m╚─╝\033[0m\033[34m└────────────────────────────────────────┘\033[0m")
            print("\n [\033[31m•0\033[0m] \033[31mBACK TO MENU\033[0m")
            lolcat("\n Press Ctrl+c to exit\n")
            print("")

            option = input("\033[93mPlease select an option: \033[0m").strip()

            if option == "1":
                clear_screen()
                vmess_main()
                return
            elif option == "2":
                clear_screen()
                RVM_main()
                return
            elif option == "3":
                clear_screen()
                Delete_vmess()
                return
            elif option == "4":
                clear_screen()
                vmess_on()
                return
            elif option == "5":
                clear_screen()
                vmess_data()
                return
            elif option == "6":
                clear_screen()
                vmess_q()
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