import time
import sys

speed = 0.1

def done():
    return "Done"
def loadings(text, duration):
    animation = "|/-\\"
    start_time = time.time()

    while time.time() - start_time < duration:
        for frame in animation:
            sys.stdout.write(f"\r{text} {frame}")
            sys.stdout.flush()
            time.sleep(speed)

    sys.stdout.write(f"\r{text} \033[92m{done()}\033[0m\n")
    sys.stdout.flush()