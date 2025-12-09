#!/usr/bin/env python3
import os
import sys
import time

# ========== COLORS ==========
RED     = "\033[1;31m"
GREEN   = "\033[1;32m"
YELLOW  = "\033[1;33m"
BLUE    = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN    = "\033[1;36m"
WHITE   = "\033[1;37m"
RESET   = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def loading():
    clear()
    print(f"{CYAN}Launching REHAN Z4X 🫥 Tool", end="")
    for _ in range(6):
        time.sleep(0.4)
        print(" .", end="", flush=True)
    time.sleep(0.5)

# ========== BIG STYLISH BANNER ==========
def banner():
    clear()
    print(f"""{CYAN}
╔════════════════════════════════════════════════╗
║                                                ║
║   {GREEN}██████╗ ███████╗██╗  ██╗ █████╗ ███╗   ██╗{CYAN}   ║
║   {GREEN}██╔══██╗██╔════╝██║  ██║██╔══██╗████╗  ██║{CYAN}   ║
║   {GREEN}██████╔╝█████╗  ███████║███████║██╔██╗ ██║{CYAN}   ║
║   {GREEN}██╔══██╗██╔══╝  ██╔══██║██╔══██║██║╚██╗██║{CYAN}   ║
║   {GREEN}██║  ██║███████╗██║  ██║██║  ██║██║ ╚████║{CYAN}   ║
║   {GREEN}╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝{CYAN}   ║
║                {WHITE}Z 4 X   🫥{CYAN}                      ║
╠════════════════════════════════════════════════╣
║  {MAGENTA}REHANZX TOOL v1.0                            {CYAN}║
║  {BLUE}INSTAGRAM ID  : rehan_z4x                     {CYAN}║
║  {GREEN}GITHUB        : github.com/rehanz4x          {CYAN}║
║  {YELLOW}TELEGRAM ID   : @mere_papa_0                 {CYAN}║
║  {CYAN}TG CHANNEL     : @NETWORKXTG2                 {CYAN}║
║                                                ║
╚════════════════════════════════════════════════╝
{RESET}""")

def start_tool():
    loading()
    print(f"\n{GREEN}[+] Starting Old Tool...{RESET}\n")
    time.sleep(1)
    os.system("python rehanzx_old.py")

def main():
    while True:
        banner()
        print(f"""
{CYAN}[1]{GREEN} Start Tool
{CYAN}[2]{RED} Exit
""")

        choice = input(f"{YELLOW}Select Option >> {RESET}")

        if choice == "1":
            start_tool()
            input(f"\n{CYAN}Press Enter to return to launcher...{RESET}")
        elif choice == "2":
            clear()
            print(f"{RED}Exiting... Goodbye Bro 👋{RESET}")
            time.sleep(1)
            sys.exit()
        else:
            print(f"{RED}Invalid option! Try again...{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()


