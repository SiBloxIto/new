import os
import platform
import time
import sys

# Ensure the requests module is installed properly
try:
    import requests
except ImportError:
    os.system("pip uninstall requests -y")
    os.system("pip install requests")

def check_for_updates():
    print('\033[1;91m[\033[1;97m-\033[1;91m] \033[1;97mChecking For Update...')
    # Suppressing output errors for git pull
    os.system('git pull --quiet 2>/dev/null')

def check_architecture():
    bit = platform.architecture()[0]
    if bit == '64bit':
        print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m64Bit Found')
        try:
            import FILE64
        except ImportError as e:
            print(f"\033[1;91m[\033[1;97m✗\033[1;91m] \033[1;97mError importing FILE64: {e}")
    elif bit == '32bit':
        print('\033[1;91m[\033[1;97m✓\033[1;91m] \033[1;97m32Bit Found')
        try:
            import FILE32
        except ImportError as e:
            print(f"\033[1;91m[\033[1;97m✗\033[1;91m] \033[1;97mError importing FILE32: {e}")
    else:
        print(f"\033[1;91m[\033[1;97m✗\033[1;91m] \033[1;97mUnsupported architecture: {bit}")

if __name__ == "__main__":
    check_for_updates()
    check_architecture()
