import datetime
import os


def Log(log):
    now = datetime.datetime.now()
    now2 = (now.strftime("%H:%M:%S %d/%m/%Y"))
    if os.path.exists('Log.log'):
        with open('Log.log', "a") as file:
            file.writelines(f"{now2} | {log}\n")
            file.close()
    else:
        with open('Log.log', "x") as file: file.close()
        Log(log)