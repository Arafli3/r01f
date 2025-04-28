from datetime import datetime
import os
import subprocess
import time
logssh = '/var/log/sshxp.log'
if not os.path.exists(logssh):
    with open(logssh, "w") as log:
        log.write("\033[92m=== \033[0m\033[93mLOG STARTED\033[0m\033[92m ===\033[0m\n" + "\033[92m-\033[0m" * 50 + "\n")

def gme_log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M]")
    sshlog = f"{timestamp} {message}\n" + "\033[92m-\033[0m" * 50 + "\n"
    with open(logssh, "a") as log:
        log.write(sshlog)
    print(logssh, end="")
def userxp(pathfil1):
    userxpsh = []
    userdanxp = []
    userblumxp = []
    with open(pathfil1, 'r') as f:
        for baris in f:
            if baris.startswith("###"):
                try:
                    bagian = baris.strip().split()
                    user = bagian[1]
                    waktuxp = bagian[2]
                    userexpp = user + ' ' + waktuxp
                    thnblntgljam = datetime.strptime(waktuxp, "%Y-%m-%d:%H")
                    skrng = datetime.now()
                    if thnblntgljam <= skrng:
                        userxpsh.append(user)
                        userdanxp.append(userexpp)
                    if thnblntgljam > skrng:
                        userblumxp.append(userexpp)
                except (IndexError, ValueError) as e:
                    gme_log(f" {e} : {baris.strip()}")
    return userxpsh, userdanxp, userblumxp

def deletessh():
    pathfil1 = '/etc/qos/ssh/sshadmin.txt'
    userxpsh, userdanxp, userblumxp = userxp(pathfil1)
    for user in userxpsh:
        checkusr = subprocess.run(["id", user], capture_output=True, text=True)
        if checkusr.returncode == 0:
            gme_log(f"Delete {user}")
            subprocess.run(["userdel", "-r", user])
        else:
            gme_log(f" \033[91mUser Not Found {user}\033[0m")
            for file1 in userxpsh:
                b = [f"/etc/xraylog/log-ssh-{file1}.txt"]
                for a in b:
                    if os.path.exists(a):
                        os.remove(a)
                        gme_log(f" \033[92m{a} successfully deleted\033[0m")
                    else:
                        gme_log(f" \033[91m{a} User not found\033[0m")
    barissbaru = []
    try:
        with open(pathfil1, 'r') as f:
            for line in f:
                if not (line.startswith("###") and any(userr in line for userr in userdanxp)):
                    barissbaru.append(line)
        with open(pathfil1, 'w') as f:
            f.writelines(barissbaru)
    except FileNotFoundError:
        gme_log(" \033[91mError: File Not found\033[0m")
    os.system("systemctl restart ssh")

def cek_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            for baris in file:
                if baris.startswith("###"):
                    try:
                        bagian = baris.strip().split()
                        user = bagian[1]
                        tanggal_jam_str = bagian[2]
                        tanggal_jam = datetime.strptime(tanggal_jam_str, "%Y-%m-%d:%H")
                        sekarang = datetime.now()
                        if tanggal_jam <= sekarang:
                            deletessh()
                        else:
                            gme_log("\033[93m There is no User exp for now\033[0m")
                    except (IndexError, ValueError) as e:
                        gme_log(f" \033[91mError Unable to process user account row: {baris.strip()}. Error: {e}\033[0m")
    except FileNotFoundError:
        print(f" \033[91m Eror: file not found \033[0m")

def main():
    nama_file = '/etc/qos/ssh/sshadmin.txt'
    men = 1
    nit = men * 60
    while True:
        gme_log("\033[93mINFO: \033[0mStart Processing User Expired.... ")
        cek_file(nama_file)
        gme_log(f"\033[93mINFO:\033[0m Wait {men} minutes for the next process.\n")
        time.sleep(nit)
if __name__ == "__main__":
    main()