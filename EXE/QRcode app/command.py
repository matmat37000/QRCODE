import os

def CLEAR_QRCODE_DIR():
    lst = os.listdir("./QRCODE/")
    for file in lst:
        os.remove(f"./QRCODE/{file}")
        
def CLEAR_PROMPT():
    os.system('cls')