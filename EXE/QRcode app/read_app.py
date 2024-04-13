import cv2
import os
import time
import webbrowser

answer_liste = ["  1) Open it", "  2) Don't open it"]

def ERROR(list):
    os.system('cls')
    print("\n  -> " + f"Is not a number between 1-{len(list)}")
    time.sleep(2)
    os.system('cls')

def READ():
    NAME = input("QRCODE name: ")
    d = cv2.QRCodeDetector()
    try: 
        val, points, qrcode = d.detectAndDecode(cv2.imread(f"./QRCODE/{NAME}.png"))
    except:
        os.system('cls')
        path = os.path.abspath(f"./QRCODE/{NAME}.png")
        print(f"QRCODE '{path}' cannot be found, check the spelling and that the image file exists.")
        input()
        os.system('python index.py')
    else:
        print(f"Valeur du QR Code: {val}")
        
        if "http" in val:
            loop = True
            while loop:
                print("Your QRCODE contains a link, do you want to open it ?\n")
                for a in answer_liste:
                    print(a)
                    answer = input("\n  -> ")
                    if answer == "1":
                        webbrowser.open(val)
                        loop = False
                        break
                    elif answer == "2":
                        print("Exit.")
                        loop = False
                    else:
                        ERROR(answer_liste)
        else:
            input()