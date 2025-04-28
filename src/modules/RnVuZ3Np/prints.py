import time
COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "orange": "\033[38;5;214m",
    "reset": "\033[0m"
}

def prints(text, speed=0.1, color=None):
    color_code = COLORS.get(color, COLORS["reset"])

    for char in text:
        print(f"{color_code}{char}", end='', flush=True)
        time.sleep(speed)
    
    print(COLORS["reset"])

