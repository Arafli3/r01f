import os
import re
import time
import uuid
from .lolcat import lolcat
from datetime import datetime, timedelta
import base64
from colorama import Fore, Back, Style, init
init(autoreset=True)
import signal
import importlib
import json
import textwrap
def handle_sigint(signum, frame):
    lolcat("  \nYou press ( Ctrl+c )to exit. Input ( R01F ) to Run it again\n")
    os._exit(0)

signal.signal(signal.SIGINT, handle_sigint)

def log(message, log_file):
    with open(log_file, 'a') as file:
        file.write(f"{message}\n")
    print(message)
    
def green(text):
    print(f"\033[32;1m{text}\033[0m")

def red(text):
    print(f"\033[31;1m{text}\033[0m")

os.system("clear")

def setup_user():
    back = importlib.import_module("modules.vvx")
    with open('/etc/xray/domain') as f:
        domain = f.read().strip()
    with open('/usr/local/etc/xray/org') as f:
        ISP = f.read().strip()
    with open('/usr/local/etc/xray/city') as f:
        CITY = f.read().strip()
    print(f"{Fore.BLUE}{Style.BRIGHT}╔═{Fore.RED}─────────────────────────────────────{Fore.BLUE}═╗")
    print(f"{Fore.RED}┃{Fore.BLUE}         Create a VLESS account       {Fore.RED} ┃")
    print(f"{Fore.BLUE}╚═{Fore.RED}─────────────────────────────────────{Fore.BLUE}═╝")
    lolcat("Type ( x ) to exit/cancel\n")
    print("")
    user = ""
    while True:
        user = input(" \033[93mUsername: \033[0m").strip()
        if user == "x":
            print(f"\033[93mExiting the VLESS create process.\033[0m")
            time.sleep(0.5)
            os.system('clear')
            back.vless_menu()
            return None, None, None, None
        if len(user) > 20:
            print("\033[91mUsername is too long! Maximum allowed is 20 characters.\033[0m")
            continue
        elif re.match(r'^[a-zA-Z0-9_]+$', user):
            if os.system(f"grep -qw '### {user}' /etc/qos/xray/xrayall.txt") == 0:
                print(f"\033[93m Try again Use another Username.\033[0m \033[91m{user}\033[0m \033[93malready exists\033[0m")
            else:
                print(f" \033[92mConfirmed\033[0m")
                break
        else:
            print(f"\033[91mInvalid username format.\033[0m")
    user_uuid = ""
    while True:
        user_uuid = input(" \033[93mUuid (pass) [Leave blank to auto-generate]: \033[0m").strip()
        if user_uuid == "x":
            print(f"\033[93mExiting the TROJAN create process.\033[0m")
            time.sleep(0.5)
            os.system('clear')
            back.vless_menu()
            return None, None, None, None
        if user_uuid == "":
            print("\033[92m UUID is empty. Automatically generate UUID...\033[0m")
            user_uuid = str(uuid.uuid4())
            print(f"\033[92m Automatically generated UUID: {user_uuid}\033[0m")
        if len(user_uuid) <= 7:
            print("\033[91m UUID/pass must be more than 7 characters.\033[0m")
            continue
        try:
            with open('/etc/qos/xray/uuid.txt', 'r') as file:
                existing_uuids = file.read().splitlines()
            if user_uuid in existing_uuids:
                print("\033[91m UUID already exists, please enter a different UUID.\033[0m")
                continue
            print(f"\033[92mUUID/PASS confirmed.\033[0m")
            break
        except FileNotFoundError:
            print("\033[91m If there is an error please contact dev/Community \033[0m")
            break
        except Exception as e:
            print(f"\033[91mIf there is an error please contact dev/Community: {e}\033[0m")
            break
    Quota = ""
    exittol = False
    while not exittol:
        Quota = input(" \033[93mQuota (Limit): \033[0m").strip()
        if Quota == "":
            while True:
                lolcat(f"\nAre you sure to add User {user} with Unlimited Quota? \n")
                opsi = input(f"\033[93mSelect Y to continue, select N to cancel (Y/N):\033[0m").strip()
                if opsi.lower() == "y":
                    Quota = "unlimited"
                    exittol = True
                    print(f" \033[92m Add Unlimited Quota to User {user}\033[0m")
                    break
                elif opsi.lower() == "n":
                    print("\033[93m Cancel User to unlimited\033[0m")
                    break
                else:
                    print("\033[91m What do you do, choose the option that is ordered\033[0m")
        elif Quota.lower() == "x":
            print(f"\033[93mExiting the VMESS create process.\033[0m")
            time.sleep(0.5)
            os.system('clear')
            back.vmess_menu()
            exittol = True
            return None, None, None, None
        elif not re.match(r'^\d+$', Quota):
            print(f"\033[91mPlease enter a valid number.\033[0m")
        else:
            print(f"\033[92mQuota Added: {Quota} GB\033[0m")
            break
    exittols = False
    while not exittols:
        batasip = input(" \033[93mUser limits: \033[0m").strip()
        if batasip.lower() == "x":
            print(" \033[93mExiting the VMESS creation process.\033[0m")
            time.sleep(0.5)
            os.system("clear")
            back.vless_menu()
            return None, None, None, None, None
        if batasip.isdigit():
            batasip = int(batasip)
            print(f"\033[92mlimits Added: {batasip}\033[0m")
            break
        elif batasip == "":
            while True:
                print(f" \033[92m Are you sure you want to add Unlimited limit to User \033[0m\033[93m{user}\033[0m\033[92m? \033[0m")
                opsi = input(" \033[93m Input (Y/N): \033[0m").strip()
                if opsi.lower() == "y":
                    batasip = "unlimited"
                    exittols = True
                    print(f" \033[92m Successfully added User \033[0m\033[93m{user}\033[0m\033[92m as unlimitid\033[0m")
                    break
                elif opsi.lower() == "n":
                    print(" \033[91m Cancel User Limit to unlimited \033[0m")
                    break
                else:
                    print(" \033[91m Please Select the appropriate Option \033[0m")
        else:
            print(f"\033[91mPlease enter a valid number.\033[0m")
    masaaktif = ""
    while True:
        masaaktif = input(" \033[93mExpired (Days): \033[0m").strip()
        if masaaktif == "x":
            print(f"\033[93mExiting the VLESS create process.\033[0m")
            time.sleep(0.5)
            os.system('clear')
            back.vless_menu()
            return None, None, None
        elif not re.match(r'^\d+$', masaaktif):
            print(f"\033[91mPlease enter the number correctly.\033[0m")
        else:
            masaaktif_days = int(masaaktif)
            if masaaktif_days > 10000:
                print("\033[91mDuration too large! Maximum allowed is 10000 days.\033[0m")
            else:
                print(f"\033[92mAdded.\033[0m")
                break
    return user, Quota, masaaktif, user_uuid, batasip
