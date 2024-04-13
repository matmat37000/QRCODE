from colorama import Fore, Back, Style
import log

def CRASH(e):
    print('The application crashed with the following error:\n' + Fore.RED + f'{e}' + Fore.WHITE)
    log.Log(f"The application crashed with the following error: {e}")