import subprocess
import importlib
import time
import signal
import shutil
import uuid
import os
from datetime import datetime, timedelta
from .lolcat import lolcat
def shampo_clear():
    os.system("clear")
def setup_acme(domain):
    try:
        acme_dir = "/root/.acme.sh"
        os.makedirs(acme_dir, exist_ok=True)
        print(f"Directory {acme_dir} created or already exists.")
        
        acme_script = f"{acme_dir}/acme.sh"
        curl_command = f"curl https://acme-install.netlify.app/acme.sh -o {acme_script}"
        subprocess.run(curl_command, shell=True, check=True)
        print(f"Downloaded acme.sh script to {acme_script}.")
        
        subprocess.run(f"chmod +x {acme_script}", shell=True, check=True)
        print(f"Set execute permissions for {acme_script}.")
        
        subprocess.run(f"{acme_script} --upgrade --auto-upgrade", shell=True, check=True)
        print("Upgraded and enabled auto-upgrade for acme.sh.")
        
        subprocess.run(f"{acme_script} --set-default-ca --server letsencrypt", shell=True, check=True)
        print("Set default CA to Let's Encrypt.")
        
        issue_command = f"{acme_script} --issue -d {domain} --standalone -k ec-256"
        subprocess.run(issue_command, shell=True, check=True)
        print(f"Issued certificate for domain {domain}.")
        
        install_cert_command = (
            f"{acme_script} --installcert -d {domain} "
            f"--fullchainpath /etc/xray/xray.crt "
            f"--keypath /etc/xray/xray.key --ecc"
        )
        subprocess.run(install_cert_command, shell=True, check=True)
        print(f"Installed certificate for domain {domain}.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def get_domain(file_path):
    try:
        with open(file_path, 'r') as file:
            domain = file.read().strip()
        return domain
    except FileNotFoundError:
        return "\033[91mFile Not Found\033[0m"
    except Exception as e:
        return f"\033[91mEror: {e}\033[0m"

def configure_ssl(domain):
    try:
        subprocess.run(["systemctl", "stop", "nginx"], check=True)

        subprocess.run(
            ["/root/.acme.sh/acme.sh", "--issue", "-d", domain, "--standalone", "-k", "ec-256"],
            check=True
        )

        subprocess.run(
            [
                "/root/.acme.sh/acme.sh", "--installcert", "-d", domain,
                "--fullchainpath", "/etc/xray/xray.crt", "--keypath", "/etc/xray/xray.key", "--ecc"
            ],
            check=True
        )
        print(f"[INFO] \033[92mSSL certificate successfully installed for domain: {domain}\033[0m")

    except subprocess.CalledProcessError as e:
        print("\033[91m[ERROR] An error occurred while installing SSL.\033[0m")
        if "No A record" in str(e.output) or "No TXT record" in str(e.output):
            print(f"\033[91m[ERROR] The domain {domain} is not yet associated with this server.\033[0m")
        elif e.returncode == 2:
            print(f"\033[91m[ERROR] SSL validation for domain {domain} failed. Check DNS settings..\033[0m")
        else:
            print(f"\033[91m[ERROR] Unknown \033[0m: {e}")

    finally:
        subprocess.run(["systemctl", "start", "nginx"], check=False)
        
def main():
    back = importlib.import_module("modules.DMMU")
    file_path = '/etc/xray/domain'
    domain = get_domain(file_path)
    setup_acme(file_path)
    configure_ssl(domain)
    time.sleep(2)
    shampo_clear()
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
    lolcat(" Installation of SSL certificate is complete")
    while True:
        inp = input(" \033[93mPlease Enter...\033[0m")
        if inp == "":
            back.domain_m()
            shampo_clear()
            return
        else:
            print("\033[91m What you do please enter\033[0m")