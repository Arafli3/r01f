import os
import subprocess
import zipfile
import json
import shutil
import pyzipper
import re
import time
from .lolcat import lolcat
import importlib
def clear():
    os.system("clear")

inilink = re.compile(
    r'^(https?://)?'
    r'([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})'
    r'(:\d+)?(/.*)?$'
)
restore_directory = "/root"
def zipfile(direktori):
    for file in os.listdir(direktori):
        if file.endswith(".zip"):
            zip_filepath = os.path.join(direktori, file)
            print("｡⁠◕⁠‿⁠◕⁠｡")
            os.remove(zip_filepath)
            return
    print("⊙⁠.⁠☉")
def megachan(url, output_dir):
    bck = importlib.import_module("modules.BPCK")
    printt = importlib.import_module("modules.RnVuZ3Np.prints")
    load = importlib.import_module("modules.RnVuZ3Np.loading")
    try:
        subprocess.run(
            ["megadl", "--path", output_dir, url],
            check=True
        )
        print(" \033[92msuccessful download backup file \03[0m")
    except subprocess.CalledProcessError as e:
        os.system("rm -r /root/extracted")
        zipfile(restore_directory)
        clear()
        print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
        print(f" \033[91m┃\033[0m \033[94m               Restore               \033[0m\033[91m ┃\033[0m")
        print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
        print("")
        print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
        print("\033[91m Error: please contact developer or community 46 \033[0m.")
        printt.prints(f" Failed to Extract file : Format Not Supported", speed=0.04, color="red")
        print("")
        print(" \033[94m─────────────────────────────────────\033[0m")
        while True:
            inputtop = input(" \033[91mError Please Enter....\033[0m")
            if inputtop == "":
                os.system("clear")
                time.sleep(0.5)
                bck.m_backup()
                return
            else:
                print(f"Why are you entering input {inputtop}?, please ")

