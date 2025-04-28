import os
import time
import random
from .lolcat import lolcat
import importlib
import signal
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)
    
def system_runn():
    from .STG import seting_menu
    printss = importlib.import_module("modules.RnVuZ3Np.prints")
    from .RTS import check_status, restart
    load = importlib.import_module("modules.RnVuZ3Np.loading")
    os.system("clear")
    printss.prints(f"Please Wait While Retrieving Data Running....", speed=0.05, color="orange")
    load.loading(5)
    os.system("clear")
    print(f"\033[91m╒\033[0m\033[94m⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻\033[0m\033[91m╕\033[0m\033[0m")
    print(f"             \033[91mStatus Running Services          \033[0m")
    print(f"\033[91m╘\033[0m\033[94m⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻⪼⪻\033[0m\033[91m╛\033[0m")
    print(f" \033[91m┌────────────────────────────────────────┐\033[0m")
    for restart1, description in restart.items():
        print(f" \033[94m|\033[0m{check_status(restart1, description)}")
    print(f" \033[91m└────────────────────────────────────────┘\033[0m")
    print(f" \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
    lolcat(f" \nPress enter or [ Ctrl+C ] • To-Exit\n")
    while True:
        option = input(f" \n\033[93mPlease Enter Back To Menu\033[0m")
        if option == "":
            os.system("clear")
            seting_menu()
            return
        else:
            print(f"\033[91mPlease Enter, don't enter anything else!\033[0m")