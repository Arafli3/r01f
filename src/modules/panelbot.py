import importlib
import os
import signal
from .lolcat import lolcat
import time
from .MNG import R01F_M
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)
signal.signal(signal.SIGINT, handle_sigint)
def info_komunitas():
    jsjsj = importlib.import_module("modules.RnVuZ3Np.lolfig")
    jsjsj.lolfig(" Come on, join")
    print(f"""
    \033[94m┌━━━━━━━━━━━━━━━━━━━━━━━━━━┐\033[0m
    \033[93m|\033[0m \033[92mDonate to Defloper:\033[0m https://saweria.co/R01FGME
    \033[93m|\033[0m \033[92mGrub Telegram Community:\033[0m https://t.me/R01FGMEComunityGrub
    \033[93m|\033[0m \033[92mTelegram Community Channel:\033[0m https://t.me/R01FGMEComunity
    \033[93m|\033[0m \033[92mGitHub :\033[0m https://github.com/GME09
    \033[91m└━━━━━━━━━━━━━━━━━━━━━━━━━━┘ \033[0m"
    """)
    while True:
        option = input(f"\033[93menter/x to back:\033[0m")
        if option == "":
            clear()
            R01F_M()
            return
        elif option == "x":
            print(" \033[91m back to menu\033[0m")
            time.sleep(2)
            clear()
            R01F_M()
            return
        else:
            print("\033[91m What are you doing please input correctly\033[0m")

def clear():
    os.system("clear")
def panelbot():
    printtol = importlib.import_module("modules.RnVuZ3Np.prints")
    jsjsj = importlib.import_module("modules.RnVuZ3Np.lolfig")
    while True:
        jsjsj.lolfig("  Coming Soon")
        lolcat(" English ")
        printtol.prints(f" Let's Support Defloper to Build Interesting Source² code in the Future", speed=0.05, color="orange")
        lolcat(" How to Support ")
        print(f" [ https://saweria.co/R01FGME ]")
        lolcat(" Indonesia ")
        printtol.prints(f" Mari Dukung Defloper untuk Membangun Source² code yang Menarik di Masa Depan", speed=0.05, color="green")
        lolcat(" Cara Mendukung ")
        print(f" [ https://saweria.co/R01FGME ]")
        print("")
        lolcat("     Info Komunitas Input 1    ")
        option = input(f"\033[93mInput Options/x to back:\033[0m")
        if option == "1":
            clear()
            info_komunitas()
            return
        elif option.lower() == "x":
            print(" \033[91m back to menu\033[0m")
            time.sleep(2)
            clear()
            R01F_M()
            return
        else:
            print("\033[91m What are you doing please input correctly\033[0m")
    
    