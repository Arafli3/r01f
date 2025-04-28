import os 
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from modules.MNG import R01F_M

def main():
   R01F_M()
if __name__ == "__main__": 
 main()