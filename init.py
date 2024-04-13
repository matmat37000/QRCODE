import os

def INIT():
    if os.path.exists('./QRCODE'):
        print("OK")
    else:
        os.mkdir('QRCODE')