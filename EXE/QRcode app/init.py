import os

def INIT():
    if not os.path.isdir("./QRCODE"):
        os.mkdir("./QRCODE")
    