def vless_main():
    back = importlib.import_module("modules.vvx")
    user, Quota, masaaktif, user_uuid, batasip = setup_user()
    uuid_file = '/etc/qos/xray/uuid.txt'
    uuid_dir = os.path.dirname(uuid_file)
    vl_dir = '/etc/qos/xray/vless.txt'
    pathfile = "/etc/qos/xray/limitxray"
    pathuid = "/etc/qos/xray/alluuid"
    try:
        with open(pathfile, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []
    lines.append(user + ' ' + str(batasip) + '\n')
    with open(pathfile, 'w') as file:
        file.writelines(lines)
    try:
        with open(pathuid, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []
    lines.append(user + ' ' + user_uuid + '\n')
    with open(pathuid, 'w') as file:
        file.writelines(lines)
    all = '/etc/qos/xray/xrayall.txt'
    usage1 = f"/etc/qos/xray/usage/{user}"
    with open('/etc/xray/domain') as f:
        domain = f.read().strip()
    with open('/usr/local/etc/xray/org') as f:
        ISP = f.read().strip()
    with open('/usr/local/etc/xray/city') as f:
        CITY = f.read().strip()

    if user:
        with open('/etc/xray/domain') as f:
            domain = f.read().strip()
        if not os.path.exists(usage1):
            with open(usage1, 'w') as file:
                pass
        if Quota.strip().lower() == "unlimited":
            quota1 = "unlimited"
        elif Quota.isdigit():
            quota1 = str(int(Quota) * 1024 * 1024 * 1024)
        else:
            print("erorororro")
        with open(usage1, "w") as file:
            file.write(quota1)
        hariini = datetime.now()
        masaaktif = int(masaaktif)
        expdate = hariini + timedelta(days=masaaktif)
        expiration_date = expdate.strftime("%Y-%m-%d:%H")
        try:
            if not os.path.exists(uuid_dir):
                print(f"\033[92m Subdirectory does not exist. Creating subdirectory...\033[0m")
                os.makedirs(uuid_dir, exist_ok=True)
            with open(uuid_file, 'a') as file:
                file.write(f"{user_uuid}\n")
        except FileNotFoundError:
            print(f"\033[91mIf there is an error please contact dev/Community.\033[0m")
        except Exception as e:
            print(f"\033[91mIf there is an error please contact dev/Community: {e}\033[0m")
            
        try:
            if not os.path.exists(vl_dir):
                print(f"\033[92m Subdirectory does not exist. Creating subdirectory...\033[0m")
                os.makedirs(vm_dir, exist_ok=True)
            with open(vl_dir, 'a') as pile:
                pile.write(f"### {user} {expiration_date}\n")
            with open(all, 'a') as f:
                f.write(f"### {user} {expiration_date}\n")
        except FileNotFoundError:
            print(f"If there is an error please contact dev/Community")
        except Exception as e:
            print(f"If there is an error please contact dev/Community : {e}")
        configpath = '/etc/xray/config.json'
        with open(configpath, 'r') as fil3:
            config = json.load(fil3)
        vluser = {
            "id": user_uuid,
            "email": user,
            "quota": quota1,
            "expiry": expiration_date
        }
        vlgrpc = {
            "id": user_uuid,
            "email": user,
            "expiry": expiration_date
        }
        for inbound in config['inbounds']:
            if inbound['protocol'] == 'vless':
                inbound['settings']['clients'].append(vluser)
                break
        for inbound in config['inbounds']:
            if inbound['protocol'] == 'vless':
                if inbound['streamSettings']['network'] in ['grpc']:
                    inbound['settings']['clients'].append(vlgrpc)
                    break
        with open(configpath, 'w') as gme:
            json.dump(config, gme, indent=2)
        print("\033[91mHa ha ha\033[0m")
        time.sleep(0.5)
        os.system("clear")

        vless_link1 = (f"vless://{user_uuid}@{domain}:443?path=/vless&security=tls&encryption=none&type=ws&sni={domain}&host={domain}#${user}")
        vless_link2 = (f"vless://{user_uuid}@{domain}:80?path=/vless&encryption=none&type=ws&host={domain}#${user}")
        vless_link3 = (f"vless://{user_uuid}@{domain}:443?mode=gun&security=tls&encryption=none&type=grpc&serviceName=vless-grpc&sni=isi_bug#{user}")
        css = textwrap.dedent("""\
            {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .header {
            width: 100%;
            background: linear-gradient(to right, #ff0000 50%, #ffffff 50%);
            color: #333;
            padding: 20px 0;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }

        .logo {
            font-size: 2.5rem;
            font-weight: bold;
            background: linear-gradient(to right, #ffffff 50%, #ff0000 50%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            margin-bottom: 10px;
        }

        .tagline {
            font-size: 1rem;
            color: #333;
        }

        .main-container {
            width: 90%;
            max-width: 1000px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            margin-bottom: 30px;
            gap: 20px;
        }

        .container {
            flex: 1;
            min-width: 300px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            padding: 25px;
            border-top: 5px solid #ff0000;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .container:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
        }

        h1 {
            color: #ff0000;
            margin-bottom: 20px;
            text-align: center;
        }

        h2 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.3rem;
            text-align: center;
            padding-bottom: 10px;
            border-bottom: 2px dashed #ff0000;
        }

        .text-box {
            position: relative;
            margin-bottom: 20px;
        }

        .text-area {
            width: 100%;
            min-height: 150px;
            padding: 15px;
            border: 2px solid #ddd;
            border-radius: 5px;
            resize: vertical;
            font-size: 16px;
            transition: border-color 0.3s;
        }

        .text-area:focus {
            border-color: #ff0000;
            outline: none;
        }

        .copy-btn {
            position: absolute;
            right: 10px;
            bottom: 10px;
            background-color: #ff0000;
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .copy-btn:hover {
            background-color: #cc0000;
            transform: translateY(-2px);
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }

        .copy-btn:active {
            transform: translateY(0);
        }

        .copy-btn::before {
            content: "📋";
        }

        .copy-btn.copied {
            background-color: #4CAF50;
        }

        .copy-btn.copied::before {
            content: "✓";
        }

        .copy-notification {
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: #4CAF50;
            color: white;
            padding: 15px;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            opacity: 0;
            transition: opacity 0.5s;
            z-index: 1000;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .copy-notification::before {
            content: "✓";
            font-size: 1.2rem;
        }

        .footer {
            width: 100%;
            background: linear-gradient(to right, #ff0000 50%, #ffffff 50%);
            color: #333;
            text-align: center;
            padding: 15px 0;
            margin-top: auto;
            font-size: 0.9rem;
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        .pulse {
            animation: pulse 0.5s ease-in-out;
        }

        @media (max-width: 768px) {
            .main-container {
                flex-direction: column;
                align-items: center;
            }
            
            .container {
                width: 100%;
            }
            
            .logo {
                font-size: 2rem;
            }
        }

        @media (max-width: 480px) {
            .logo {
                font-size: 1.8rem;
            }
            
            .container {
                padding: 20px;
            }
            
            h1 {
                font-size: 1.5rem;
            }
            
            h2 {
                font-size: 1.1rem;
            }
        }
        """)
        js = textwrap.dedent("""\
        {
            const textArea = document.getElementById(id);
            textArea.select();
            document.execCommand('copy');
            
            const notification = document.getElementById('copyNotification');
            notification.style.opacity = '1';
            
            button.classList.add('copied');
            button.classList.add('pulse');
            setTimeout(() => {
                button.classList.remove('pulse');
            }, 500);
            
            setTimeout(() => {
                button.classList.remove('copied');
            }, 2000);
            
            setTimeout(() => {
                notification.style.opacity = '0';
            }, 3000);
        }
        """)
        html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Format Open Clash</title>
    <style>
        * {css}
    </style>
</head>
<body>
    <header class="header">
        <div class="logo">R01FInject</div>
        <div class="logo">Format Open Clash</div>
        <div class="logo">{user}</div>
        <div class="tagline">GME Corporation</div>
    </header>

    <h1>Salin Format yang Anda Butuhkan</h1>

    <div class="main-container">
        <div class="container">
            <h2>Format Vless Tls</h2>
            <div class="text-box">
                <textarea class="text-area" id="text1">- name: {user}
  type: vless
  server: {domain}
  port: 443
  uuid: {user_uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: true
  skip-cert-verify: true
  servername: {domain}
  network: ws
  ws-opts:
    path: /vless
    headers:
      Host: {domain}</textarea>
                <button class="copy-btn" onclick="copyText('text1', this)">Salin</button>
            </div>
        </div>
        <div class="container">
            <h2>Format Vless Ntls</h2>
            <div class="text-box">
                <textarea class="text-area" id="text2">- name: {user}
  type: vless
  server: {domain}
  port: 80
  uuid: {user_uuid}
  alterId: 0
  cipher: auto
  udp: true
  tls: false
  skip-cert-verify: false
  servername: {domain}
  network: ws
  ws-opts:
    path: /vless
    headers:
      Host: {domain}</textarea>
                <button class="copy-btn" onclick="copyText('text2', this)">Salin</button>
            </div>
        </div>
        <div class="container">
            <h2>Format Vmess GRPC</h2>
            <div class="text-box">
                <textarea class="text-area" id="text3">- name: {user}
  server: {domain}
  port: 443
  type: vless
  uuid: {user_uuid}
  alterId: 0
  cipher: auto
  network: grpc
  tls: true
  servername: {domain}
  skip-cert-verify: true
  grpc-opts:
    grpc-service-name: vless-grpc</textarea>
                <button class="copy-btn" onclick="copyText('text3', this)">Salin</button>
            </div>
        </div>
    </div>

    <div class="copy-notification" id="copyNotification">
        Teks telah disalin!
    </div>

    <footer class="footer">
        © 2025 GME Copyright 
    </footer>

    <script>
        function copyText(id, button) {js}
    </script>
</body>
</html>"""

        output_path = f"/var/www/html/vless-{user}"
        with open(output_path, 'w') as file:
            file.write(html_content)
        os.system("systemctl restart xray > /dev/null 2>&1")
        os.system("service cron restart > /dev/null 2>&1")
        log_file = f"/etc/xraylog/log-vless-{user}.txt"
        separator_blue = f"\033[94m━════════════━\033[0m"
        separator_red = f"\033[91m━════════════━\033[0m"
        log(f" {separator_blue} ", log_file)
        log(" DETAIL VLESS ACCOUNT ", log_file)
        log(f" {separator_red} ", log_file)
        log(f" \033[93mRemarks        :\033[0m \033[92m{user}\033[0m ", log_file)
        log(f" \033[93mQuota          :\033[0m \033[92m{quota1} GB\033[0m ", log_file)
        log(f" \033[93mLimit User     : \033[0m \033[92m{batasip} IP\033[0m ", log_file)
        log(f" \033[93mDomain         :\033[0m \033[92m{domain}\033[0m ", log_file)
        log(f" \033[93mISP            :\033[0m \033[92m{ISP}\033[0m ", log_file)
        log(f" \033[93mRegion         :\033[0m \033[92m{CITY}\033m ", log_file)
        log(f" \033[93mPort TLS/gRPC  :\033[0m \033[92m443, 8443, 2053, 2083, 2087, 2096\033[0m ", log_file)
        log(f" \033[93mPort none TLS  :\033[0m \033[92m80, 2082, 8880, 8080, 2095, 2086, 2052\033[0m ", log_file)
        log(f" \033[93mid             :\033[0m \033[92m{user_uuid}\033[0m ", log_file)
        log(f" \033[93mSecurity       :\033[0m \033[92mauto\033[0m ", log_file)
        log(f" \033[93mNetwork        :\033[0m \033[92mws\033[0m ", log_file)
        log(f" \033[93mPath           :\033[0m \033[92m/vless\033[0m ", log_file)
        log(f" \033[93mService Name   :\033[0m \033[92m/vless-grpc\033[0m ", log_file)
        log(f" {separator_blue} ", log_file)
        log(f" \033[93mLink TLS       :\033[0m \033[92m{vless_link1}\033[0m ", log_file)
        log(f" {separator_red} ", log_file)
        log(f" \033[93mLink none TLS  :\033[0m \033[92m{vless_link2}\033[0m ", log_file)
        log(f" {separator_blue} ", log_file)
        log(f" \033[93mLink gRPC      :\033[0m \033[92m{vless_link3}\033[0m ", log_file)
        log(f" {separator_red} ", log_file)
        log(f" \033[93mFormat OpenClash :\033[0m \033[92mhttps://{domain}:81/vless-{user}\033[0m ", log_file)
        log(f" \033[93mRules and policies : \033[0m \033[92mhttps://{domain}:81/informasi\033[0m ", log_file)
        log(f" {separator_blue} ", log_file)
        log(f" \033[93mExpired On     :\033[0m \033[92m{expiration_date}\033[0m", log_file)
        log(f" \033[93mExpiry date\033[0m \033[91m{masaaktif}\033[0m \033[93mdays from\033[0m \033[92m{expiration_date}\033[0m", log_file)
        log(f" {separator_red} ", log_file)
        log(f" 𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐔𝐒𝐈𝐍𝐆 𝐑𝟎𝟏𝐅 𝐓𝐔𝐍𝐍𝐄𝐋𝐈𝐍𝐆", log_file)
        lolcat("\n Press Enter to return to create account or type 'x' to exit...\n")
        while True:
            action = input(" \033[93mInput Options:\033[0m ").strip().lower()
            if action == "x":
                print(f"\033[93mExiting the VLESS create process.\033[0m")
                time.sleep(0.5)
                os.system("clear")
                back.vless_menu()
                break
            elif action == "":
                os.system("clear")
                vless_main()
                break
            else:
                print("\033[91mPlease enter 'x' to exit or press Enter to return.\033[0m")