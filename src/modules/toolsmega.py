import os
import subprocess
import platform
import time
import signal
import shutil
import re
from .lolcat import lolcat
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)
signal.signal(signal.SIGINT, handle_sigint)
def clear():
    os.system("clear")
def is_rclone_installed():
    try:
        subprocess.run(["rclone", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except FileNotFoundError:
        return False


def install_latest_rclone():
    from .BPCK import m_backup
    try:
        lolcat("Installing Required Package Data")
        time.sleep(2)
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "curl"], check=True)
        install_script_url = "https://rclone.org/install.sh"
        subprocess.run(["curl", "-O", install_script_url], check=True)
        subprocess.run(["sudo", "bash", "install.sh"], check=True)

        lolcat("Done....")
        time.sleep(2)
        os.remove("install.sh")
        configur_mega()
    except Exception as e:
        print(f"\033[91m Failed to Download Package Data\Please Contact Defloper : {e}\033[0m")
        time.sleep(5)
        m_backup()


def get_rclone_config_path():
    home = os.path.expanduser("~")
    return os.path.join(home, ".config", "rclone", "rclone.conf")


def list_mega_remotes(config_path):
    from configparser import ConfigParser

    parser = ConfigParser()
    parser.read(config_path)

    mega_remotes = [section for section in parser.sections() if parser.get(section, "type", fallback="") == "mega"]

    if mega_remotes:
        lolcat(" \nMega.nz remote list:\n")
        for remote in mega_remotes:
            print(f"        - {remote}")
    else:
        print(" \033[91m There is no mega.nz Remote. Please create a mega.nz Account\033[0m")
    return mega_remotes


def add_or_update_remote(config_path, name, email, password):
    from configparser import ConfigParser
    import base64

    parser = ConfigParser()
    parser.read(config_path)

    encoded_password = base64.b64encode(password.encode("utf-8")).decode("utf-8")
    result = subprocess.run(
            ["rclone", "obscure", password],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
    obfuscated_password = result.stdout.strip()
    if not parser.has_section(name):
        parser.add_section(name)

    parser.set(name, "type", "mega")
    parser.set(name, "user", email)
    parser.set(name, "pass", obfuscated_password)

    with open(config_path, "w") as config_file:
        parser.write(config_file)

    print(f" \033[92mRemote '\033[0m\033[94m{name}\033[0m\033[92m' Successfully added/updated.\033[0m")
    time.sleep(2)
    clear()


def delete_remote(config_path, name):
    from configparser import ConfigParser

    parser = ConfigParser()
    parser.read(config_path)

    if parser.has_section(name):
        parser.remove_section(name)
        with open(config_path, "w") as config_file:
            parser.write(config_file)
        print(f" \033[92mRemote '\033[0m\033[94m{name}\033[92m' Successfully deleted\033[0m.")
        time.sleep(2)
        clear()
    else:
        print(f"\033[91mRemote '\033[0m\033[93m{name}\033[0m\033[91m' Not found \033[0m")
        time.sleep(2)
        clear()


def configur_mega():
    config_path = get_rclone_config_path()
    from .BPCK import m_backup
    clear()

    while True:
        lolcat("\n              Rclone Mega.nz Remote Manager")
        mega_remotes = list_mega_remotes(config_path)

        if not mega_remotes:
            lolcat("                    \nOpsi:")
            print("         \033[93m1.\033[0m \033[94m Add Remote\033[0m")
            print("         \n\033[91m0.\033[0m\033[94m Exit menu\033[0m\n")
            choice = input("\n       \033[93mSelect opsi:\033[0m ").strip()

            if choice == "1":
                lolcat("\n Enter X to Cancel \n")
                name = input("\033[93m Enter Remote Name Mega.nz:\033[0m ").strip()
                if name == "x":
                    print("\033[93m Cancell\033[0m")
                    time.sleep(1)
                    clear()
                    configur_mega()
                email = input("\033[93m Enter Mega.nz Email:\033[0m ").strip()
                if email == "x":
                    print("\033[93m Cancell\033[0m")
                    time.sleep(1)
                    clear()
                    configur_mega()
                password = input("\033[93m Enter Mega.nz Password:\033[0m ").strip()
                if password == "x":
                    print("\033[93m Cancell\033[0m")
                    time.sleep(1)
                    clear()
                    configur_mega()
                add_or_update_remote(config_path, name, email, password)
            elif choice == "2":
                print(" \033[93m Exit To Backup .\033[0m")
                time.sleep(2)
                clear()
                m_backup()
            else:
                print("\033[91mWhat are you doing? Invalid option\033[0m")
        else:
            lolcat("                     \n choose Options:\n")
            print("          \033[93m1.\033[0m \033[94m Add/update Remote\033[0m")
            print("          \033[93m2. \033[0m\033[91mDelete Remote\033[0m")
            print("   \n\033[91m0.\033[0m\033[94m Exit menu\033[0m\n")
            choice = input("\n       \033[93mInput Options :\033[0m ").strip()

            if choice == "1":
                lolcat("\n Enter X to Cancel \n")
                name = input("\033[93m Enter Remote Name Mega.nz:\033[0m ").strip()
                if name == "x":
                    print("\033[93m Cancell\033[0m")
                    time.sleep(1)
                    clear()
                    configur_mega()
                email = input("\033[93m Enter Mega.nz Email:\033[0m ").strip()
                if email == "x":
                    print("\033[93m Cancell\033[0m")
                    time.sleep(1)
                    clear()
                    configur_mega()
                password = input("\033[93m Enter Mega.nz Password:\033[0m ").strip()
                if password == "x":
                    print("\033[93m Cancell\033[0m")
                    time.sleep(1)
                    clear()
                    configur_mega()
                add_or_update_remote(config_path, name, email, password)
            elif choice == "2":
                name = input(" \033[93m Enter the Remote You Want to Delete:\033[0m ").strip()
                if name == "x":
                    print("\033[93m Cancell\033[0m")
                    time.sleep(1)
                    clear()
                    configur_mega()
                delete_remote(config_path, name)
            elif choice == "0":
                print(" \033[93m Exit to backup \033[0m.")
                time.sleep(2)
                clear()
                m_backup()
            else:
                print(" \033[91mWhat are you doing Invalid option. \033[0m")
                time.sleep(2)
                clear()