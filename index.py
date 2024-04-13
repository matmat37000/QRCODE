import os
from pprint import pprint
import time

from colorama import Fore
from qrcode import ERROR_CORRECT_H, ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q
import qrcode

import command
import crash
from log import Log
import read_app

answer_liste = ["  1) Create a QRCODE", "  2) Read a QRCODE", "  3) Clear image dir", "  4) Close"]

def QRCODE(NAME, DATA, VERSION=1, ERROR_CORRECT=ERROR_CORRECT_L, BOX_SIZE=10, BORDER=4):
    qr = qrcode.QRCode(
    version=VERSION,
    error_correction=ERROR_CORRECT,
    box_size=BOX_SIZE,
    border=BORDER,
    )
    qr.add_data(DATA)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    try:
        img.save(f"QRCODE/{NAME}.png")
    except:
        print("The QRCODE '" + Fore.LIGHTBLUE_EX + f"{NAME}.png" + Fore.WHITE + "' cannot be created !")
        Log(f"The QRCODE '{NAME}.png' cannot be created !")
    else:
        path = os.path.abspath(f"QRCODE/{NAME}.png")
        print(f"Image save in '{Fore.LIGHTBLUE_EX + path + Fore.WHITE}'")# \\{NAME}.png")
        Log(f"Image save in '{path}'")
        time.sleep(2)

def MENU():
    loop = True
    
    while loop:
        command.CLEAR_PROMPT()
        print("What do you want to do ?\n")
        for a in answer_liste:
            print(a)
        answer = input("\n  -> ")
        if answer == "1":
            command.CLEAR_PROMPT()
            QRCODE(input("Name: "), input("Data: "))
            # loop = False
        elif answer == "2":
            command.CLEAR_PROMPT()
            read_app.READ()
            # loop = False
        elif answer == "3":
            command.CLEAR_QRCODE_DIR()
            command.CLEAR_PROMPT()
        elif answer == "4":
            print("  Exit.")
            loop = False
        else:
            read_app.ERROR(answer_liste)

def INIT():
    if os.path.exists('./QRCODE'):
        print("OK")
    else:
        os.makedirs('./QRCODE')
        

try:
    INIT()
    MENU()
except Exception as e: 
    crash.CRASH(e=e)
    time.sleep(15)