def ext(file_path, extracttt, password):
    bck = importlib.import_module("modules.BPCK")
    printt = importlib.import_module("modules.RnVuZ3Np.prints")
    load = importlib.import_module("modules.RnVuZ3Np.loading")
    try:
        with pyzipper.AESZipFile(file_path) as zip_ref:
            zip_ref.pwd = password.encode()
            zip_ref.extractall(extracttt)
        print(f"\033[92m File successfully extracted \033[0m")
    except RuntimeError as e:
        if "Bad password" in str(e):
            os.system("rm -r /root/extracted")
            zipfile(restore_directory)
            clear()
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m \033[94m               Restore               \033[0m\033[91m ┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            print("")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            print("\033[91m Error: please contact developer or community 79 \033[0m.")
            printt.prints(f" Wrong Password!", speed=0.04, color="red")
            print("")
            print(" \033[94m─────────────────────────────────────\033[0m")
            while True:
                inputtop = input(" \033[91mError Please Enter....\033[0m")
                if inputtop == "":
                    os.system("clear")
                    time.sleep(0.5)
                    bck.m_backup()
                    return
                else:
                    print(f"\033[91mWhy are you entering input {inputtop}?, please \033[0m")
        else:
            os.system("rm -r /root/extracted")
            zipfile(restore_directory)
            clear()
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m \033[94m               Restore               \033[0m\033[91m ┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            print("")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            print("\033[91m Error: please contact developer or community 101 \033[0m.")
            printt.prints(f" Failed to Extract file", speed=0.04, color="red")
            print("")
            print(" \033[94m─────────────────────────────────────\033[0m")
            while True:
                inputtop = input(" \033[91mError Please Enter....\033[0m")
                if inputtop == "":
                    os.system("clear")
                    time.sleep(0.5)
                    bck.m_backup()
                    return
                else:
                    print(f"\033[91mWhy are you entering input {inputtop}?, please \033[0m")
    except NotImplementedError as e:
        os.system("rm -r /root/extracted")
        zipfile(restore_directory)
        clear()
        print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
        print(f" \033[91m┃\033[0m \033[94m               Restore               \033[0m\033[91m ┃\033[0m")
        print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
        print("")
        print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
        print("\033[91m Error: please contact developer or community 123 \033[0m.")
        printt.prints(f" Failed to Extract file : Format Not Supported", speed=0.04, color="red")
        print("")
        print(" \033[94m─────────────────────────────────────\033[0m")
        while True:
            inputtop = input(" \033[91mError Please Enter....\033[0m")
            if inputtop == "":
                os.system("clear")
                time.sleep(0.5)
                bck.m_backup()
                return
            else:
                print(f"\033[91mWhy are you entering input {inputtop}?, please \033[0m")
def koplakakajs(extract_dir):
    metadata_path = os.path.join(extract_dir, "metadata.json")
    if not os.path.exists(metadata_path):
            os.system("rm -r /root/extracted")
            zipfile(restore_directory)
            clear()
            print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
            print(f" \033[91m┃\033[0m \033[94m               Restore               \033[0m\033[91m ┃\033[0m")
            print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
            print("")
            print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
            print("\033[91m Error: please contact developer or community 147 \033[0m.")
            printt.prints(f" Metadata Looks like it's missing or you entered the wrong download link!", speed=0.04, color="red")
            print("")
            print(" \033[94m─────────────────────────────────────\033[0m")
            while True:
                inputtop = input(" \033[91mError Please Enter....\033[0m")
                if inputtop == "":
                    os.system("clear")
                    time.sleep(0.5)
                    bck.m_backup()
                    return
                else:
                    print(f"\033[91mWhy are you entering input {inputtop}?, please \033[0m")
    print(" \033[92mReading Meta Data...\033[0m")
    with open(metadata_path, "r") as f:
        metadata = json.load(f)
    for original_path, backup_path in metadata.items():
        source_path = os.path.join(extract_dir, backup_path)
        if not os.path.exists(source_path):
            print(f" \033[91mSource File does not exist, No Problem \033[0m")
            continue
        os.makedirs(os.path.dirname(original_path), exist_ok=True)
        shutil.move(source_path, original_path)
        print(f" \033[92m Recover Files\033[0m")
def restore():
    try:
        nama_paket = "megatools"
        subprocess.run(['dpkg', '-s', nama_paket], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Paket {nama_paket} sudah terinstall.")
    except subprocess.CalledProcessError:
        print(f"Paket {nama_paket} belum terinstall. Melakukan instalasi...")
        try:
            # Install paket menggunakan apt
            subprocess.run(['sudo', 'apt-get', 'install', '-y', nama_paket], check=True)
            print(f"Paket {nama_paket} berhasil diinstall.")
        except subprocess.CalledProcessError as e:
            print(f"Gagal menginstall paket {nama_paket}. Error: {e}")
    clear()
    bck = importlib.import_module("modules.BPCK")
    printt = importlib.import_module("modules.RnVuZ3Np.prints")
    load = importlib.import_module("modules.RnVuZ3Np.loading")
    print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
    print(f" \033[91m┃\033[0m \033[94m               Restore               \033[0m\033[91m ┃\033[0m")
    print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
    print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
    lolcat(" Enter X to return or Ctrl+c to exit")
    print("")
    while True:
        megalink = input(" \033[93m Enter Mega.nz backup :\033[0m ").strip()
        if megalink.lower() == "x":
            os.system("clear")
            time.sleep(0.5)
            bck.m_backup()
            return
        if inilink.match(megalink):
            break
        else:
            print(f" \033[91m Please enter the Backup link correctly\033[0m")
    zip_password = input(" \033[93m input Your Password :\033[0m ").strip()
    if not os.path.exists(restore_directory):
        os.makedirs(restore_directory)
    megachan(megalink, restore_directory)
    downloaded_files = [
        f for f in os.listdir(restore_directory)
        if f.endswith(".zip")
    ]
    if not downloaded_files:
        os.system("rm -r /root/extracted")
        zipfile(restore_directory)
        clear()
        print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
        print(f" \033[91m┃\033[0m \033[94m               Restore               \033[0m\033[91m ┃\033[0m")
        print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
        print("")
        print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
        print("\033[91m Error: please contact developer or community 210 \033[0m.")
        print("")
        print(" \033[94m─────────────────────────────────────\033[0m")
        while True:
            inputtop = input(" \033[91mError Please Enter....\033[90")
            if inputtop == "":
                os.system("clear")
                time.sleep(0.5)
                bck.m_backup()
                return
            else:
                print(f"Why are you entering input {inputtop}?, please ")
    zip_file_path = os.path.join(restore_directory, downloaded_files[0])
    extract_dir = os.path.join(restore_directory, "extracted")
    os.makedirs(extract_dir, exist_ok=True)
    ext(zip_file_path, extract_dir, zip_password)
    koplakakajs(extract_dir)
    os.remove(zip_file_path)
    printt.prints(f"Please reboot the server By Pressing Enter!", speed=0.05, color="orange")
    load.loading(2)
    os.system("rm -r /root/extracted")
    os.system("sudo chown www-data:www-data /etc/qos/limit/quota.json")
    os.system("sudo chmod +x /etc/qos/limit/quota.json")
    os.system("sudo chmod +x /etc/qos/limit/traffic_cache.json")
    os.system("sudo chown www-data:www-data /etc/qos/limit/traffic_cache.json")
    zipfile(restore_directory)
    clear()
    print(f" \033[94m╔═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╗\033[0m")
    print(f" \033[91m┃\033[0m \033[94m               Restore               \033[0m\033[91m ┃\033[0m")
    print(f" \033[94m╚═\033[0m\033[91m─────────────────────────────────────\033[0m\033[94m═╝\033[0m")
    print("")
    print(f"   \033[92m𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆\033[0m")
    printt.prints(f" RESTORE Completed ", speed=0.04, color="green")
    print("")
    print(" \033[94m─────────────────────────────────────\033[0m")
    while True:
        inputtop = input(" \033[93mPlease Enter To Reboot...\033[0m")
        if inputtop == "":
            os.system("clear")
            time.sleep(0.5)
            os.system("reboot")
            return
        else:
            print(f"\033[91mWhy are you entering input {inputtop}?, please Enter To Reboot\033[91m")
