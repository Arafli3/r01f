import time
from .lolcat import lolcat
def loading(duration):
    animation = "|/-\\"
    start_time = time.time()
    while time.time() - start_time < duration:
        for frame in animation:
            print(f"\r\033[93m Please Wait It takes some time...\033[0m {frame}", end="", flush=True)
            time.sleep(0.1)
    lolcat("\rDone!           ")