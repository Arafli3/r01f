import os
import time
import json
import re
import subprocess
from datetime import datetime
import psutil
import requests
from .lolcat import lolcat
import importlib
import signal 

def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)
def get_isp():
    response = requests.get("https://ipinfo.io/json")
    
    if response.status_code == 200:
        data = response.json()
        isp = data.get("org", "\033[91mISP Not Found\033[0m")
        return isp
    else:
        return "\033[91mFailed to Retrieve Isp Information\033[0m"

def get_local_ip():
    try:
        ip = subprocess.check_output("hostname -I", shell=True).decode().strip()
        return ip
    except subprocess.CalledProcessError:
        return "\033[91mFailed to Retrieve Local IPl\033[0m"
        
def get_domain(file_path):
    try:
        with open(file_path, 'r') as file:
            domain = file.read().strip()
        return domain
    except FileNotFoundError:
        return "\033[91mFile Not Found\033[0m"
    except Exception as e:
        return f"\033[91mEror: {e}\033[0m"

def get_region_and_continent_ipapi():
    try:
        response = requests.get("http://ip-api.com/json?fields=continent,regionName,country")
        if response.status_code == 200:
            data = response.json()
            region = data.get("regionName", "\033[91mRegion Not Found\033[0m")
            country = data.get("country", "\033[91mCountry Not Found\033[0m")
            continent = data.get("continent", "\033[91mContinent Not Found\033[0m")

            return region, country, continent
        else:
            return "\033[91mFailed to get Api key\033[0m", "", ""
    except Exception as e:
        return f"Eror: {e}", "", ""

def custom_time_format():
    now = datetime.now()
    formatted_time = now.strftime("%A %d:%b:%Y | %H:%M:%S")
    return formatted_time

def time_for():
    now = datetime.now()
    formatted_time = now.strftime("%A %d:%b")
    return formatted_time
    
