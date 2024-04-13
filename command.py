import os

from log import Log

def CLEAR_QRCODE_DIR():
    lst = os.listdir("./QRCODE/")
    for file in lst:
        os.remove(f"./QRCODE/{file}")
    Log("Clear dir")
        
def CLEAR_PROMPT():
    os.system('cls')