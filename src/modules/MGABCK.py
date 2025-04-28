import os
import zipfile
import pyzipper
import time
import json
from datetime import datetime
import subprocess
from getpass import getpass
import importlib
import signal 
from .lolcat import lolcat

def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)
signal.signal(signal.SIGINT, handle_sigint)
def clear_screen():
    os.system("clear")
backgme = importlib.import_module("path.path")
os.makedirs(backgme.backup_dir, exist_ok=True)
os.makedirs(backgme.temp_dir, exist_ok=True)

def get_username():
    if not os.path.exists(backgme.hshdhud2e):
        raise FileNotFoundError(f"\033[91mFile {backgme.hshdhud2e} Not found.\033[0m")
    
    with open(backgme.hshdhud2e, "r") as data_file:
        data = json.load(data_file)
        if "user" in data:
            return data["user"]
        else:
            raise KeyError("'\033[91muser key not found in data!.\033[0m")

def check_rclone_remote():
    m = importlib.import_module("modules.BPCK")
    load = importlib.import_module("modules.RnVuZ3Np.loading")
    printt = importlib.import_module("modules.RnVuZ3Np.prints")
    printt.prints(f"Checking Backup Data Configuration", speed=0.05, color="orange")
    load.loading(2)
    result = subprocess.run("rclone listremotes", shell=True, capture_output=True, text=True)
    remotes = [remote.rstrip(':') for remote in result.stdout.strip().splitlines()]

    if result.returncode != 0 or not remotes:
        print("\033[91m No Configuration Data for Data Backup!.\033[0m")
        printt.prints(f"Return to the Backup menu Select number 5 to configure Mega Backup ", speed=0.05, color="red")
        print(f"\033[93mReturn to Backup menu automatically....\033[0m")
        time.sleep(1)
        m.m_backup()
        return
    
    if len(remotes) == 1:
        lolcat(f"Single Backup Configuration found : {remotes[0]}")
        return remotes[0]
    else:
        while True:
            lolcat("Data Configuration Found!. Please select:\n")
            for i, remote in enumerate(remotes, 1):
                print(f"{i}. {remote}")
            lolcat("\n Press (Ctrl+c). to exit or x Back to menu")
            choice = input(f"\n\033[93mEnter Remote Name Above:\033[0m ").strip()
            if choice in remotes:
                return choice
            elif choice == "x":
                print(" \033[93m Exit data backup\033[0m")
                time.sleep(0.05)
                clear_screen()
                m_backup()
            else:
                print("\033[91mThe remote entered is invalid. Please try again..\033[0m")

def kesalahan():
    m = importlib.import_module("modules.BPCK")
    printt = importlib.import_module("modules.RnVuZ3Np.prints")
    printt.prints(
        "There was an Error While Uploading Backup. It Looks Like Mega.nz Configuration is Invalid\n Please Contact Defloper Or Ask The R01F/GME Community", 
        speed=0.05, 
        color="red"
    )
    while True:
        option = input("\n \033[0m Please Enter\033[0m ")
        if option.strip() == "":
            os.system("clear")
            m.m_backup()
            break
        else:
            print("\033[91mDi enter lah Pepek\033[0m")

