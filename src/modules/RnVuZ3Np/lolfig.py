import subprocess

def lolfig(text, font="slant"):
    try:
        figlet_process = subprocess.Popen(
            ['/usr/bin/figlet', '-f', font], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        figlet_output, figlet_error = figlet_process.communicate(input=text.encode())
        
        if figlet_process.returncode != 0:
            print(f"Figlet Error: {figlet_error.decode()}")
            return
        lolcat_process = subprocess.Popen(
            ['/usr/games/lolcat', '--force'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        lolcat_output, lolcat_error = lolcat_process.communicate(input=figlet_output)
        
        if lolcat_process.returncode != 0:
            print(f"Lolcat Error: {lolcat_error.decode()}")
            return
        print(lolcat_output.decode(), end='')
    
    except FileNotFoundError as e:
        print("Error: Pastikan 'figlet' dan 'lolcat' sudah diinstal di sistem Anda.")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")

