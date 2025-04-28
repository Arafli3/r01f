import subprocess

def lolcat(text):
    process = subprocess.Popen(
        ['/usr/games/lolcat', '--force'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, _ = process.communicate(input=text.encode())
    print(stdout.decode(), end='')