def ensure_backup_directory(rclone_remote):
    try:
        load = importlib.import_module("modules.RnVuZ3Np.loading")
        printt = importlib.import_module("modules.RnVuZ3Np.prints")
        clear_screen()

        print(f"\033[92mChecking Subdirectories in\033[0m: \033[91m{rclone_remote}\033[0m")
        check_command = f"rclone lsf {rclone_remote}:backupdatavps"
        result = subprocess.run(check_command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            printt.prints(
                "Subdirectory Not Found, Creating Subdirectory...", 
                speed=0.03, 
                color="orange"
            )
            make_dir_command = f"rclone mkdir {rclone_remote}:backupdatavps"
            mkdir_result = subprocess.run(make_dir_command, shell=True)

            if mkdir_result.returncode == 0:
                print("\033[92mSubdirectory created successfully\033[0m")
            else:
                raise RuntimeError(f"Failed to create subdirectory in {rclone_remote}")
        else:
            print("\033[92mSubdirectory Found\033[0m")
    except RuntimeError as e:
        os.system("clear")
        print(f"\033[91m{str(e)}\033[0m")
        kesalahan()
    except Exception as general_error:
        print(f"\033[91mUnexpected Error: {str(general_error)}\033[0m")
        kesalahan()

def create_backup(rclone_remote):
    m = importlib.import_module("modules.BPCK")
    R01F = importlib.import_module("modules.RnVuZ3Np.runnn")
    isp = R01F.get_isp()
    ruserr = R01F.userrr()
    IipI = R01F.get_local_ip()
    file_path1 = '/etc/xray/domain'
    domain = R01F.get_domain(file_path1)
    region, country, continent = R01F.get_region_and_continent_ipapi()
    wkt = R01F.custom_time_format()
    decrypted_text = R01F.data['decrypted_text']
    expiry = R01F.expiry_date(decrypted_text)
    decrypted = R01F.data['decrypted_text']
    formatted_expiry = R01F.format_expiry_date(decrypted)
    path_data = importlib.import_module("path.path")
    try:
        username = get_username()
    except (FileNotFoundError, KeyError) as e:
        print(f"\033[91mEror: {e}\033[0m")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M")
    backup_name = f"{username}-{timestamp}.zip"
    metadata_name = f"metadata_{timestamp}.json"
    backup_path = os.path.join(backgme.backup_dir, backup_name)
    metadata_path = os.path.join(backgme.backup_dir, metadata_name)

    metadata = {}
    lolcat("Don't be confused when entering/creating an invisible password ｡⁠◕⁠‿⁠◕⁠｡")
    password = getpass(f" \n\033[93mCreate Password For Backup Data Security :\033[0m ").encode()

    for path in path_data.path_data:
        if os.path.exists(path):
            if os.path.isfile(path):
                metadata[path] = os.path.relpath(path, "/")
            elif os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for file in files:
                        full_path = os.path.join(root, file)
                        metadata[full_path] = os.path.relpath(full_path, "/")

    with open(metadata_path, "w") as meta_file:
        json.dump(metadata, meta_file, indent=4)

    try:
        with pyzipper.AESZipFile(backup_path, 'w', compression=zipfile.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as backup_zip:
            backup_zip.setpassword(password)
            for file, rel_path in metadata.items():
                backup_zip.write(file, rel_path)
            backup_zip.write(metadata_path, "metadata.json")
        lolcat(f"Backup successfully Created ｡⁠◕⁠‿⁠◕⁠｡")
    except Exception as e:
        print(f"\033[91mError while creating encrypted ZIP file: {e}\033[0m")
        return

    ensure_backup_directory(rclone_remote)

    lolcat(" \nUploading backup to cloud storage...\n")
    upload_command = f"rclone copy {backup_path} {rclone_remote}:backupdatavps"
    result = subprocess.run(upload_command, shell=True)
    if result.returncode == 0:
        lolcat(f"Backup data successfully uploaded")

        public_link_command = f"rclone link {rclone_remote}:backupdatavps/{backup_name}"
        public_link_result = subprocess.run(public_link_command, shell=True, capture_output=True, text=True)

        if public_link_result.returncode == 0:
            public_link = public_link_result.stdout.strip()
        else:
            print(" \033[91mFailed to get backup link.\033[0m ")
    else:
        print(" \033[91mFailed to upload backup data\033[0m")
    
    while True:
        lolcat("    Save the Data Below Safely\n\n")
        print(f"\033[94m┌━━━━━━━━━━━━━━━━━━━━━━━━━━┐\033[0m")
        print(f" \033[92m Client Name\033[0m : {ruserr} ")
        print(f" \033[92m ISP \033[0m:  {isp}")
        print(f" \033[92m IP VPS \033[0m:  {IipI}")
        print(f" \033[92m Domain \033[0m:  {domain}")
        print(f" \033[92m Region \033[0m:  {region}/{country}/{continent}")
        print(f" \033[92m Time \033[0m:  {wkt}")
        print(f" \033[92m Expired On\033[0m  : {formatted_expiry} ")
        print(f" \033[92m Expired Days\033[0m : {expiry} ")
        print(f" \033[92m Bw Day\033[0m : {R01F.today_bandwidth()} ")
        print(f" \033[92m Bw Mhont\033[0m : {R01F.monthly_bandwidth()}")
        print(f"\033[91m└━━━━━━━━━━━━━━━━━━━━━━━━━━┘ \033[0m")
        print(f"\033[94m┌━━━━━━━━━━━━━━━━━━━━━━━━━━┐\033[0m")
        print(f" Your link : {public_link}")
        print(f" Your Password Restore : {password.decode()}")
        print(f" \033[94mIf a problem occurs, please contact Developer\033[0m")
        print(f"\033[91m└━━━━━━━━━━━━━━━━━━━━━━━━━━┘ \033[0m")
        lolcat(f" 𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\n ")
        print("")
        lolcat(f"   Press [ Ctrl+C ] • To-Exit")
        print("")
        option = input("\n \033[93mPlease Enter to Return to Backup menu\033[0m\n")
        if option == "":
            print(f"\033[93mBack to Backup menu \033[0m")
            time.sleep(0.5)
            clear_screen()
            m.m_backup()
        else:
            print("\033[91m what are you doing Please enter!!\033[0m")
            time.sleep(0.5)
            clear_screen()