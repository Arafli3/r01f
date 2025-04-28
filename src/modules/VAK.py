import os
import sys
import time
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from .mmxsh import ssh_menu
from .vevek import vmess_menu
from .vvx import vless_menu
from .tt import trojan_menu
from .lolcat import lolcat
from .MNG import R01F_M
from .limitxray import xraylimit
import signal 
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)

def clear_screen():
    os.system("clear")

def vpn_menu():
    while True:
        try:
            clear_screen()
            print(" \033[34m╔─╗\033[0m\033[34m┌────────────────────────────────────────┐\033[0m")
            print(" \033[31m| |\033[0m                V̳P̳N̳ ̳M̳E̳N̳U̳")
            print(" \033[31m| |\033[34m└────────────────────────────────────────┘\033[0m")
            print(" \033[31m| |\033[0m [\033[31m1\033[0m] Menu SSH")
            print(" \033[31m| |\033[0m [\033[31m2\033[0m] Menu Vmess")
            print(" \033[31m| |\033[0m [\033[31m3\033[0m] Menu Vless")
            print(" \033[31m| |\033[0m [\033[31m4\033[0m] Menu Trojan")
            print(" \033[31m| |\033[0m [\033[91m5\033[0m] Xray Limit")
            print(" \033[34m╚─╝\033[0m\033[34m└────────────────────────────────────────┘\033[0m")
            print("")
            print("\n [\033[31m•0\033[0m] \033[31mBACK TO MENU\033[0m")
            lolcat("\n Press Ctrl+c to exit\n")
            print("")
            option = input(" \033[93mPlease select an option:\033[0m ").strip()
            if option == "1":
                clear_screen()
                ssh_menu()
                return
            elif option == "2":
                clear_screen()
                vmess_menu()
                return
            elif option == "3":
                clear_screen()
                vless_menu()
                return
            elif option == "4":
                clear_screen()
                trojan_menu()
                return
            elif option == "5":
                clear_screen()
                xraylimit()
                return
            elif option == "0":
                clear_screen()
                R01F_M()
                return
            else:
                print("\033[91mYou pressed the wrong button, please try again.\033[0m")
                time.sleep(1)
        except KeyboardInterrupt:
            pass
            
            break
            
        
