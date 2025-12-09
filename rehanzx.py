#!/usr/bin/env python3
import os
import sys
import time

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

VERSION = "1.0"

def clear():
    os.system("clear")

def banner():
    print(f"""{CYAN}
██████╗ ███████╗██╗  ██╗ █████╗ ███╗   ██╗███████╗██╗  ██╗
██╔══██╗██╔════╝██║  ██║██╔══██╗████╗  ██║╚══███╔╝╚██╗██╔╝
██████╔╝█████╗  ███████║███████║██╔██╗ ██║  ███╔╝  ╚███╔╝ 
██╔══██╗██╔══╝  ██╔══██║██╔══██║██║╚██╗██║ ███╔╝   ██╔██╗ 
██║  ██║███████╗██║  ██║██║  ██║██║ ╚████║███████╗██╔╝ ██╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
{YELLOW}🔥 REHANZX TOOL v{VERSION} 🔥{RESET}
{GREEN}Author : Rehanz4x
GitHub : https://github.com/rehanz4x{RESET}
""")

def check_update():
    print(f"{YELLOW}[+] Checking for updates...{RESET}")
    os.system("git pull")
    print(f"{GREEN}[+] Update check complete!{RESET}")
    time.sleep(1)

def main_menu():
    clear()
    banner()
    print(f"""
{CYAN}[1]{WHITE} Start Tool
{CYAN}[2]{WHITE} Check Update
{CYAN}[3]{WHITE} About
{CYAN}[4]{WHITE} Exit
""")

    choice = input(f"{YELLOW}Select Option >> {RESET}")

    if choice == "1":
        print(f"{GREEN}Tool Starting...{RESET}")
        time.sleep(1)

    elif choice == "2":
        check_update()
        main_menu()

    elif choice == "3":
        print(f"""
{CYAN}RehanzX Tool
Version : {VERSION}
Developer : Rehanz4x
GitHub : https://github.com/rehanz4x{RESET}
""")
        input("Press Enter to go back...")
        main_menu()

    elif choice == "4":
        print(f"{RED}Goodbye!{RESET}")
        sys.exit()

    else:
        print(f"{RED}Invalid Option!{RESET}")
        time.sleep(1)
        main_menu()

if __name__ == "__main__":
    main_menu()
