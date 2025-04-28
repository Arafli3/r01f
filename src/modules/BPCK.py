import os
import sys
import time
import signal 
import importlib
from .lolcat import lolcat
from .BOTTEL import bottel
from .MGABCK import create_backup, check_rclone_remote
from .toolsmega import configur_mega, install_latest_rclone, is_rclone_installed
from .WATELL import watell
from .RESTR import restore
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)
signal.signal(signal.SIGINT, handle_sigint)
def clear_screen():
    os.system("clear")
def m_backup():
    bck = importlib.import_module("modules.MNG")
    while True:
        print(f"""
    \033[94m╔─╗\033[0m\033[94m┌────────────────────────────────────────┐\033[0m
    \033[91m| |\033[0m          B̳A̳C̳K̳U̳P̳ ̳&̳ ̳R̳E̳S̳T̳O̳R̳E̳ ̳D̳A̳T̳A̳
    \033[91m| |\033[0m\033[94m└────────────────────────────────────────┘\033[0m
    \033[91m| |\033[0m [\033[91m1\033[0m] Backup Vps Data
    \033[91m| |\033[0m [\033[91m2\033[0m] Bot Tele Optomatis BCKP
    \033[91m| |\033[0m [\033[91m3\033[0m] Bot WA Optomatis BCKP
    \033[91m| |\033[0m [\033[91m4\033[0m] \033[94mRestore VPS Data \033[0m
    \033[91m| |\033[0m [\033[91m5\033[0m] \033[93mAdd Configurasi Mega\033[0m
    \033[91m| |\033[0m
    \033[94m╚─╝\033[0m\033[94m└────────────────────────────────────────┘\033[0m"
        [\033[91m•0\033[0m] \033[91mBACK TO MENU\033[0m
        """)
        lolcat(f" Press [ Ctrl+C ] • To-Exit")
        option = input(f"\n \033[93mInput Option: \033[0m")
        if option == "1":
            clear_screen()
            remote = check_rclone_remote()
            create_backup(remote)
            return
        elif option == "2":
            clear_screen()
            bottel()
            return
        elif option == "3":
            clear_screen()
            watell()
            return
        elif option == "4":
            restore()
            clear_screen()
            return
        elif option == "5":
            clear_screen()
            if not is_rclone_installed():
                print(" \033[91mConfiguration Data seems to be deleted. Performing download\033[0m")
                time.sleep(2)
                clear_screen()
                install_latest_rclone()
            else:
                lolcat(" Getting Mega.nz Configuration")
                time.sleep(2)
                clear_screen()
                configur_mega()
            return
        elif option == "0":
            print(f" \033[91mBACK TO MENU\033[0m")
            time.sleep(0.5)
            clear_screen()
            bck.R01F_M()
            return
        else:
            print(f" \033[91mYou pressed the wrong button, please try again\033[0m")
            clear_screen()