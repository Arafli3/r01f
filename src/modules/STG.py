import os
import sys
import time
import signal 
from .lolcat import lolcat
from .RTS import restart_services, restart
from .RNNG import system_runn
from .DMMU import domain_m
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)
def clear_screen():
    os.system("clear")
    
def seting_menu():
    from .MNG import R01F_M
    while True:
        print(f"""
    \033[94m╔─╗\033[0m\033[94m┌────────────────────────────────────────┐\033[0m
    \033[91m| |\033[0m              S̳E̳T̳T̳I̳N̳G̳S̳ ̳M̳E̳N̳U̳ 
    \033[91m| |\033[0m\033[94m└────────────────────────────────────────┘\033[0m
    \033[91m| |\033[0m [\033[91m01\033[0m] RESTART SYSTEM
    \033[91m| |\033[0m [\033[91m02\033[0m] RUNNING SYSTEM
    \033[91m| |\033[0m [\033[91m03\033[0m] DOMAIN MENU
    \033[91m| |\033[0m [\033[91m04\033[0m] DNS MENU
    \033[91m| |\033[0m [\033[91m05\033[0m] TETS SPEED MENU
    \033[91m| |\033[0m [\033[91m06\033[0m] TCP BBR MENU
    \033[91m| |\033[0m [\033[91m07\033[0m] BUG PROXY HUNTER
    \033[94m╚─╝\033[0m\033[94m└────────────────────────────────────────┘\033[0m
    
    [\033[91m•0\033[0m] \033[91mBACK TO MENU\033[0m
        """)
        lolcat(f" Press [ Ctrl+C ] • To-Exit")
        option = input(f"\n \033[93mInput Option: \033[0m")
        if option == "1":
            clear_screen()
            restart_services(restart)
            return
        elif option == "2":
            clear_screen()
            system_runn()
            return
        elif option == "3":
            clear_screen()
            domain_m()
            return
            pass
        elif option == "4":
            clear_screen()
            return
            pass
        elif option == "5":
            clear_screen()
            return
            pass
        elif option == "6":
            clear_screen()
            return
            pass
        elif option == "7":
            clear_screen()
            return
            pass
        elif option == "8":
            clear_screen()
            return
            pass
        elif option == "0":
            clear_screen()
            R01F_M()
            return
        else:
            print(f" \033[91mYou pressed the wrong button, please try again\033[0m")