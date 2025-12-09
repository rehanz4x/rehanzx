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

# ========== CLEAR ==========
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ========== LOADING ==========
def loading(text="Loading"):
    print(f"\n{CYAN}{text}", end="")
    for _ in range(5):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print(RESET)

# ========== BANNER ==========
def banner():
    clear()
    print(f"""{CYAN}
╔════════════════════════════════════════════════════╗
║                                                    ║
║   {GREEN}██████╗ ███████╗██╗  ██╗ █████╗ ███╗   ██╗   {CYAN}║
║   {GREEN}██╔══██╗██╔════╝██║  ██║██╔══██╗████╗  ██║   {CYAN}║
║   {GREEN}██████╔╝█████╗  ███████║███████║██╔██╗ ██║   {CYAN}║
║   {GREEN}██╔══██╗██╔══╝  ██╔══██║██╔══██║██║╚██╗██║   {CYAN}║
║   {GREEN}██║  ██║███████╗██║  ██║██║  ██║██║ ╚████║   {CYAN}║
║   {GREEN}╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   {CYAN}║
║                                                    ║
║                {YELLOW}REHAN Z4X 🫥               {CYAN}║
╠════════════════════════════════════════════════════╣
║  {MAGENTA}REHANZX TOOL v1.0                          {CYAN}║
║  {BLUE}INSTAGRAM ID  : rehan_z4x                    {CYAN}║
║  {GREEN}GITHUB        : github.com/rehanz4x          {CYAN}║
║  {YELLOW}TELEGRAM ID   : @mere_papa_0                {CYAN}║
║  {CYAN}TG CHANNEL     : @NETWORKXTG2               {CYAN}║
╚════════════════════════════════════════════════════╝
{RESET}
""")

# ========== START OLD TOOL ==========
def start_tool():
    loading("Starting Old Tool")
    if os.path.exists("rehanzx_old.py"):
        os.system("python rehanzx_old.py")
    else:
        print(f"{RED}[!] rehanzx_old.py file not found!{RESET}")
    input(f"\n{CYAN}Press Enter to return to menu...{RESET}")

# ========== CHECK UPDATE ==========
def check_update():
    loading("Checking for updates")
    os.system("git pull")
    print(f"{GREEN}[+] Update process complete!{RESET}")
    input(f"\n{CYAN}Press Enter to return to menu...{RESET}")

# ========== MAIN MENU ==========
def main():
    while True:
        banner()
        print(f"""{CYAN}
[1]{GREEN} Start Tool
[2]{YELLOW} Check Update
[3]{RED} Exit
""")

        choice = input(f"{YELLOW}Select Option >> {RESET}")

        if choice == "1":
            start_tool()
        elif choice == "2":
            check_update()
        elif choice == "3":
            clear()
            print(f"{RED}Exiting... Goodbye Bro 👋{RESET}")
            time.sleep(1)
            sys.exit()
        else:
            print(f"{RED}Invalid Option! Try Again...{RESET}")
            time.sleep(1)

# ========== RUN ==========
if __name__ == "__main__":
    main()
