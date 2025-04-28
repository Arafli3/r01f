import os
import time
import random
from .lolcat import lolcat
import importlib
import signal
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)
ORANGE = "\033[38;5;214m"
RESET = "\033[0m"
restart = {
    "ssh": "SSH System",
    "cron": "Cron System",
    "xray": "XRAY system",
    "xray.service": "XRAY 2 System",
    "nginx": "Nginx System",
    "apache2": "Apache2",
    "R01F-CORE": "Limit Qouta",
    "stunnel4": "Stunnel System",
    "dropbear": "Dropbear System",
    "ws-stunnel.service": "Ws Stunnel System",
    "ws-dropbear.service": "Ws Dropbear System",
    "udp-custom": "Udp system",
    "userxp.service": "Auto User xrayexp",
    "sshxp.service": "Auto User sshexp",
}
def restart_services(services):
    printss = importlib.import_module("modules.RnVuZ3Np.prints")
    total_services = len(services)
    total_estimated_time = total_services * random.randint(3, 6) 
    lolcat(f"  Starting to restart {total_services} services...")
    print(f"  \033[93mEstimated total time: {total_estimated_time} seconds\033[0m\n")
    
    for idx, (service, description) in enumerate(services.items(), start=1):
        print(f" \033[94m[\033[0m\033[93m{idx}/{total_services}\033[0m\033[91m] \033[0m\033[92mRestarting\033[0m \033[94m({description})...\033[0m")
        estimated_time = random.randint(3, 6)
        print(f" \033[93mEstimated time for this service:\033[0m\033[91m {estimated_time}\033[0m \033[93mseconds\033[0m")
        loading_animation(estimated_time)
        os.system(f"sudo systemctl restart {service}")
        
        print(f" \033[93mService\033[92m ({description})\033[0m \033[93mrestarted successfully\033[0m\033[91m!\033[0m\n")
    os.system(f"screen -dmS badvpn badvpn-udpgw --listen-addr 127.0.0.1:7300 --max-clients 500")
    print(f" \033[93mService\033[92m Badvpn\033[0m \033[93mrestarted successfully\033[0m\033[91m!\033[0m\n")
    lolcat(" \nAll services have been restarted successfully!\n")
    time.sleep(1)
    os.system("clear")
    printss.prints(f"Please Wait While Retrieving Data Running....", speed=0.05, color="orange")
    loading_animation(5)
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
        option = input(f" \n\033[93mPlease Enter Back to menu\033[0m")
        if option == "":
            os.system("clear")
            seting_menu()
            return
        else:
            print(f"\033[91mPlease Enter, don't enter anything else!\033[0m")
            
def loading_animation(duration):
    animation = "|/-\\"
    start_time = time.time()
    while time.time() - start_time < duration:
        for frame in animation:
            print(f"\r\033[93m Please Wait It takes some time...\033[0m {frame}", end="", flush=True)
            time.sleep(0.1)
    lolcat("\rDone!           ")

import subprocess

def check_status(name, description):
    try:
        result = subprocess.run(
            ["systemctl", "is-active", name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stdout.strip() == "active":
            return f"\033[93m{description}: \033[0m\033[92mON/RUNNING\033[0m"
        else:
            error_message = result.stderr.strip() or f"\033[91m{description} is not running\033[0m"
            return f"\033[93m{description}:\033[0m \033[91mOFF - {error_message}\033[0m"
    
    except Exception as e:
        return f"\033[91mError checking {description}: {e}\033[0m"