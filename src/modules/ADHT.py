import os
import time
import importlib
from .lolcat import lolcat
def clear():
    os.system("clear")
path = "/var/lib/Gmehost/ipvps.conf"
def change_domain(filename):
    from .DMMU import domain_m
    pathfil = '/etc/xray/domain'
    try:
        if not os.path.exists(filename):
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'w') as file:
                file.write("IP=\n")

        with open(filename, 'r') as file:
            lines = file.readlines()
            
        while True:
            new_domain = input(" \033[93m Enter New Domain\033[0m: ")
            if new_domain == "x":
                print(" \033[93mBack To Menu\033[0m")
                time.sleep(2)
                clear()
                domain_m()
            elif new_domain == "":
                print("\033[91m Please enter domain or exit\033[0m")
            else:
                break
        
        updated_lines = []
        for line in lines:
            if line.startswith("IP="):
                updated_line = f"IP={new_domain}\n"
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line)
                
        with open(filename, 'w') as file:
            file.writelines(updated_lines)
        with open(pathfil, 'w') as f:
            f.write(new_domain)
        
        print(f"\033[92mDomain Successfully Changed To {new_domain}\033[0m")
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
    menull()


def menull():
    clear()
    R01F = importlib.import_module("modules.RnVuZ3Np.runnn")
    path1 = '/etc/xray/domain'
    domain = R01F.get_domain(path1)
    isp = R01F.get_isp()
    ip = R01F.get_local_ip()
    path = "/var/lib/Gmehost/ipvps.conf"
    print(f"""
    \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m
    \033[91m┃\033[0m \033[91m         Change Your Domain          \033[0m\033[91m ┃\033[0m
    \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m
    \033[94m┌────────────────────────────────────────────┐\033[0m
    \033[93mYour Current Domain :\033[0m {domain}
    \033[93mIP                  :\033[0m {ip}
    \033[93mISP                 : \033[0m{isp}
    \033[91m└────────────────────────────────────────────┘\033[0m 
    """)
    lolcat("  Type x to cancel and return to the Domain menu\n")
    change_domain(path)
    