def today_bandwidth():
    try:
        result = subprocess.run(['vnstat', '-d'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            print(f"\033[91mError: {result.stderr}\033[0m")
            return None
        output = result.stdout
        today = datetime.now().strftime('%Y-%m-%d')
        today_usage = None
        for line in output.splitlines():
            if today in line:
                match = re.search(r"\d{4}-\d{2}-\d{2}\s+([\d\.]+)\s+(MiB|GiB|TiB)\s+\|\s+([\d\.]+)\s+(MiB|GiB|TiB)\s+\|\s+([\d\.]+)\s+(MiB|GiB|TiB)", line)
                if match:
                    total_bandwidth = match.group(5) + " " + match.group(6)
                    today_usage = total_bandwidth
                    break

        if today_usage:
            return today_usage
        else:
            return "\033[91mToday's bandwidth usage data not found.\033[0m"
        
    except Exception as e:
        return f"\033[91mEror: {e}\033[0m"
        
file_path = '/usr/bin/data.json'
with open(file_path, 'r') as file:
    data = json.load(file)
user = data.get('user', '')
partial_user = user[:5]

def monthly_bandwidth():
    try:
        result = subprocess.run(['vnstat', '-m'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            print(f"\033[91mError: {result.stderr}\033[0m")
            return None
        output = result.stdout
        this_month_usage = None
        
        for line in output.splitlines():
            match = re.search(r"(\d{4}-\d{2})\s+([\d\.]+)\s+(GiB|MiB|TiB)\s+\|\s+([\d\.]+)\s+(GiB|MiB|TiB)\s+\|\s+([\d\.]+)\s+(GiB|MiB|TiB)", line)
            if match:
                month_year = match.group(1)
                total_bandwidth = match.group(6) + " " + match.group(7)
                this_month_usage = f"{month_year} | {total_bandwidth}"
                break

        if this_month_usage:
            return this_month_usage
        else:
            return "\033[91mCould not find this month's bandwidth usage.\033[0m"
        
    except Exception as e:
        return f"\033[91mAn error occurred: {e}\033[0m"

total_memory = psutil.virtual_memory().total
used_memory = psutil.virtual_memory().used
memory_percent = psutil.virtual_memory().percent

def expiry_date(decrypted_text):
    try:
        parts = decrypted_text.split()
        ip_address = parts[0]
        expiration_date_str = parts[1]

        expiration_date = datetime.strptime(expiration_date_str, "%m-%d-%Y")
        today = datetime.now()

        delta = expiration_date - today

        if delta.days < 0:
            return "Expired"
        else:
            return f"{delta.days} days"
    except (ValueError, IndexError):
        return "Invalid date format"

def format_expiry_date(decrypted_text):
    try:
        parts = decrypted_text.split()
        ip_address = parts[0]
        expiration_date_str = parts[1]

        expiration_date = datetime.strptime(expiration_date_str, "%m-%d-%Y")

        formatted_date = expiration_date.strftime("%A - %B - %Y")
        return formatted_date
    except (ValueError, IndexError):
        return "Invalid date format"

with open(file_path, 'r') as f:
    data = json.load(f)

decrypted = data.get('decrypted_text', '')
expiry = expiry_date(decrypted)
formatted_expiry = format_expiry_date(decrypted)


def bytes_to_human(byte_size):
    if byte_size >= 1024 ** 3:
        return f"{byte_size / (1024 ** 3):.2f} GB"
    else:
        return f"{byte_size / (1024 ** 2):.2f} MB"

wt = time_for()
disk_usage = psutil.disk_usage('/')
wkt = custom_time_format()
region, country, continent = get_region_and_continent_ipapi()
file_path = '/etc/xray/domain'
domain = get_domain(file_path)
local_ip = get_local_ip()
isp = get_isp()

def check_ssh():
    try:
        result = subprocess.run(['systemctl', 'is-active', 'ssh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            return "SSH =\033[92m ON\033[0m"
        else:
            return "SSH = \033[91mOFF\033[0m"
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
def check_Nginx():
    try:
        result = subprocess.run(['systemctl', 'is-active', 'nginx'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return "Nginx =\033[92m ON\033[0m"
        else:
            return "Nginx = \033[91mOFF\033[0m"
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
def check_Xray():
    try:
        result = subprocess.run(['systemctl', 'is-active', 'xray'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return "Xray =\033[92m ON\033[0m"
        else:
            return "Xray = \033[91mOFF\033[0m"
    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        
        
def R01F_M():
    from .VAK import vpn_menu
    from .STG import seting_menu
    from .BPCK import m_backup
    pan = importlib.import_module("modules.panelbot")
    while True:
        os.system("clear")
        print(f"""
     \033[91m╔═\033[0m\033[94m───────────────────────────────────────────\033[0m\033[91m═╗\033[0m
     \033[94m|\033[0m\033[91m                VPS Information              \033[0m\033[94m|\033[0m
   \033[91m╔═╩═\033[0m\033[94m───────────────────────────────────────────\033[0m\033[91m═╝\033[0m
   \033[91m║\033[0m \033[92mISP         : \033[0m{isp}
   \033[94m|\033[0m \033[92mIP VPS      : \033[0m{local_ip}
   \033[94m|\033[0m \033[92mDomain      : \033[0m{domain}
   \033[94m|\033[0m\033[92m Region      : \033[0m{region}/{country}/{continent}
   \033[94m|\033[0m\033[92m Time        : \033[0m{wkt}
   \033[94m|\033[0m\033[92m RAM Usage   : \033[0m{bytes_to_human(used_memory)} | {bytes_to_human(total_memory)} | {memory_percent}%
   \033[94m|\033[0m\033[92m DISK Usage  : \033[0m{bytes_to_human(disk_usage.used)} | {bytes_to_human(disk_usage.total)} | {bytes_to_human(disk_usage.free)} | {disk_usage.percent}%
   \033[94m|\033[0m\033[92m Bandwidth Usage Today  : \033[0m{wt} | {today_bandwidth()}
   \033[91m║\033[0m \033[0m\033[0m\033[92mBandwidth Usage this Month :\033[0m {monthly_bandwidth()}
   \033[91m╠═\033[0m\033[94m────────────────────────────────────────────\033[0m\033[91m═╗\033[0m
  \033[94m|\033[0m          𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙄𝙉𝙏𝙀𝙍𝙉𝙀𝙏 𝙂𝘼𝙈𝙀 \033[94m|\033[0m
  \033[91m╠═\033[0m\033[94m────────────────────────────────────────────\033[0m\033[91m═╝\033[0m
   \033[91m║\033[0m     𝙁𝙧𝙚𝙚𝙙𝙤𝙢 𝙔𝙤𝙪𝙧 𝙉𝙚𝙩𝙬𝙤𝙧𝙠      \033[91m║\033[0m 
   \033[91m╒═\033[0m\033[94m────────────────────────────────────────────\033[0m\033[91m═╕\033[0m  
   \033[94m|\033[0m\033[91mR.\033[0mADD PANELL BOT
   \033[94m|\033[0m\033[91m0.\033[0mVPN Menu
   \033[94m|\033[0m\033[91m1.\033[0mSetting
   \033[94m|\033[0m\033[91mF\033[0m.Backup Data
   \033[91m╘═\033[0m\033[94m─────────────────────\033[91m═╦═\033[0m\033[94m────────────────────\033[0m\033[91m═╛\033[0m
   \033[91m╒═\033[0m\033[94m─────────────────────\033[91m═╩═\033[0m\033[94m────────────────────\033[0m\033[91m═╕\033[0m
       [\033[91m88\033[0m].\033[92mChek System\033[0m \033[94m|\033[0m [\033[91m00\033[0m].\033[92mReboot VPS\033[0m
   \033[91m╘═\033[0m\033[94m─────────────────────\033[91m═╦═\033[0m\033[94m────────────────────\033[0m\033[91m═╛\033[0m
   \033[91m╒═\033[0m\033[94m─────────────────────\033[91m═╩═\033[0m\033[94m────────────────────\033[0m\033[91m═╕\033[0m
     \033[92mClient Name : \033[0m{partial_user}
     \033[92mExpired     : \033[0m{expiry}
     \033[92mExp time    : \033[0m{formatted_expiry}
     \033[92mV.Sc TUNNEL : \033[0m1.0.0
     \033[92mDeveloper   : \033[0m\033[94m𝙂𝙈𝙀\033[0m
   \033[91m╘═\033[0m\033[94m─────────────────────\033[91m═╦═\033[0m\033[94m────────────────────\033[0m\033[91m═╛\033[0m
   \033[91m╒═\033[0m\033[94m─────────────────────\033[91m═╩═\033[0m\033[94m────────────────────\033[0m\033[91m═╕\033[0m
          {check_ssh()}  |  {check_Nginx()}  |  {check_Xray()}
   \033[91m╘═\033[0m\033[94m────────────────────────────────────────────\033[0m\033[91m═╛\033[0m
    """)
        lolcat("\n Press Ctrl+c to exit\n")
        option = input(f" \033[93mInput options: \033[0m").strip()
        if option.lower() == "r":
            os.system("clear")
            pan.panelbot()
        elif option == "0":
            os.system("clear")
            vpn_menu()
            return
        elif option == "1":
            os.system("clear")
            seting_menu()
            return
        elif option.lower() == "f":
            os.system("clear")
            m_backup()
        elif option == "88":
            os.system("gotop")
        elif option == "00":
            os.system("reboot")
        else:
            print("\033[91mYou pressed the wrong button, please try again.\033[0m")
            time.sleep(1)