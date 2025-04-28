import os
import time
import signal
import os
import time
import importlib
from .AS import create_ssh
from .RNSH import list_ssh_members
from .HS import list_users
from .STSH import statussUserSSH
from .DAS import logdatassh
from .lolcat import lolcat
from .limitssh import sshlimit
def clear_screen():
    os.system("clear")

def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)

def ssh_menu():
    vak = importlib.import_module("modules.VAK")
    while True:
        clear_screen()
        print(" \033[34m╔─╗\033[0m\033[34m┌────────────────────────────────────────┐\033[0m")
        print(" \033[31m| |\033[0m                S̳S̳H̳ ̳M̳E̳N̳U̳")
        print(" \033[31m| |\033[0m\033[34m└────────────────────────────────────────┘\033[0m")
        print(" \033[31m| |\033[0m [\033[31m01\033[0m] Create an SSH Account")
        print(" \033[31m| |\033[0m [\033[31m02\033[0m] Renew SSH Account")
        print(" \033[31m| |\033[0m [\033[31m03\033[0m] Delete SSH Account")
        print(" \033[31m| |\033[0m [\033[31m04\033[0m] Check SSH Account Status")
        print(" \033[31m| |\033[0m [\033[31m05\033[0m] View SSH User Account Data")
        print(" \033[31m| |\033[0m [\033[31m06\033[0m] Menu banned User SSH")
        print(" \033[31m| |\033[0m [\033[31m07\033[0m] SSH Banners")
        print(" \033[34m╚─╝\033[0m\033[34m└────────────────────────────────────────┘\033[0m")
        print("\n [\033[31m•0\033[0m] \033[31mBACK TO MENU\033[0m")
        lolcat("\n Press Ctrl+c to exit\n")
        print("")
        option = input(" \033[93mPlease select an option:\033[0m ").strip()

        if option == "1":
            clear_screen()
            create_ssh()
            return
        elif option == "2":
            clear_screen()
            list_ssh_members()
            return
        elif option == "3":
            clear_screen()
            list_users()
            return
        elif option == "4":
            clear_screen()
            statussUserSSH()
            return
        elif option == "5":
            clear_screen()
            logdatassh()
            return
        elif option == "6":
            clear_screen()
            sshlimit()
            return
        elif option == "7":
            clear_screen()
            os.system("nano /etc/WhoamI.net")
            return
        elif option == "0":
            clear_screen()
            vak.vpn_menu()
            return
        else:
            print("\033[91mYou pressed the wrong button, please try again.\033[0m")
            time.sleep(1)
            continue 
            
        break