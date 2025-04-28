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
                match = re.search(r"\d{4}-\d{2}-\d{2}\s+([\d\.]+)\s+(MiB|GiB)\s+\|\s+([\d\.]+)\s+(MiB|GiB)\s+\|\s+([\d\.]+)\s+(MiB|GiB)", line)
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
        
file_path12 = '/usr/bin/data.json'
def userrr():
    with open(file_path12, 'r') as file:
        data = json.load(file)
    user = data.get('user', '')
    partial_user = user[:5]
    return partial_user

def monthly_bandwidth():
    try:
        result = subprocess.run(['vnstat', '-m'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            print(f"\033[91mError: {result.stderr}\033[0m")
            return None
        output = result.stdout
        this_month_usage = None
        
        for line in output.splitlines():
            match = re.search(r"(\d{4}-\d{2})\s+([\d\.]+)\s+(GiB|MiB)\s+\|\s+([\d\.]+)\s+(GiB|MiB)\s+\|\s+([\d\.]+)\s+(GiB|MiB)", line)
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

with open(file_path12, 'r') as f:
    data = json.load(f)

decrypted_text = data['decrypted_text']
expiry = expiry_date(decrypted_text)

def format_expiry_date(decrypted_text):
    parts = decrypted_text.split()
    ip_address = parts[0]
    expiration_date_str = parts[1]

    expiration_date = datetime.strptime(expiration_date_str, "%m-%d-%Y")

    formatted_date = expiration_date.strftime("%A - %B - %Y")
    
    return formatted_date

with open(file_path12, 'r') as f:
    data = json.load(f)

decrypted = data['decrypted_text']
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
        