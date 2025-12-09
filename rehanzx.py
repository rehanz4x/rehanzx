#!/usr/bin/env python
import requests
import pyfiglet
import os
import re
import uuid
from datetime import datetime
from rich.console import Console

try:
    import requests
except ImportError:
    os.system("pip install requests")

try:
    from rich.console import Console
except ImportError:
    os.system("pip install rich")

MAGENTA = "\033[1m\033[35m"
GREEN = "\033[1m\033[32m"
YELLOW = "\033[1m\033[33m"
RED = "\033[1m\033[31m"
BLUE = "\033[1m\033[34m"
CYAN = "\033[1m\033[36m"
WHITE = "\033[1m\033[37m"
ORANGE = "\033[1m\033[38;5;208m"
RESET = "\033[0m"

UID = str(uuid.uuid4())
console = Console()

def display_header():
    os.system("cls" if os.name == 'nt' else "clear")

    print(f"""
\033[38;5;213m╔══════════════════════════════════════════════════════╗
\033[38;5;213m                                                      
\033[38;5;213m   \033[96m{pyfiglet.figlet_format("REHAN").rstrip()}   \033[38;5;213m
\033[38;5;213m                                                      
\033[38;5;213m        \033[38;5;213mREHAN IG REPORT • Premium Tool   \033[38;5;213m
\033[38;5;213m                                                     
\033[38;5;213m  \033[38;5;203m👑 OWNER   \033[1;90m: \033[1;37m@rehan_z4x         \033[38;5;213m
\033[38;5;213m  \033[38;5;203m💌 INSTGRAM ID  \033[1;90m: \033[1;37m@rehan_z4x         \033[38;5;213m
\033[38;5;213m  \033[38;5;81m🛠 TOOL    \033[1;90m: \033[1;37mINSTAGRAM REPORT TOOL VIP \033[38;5;213m
\033[38;5;213m  \033[38;5;75m📢 TELEGRAM ID \033[1;90m: \033[1;37m@mere_papa_0       \033[38;5;213m
\033[38;5;213m  \033[38;5;119m🔢 VERSION \033[1;90m: \033[1;37m7.1                      \033[38;5;213m
\033[38;5;213m  \033[38;5;220m💎 TYPE    \033[1;90m: \033[1;32mFREE         \033[38;5;213m
\033[38;5;213m                                                     
\033[38;5;213m╚══════════════════════════════════════════════════════╝
\033[0m""")
def report_instagram(target_id, sessionid, csrftoken):
    display_header()
    
    print(f"""
{CYAN} _____________________________
|                             | 
| {YELLOW}~${MAGENTA} choose the report        |
|_____________________________|

------------------------------
| {GREEN}1 ~ {YELLOW}spam                  |
------------------------------
| {GREEN}2 ~ {YELLOW}self                  |
------------------------------
| {GREEN}3 ~ {YELLOW}sale                  |
------------------------------
| {GREEN}4 ~ {YELLOW}Nudity              |
------------------------------
| {GREEN}5 ~ {YELLOW}violence              |
------------------------------
| {GREEN}6 ~ {YELLOW}hate                  |
------------------------------
| {GREEN}7 ~ {YELLOW}harassment            |
------------------------------
| {GREEN}8 ~ {YELLOW}instagram             |
------------------------------
| {GREEN}9 ~ {YELLOW}instagram business    |
------------------------------
| {GREEN}10 ~ {YELLOW}copyright            |
------------------------------
| {GREEN}11 ~ {YELLOW}Impression 3 business                  
------------------------------
| {GREEN}12 ~ {YELLOW}Impression 3 instagram                  
------------------------------
| {GREEN}13 ~ {YELLOW}Impression 4 business                   
------------------------------
| {GREEN}14 ~ {YELLOW}Impression 4 instagram                  
------------------------------
| {GREEN}15 ~ {YELLOW}Violence 1               
------------------------------
""")

    try:
        report_type = int(input("-> type number (1-15): "))
        if report_type > 15 or report_type < 1:
            print("wrong number\ntry again")
            return
        else:
            print(f"You chose report type {report_type}.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    while True:
        try:
            response = requests.post(
                f"https://i.instagram.com/users/{target_id}/flag/",
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
                    "Host": "i.instagram.com",
                    'cookie': f"sessionid={sessionid}",
                    "X-CSRFToken": csrftoken,
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                },
                data=f'source_name=&reason_id={report_type}&frx_context=',
                allow_redirects=False
            )
            if response.status_code == 429:
                console.print(f"- Ban with status code [ {response.status_code} ] ")
                exit()
            elif response.status_code == 500:
                console.print(f"- Target Not Found with status code [ {response.status_code} ] ")
                exit()
            else:
                console.print(f"- Report Done with status code [ {response.status_code} ] ")
        except requests.exceptions.TooManyRedirects:
            console.print(f"- Report Done with status code [ {response.status_code} ] ")
        except Exception as e:
            console.print(f"- Report Failed with status code [ {response.status_code} ] ")
            exit()

def start_process():
    username = input(f"{GREEN}[+] USERRNAME :{RESET}{CYAN} @")
    if not username:
        console.print("[!] You must write The user")
        exit()
    password = input(f"{GREEN}[+] PASSWD :{RESET} ")
    if not password:
        console.print("[!] You must write The password")
        exit()
    
    login_response = requests.post(
        'https://i.instagram.com/api/v1/accounts/login/',
        headers={
            'User-Agent': 'Instagram 114.0.0.38.120 Android (30/3.0; 216dpi; 1080x2340; huawei/google; Nexus 6P; angler; angler; en_US)',
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-Connection-Type": "WIFI",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Host': 'i.instagram.com'
        },
        data={
            '_uuid': UID,
            'password': password,
            'username': username,
            'device_id': UID,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_count': '0'
        },
        allow_redirects=True
    )
    
    if 'logged_in_user' in login_response.text:
        console.print("- Login Done [bold green]succ_Login[/bold green] ")
        sessionid = login_response.cookies['sessionid']
        csrftoken = login_response.cookies['csrftoken']
        target = input("- Target username : ")
        
        lookup_response = requests.post(
            'https://i.instagram.com:443/api/v1/users/lookup/',
            headers={
                "Connection": "close",
                "X-IG-Connection-Type": "WIFI",
                "mid": "XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq",
                "X-IG-Capabilities": "3R4=",
                "Accept-Language": "ar-sa",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Instagram 99.4.0 TweakPY_vv1ck (TweakPY_vv1ck)",
                "Accept-Encoding": "gzip, deflate"
            },
            data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % target}
        )
        
        if 'No users found' in lookup_response.text:
            adv_search = requests.get(
                f'https://www.instagram.com/{target}',
                headers={
                    'Host': 'www.instagram.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Connection': 'keep-alive',
                    'Cookie': f'csrftoken={csrftoken}',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-User': '?1',
                    'TE': 'trailers'
                }
            )
            try:
                target_id = re.findall('"profile_id":"(.*?)"', adv_search.text)[0]
                report_instagram(target_id, sessionid, csrftoken)
            except IndexError:
                try:
                    target_id = re.findall('"page_id":"profilePage_(.*?)"', adv_search.text)[0]
                    report_instagram(target_id, sessionid, csrftoken)
                except IndexError:
                    try:
                        adv_search2 = requests.get(
                            f'https://www.instagram.com/api/v1/users/web_profile_info/?username={target}',
                            headers={
                                'Host': 'www.instagram.com',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
                                'Accept': '*/*',
                                'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                                'Accept-Encoding': 'gzip, deflate, br',
                                'X-CSRFToken': csrftoken,
                                'X-IG-App-ID': '936619743392459',
                                'X-ASBD-ID': '198387',
                                'X-IG-WWW-Claim': 'hmac.AR3KPEPoXkWYhwtoCUKyUHK80GsE1g2PJI1uPtDlCyo4PHKn',
                                'X-Requested-With': 'XMLHttpRequest',
                                'Alt-Used': 'www.instagram.com',
                                'Connection': 'keep-alive',
                                'Referer': f'https://www.instagram.com/{target}/',
                                'Cookie': f'sessionid={sessionid}',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Mode': 'cors',
                                'Sec-Fetch-Site': 'same-origin',
                                'TE': 'trailers'
                            }
                        )
                        target_id = adv_search2.json()['data']['user']['id']
                        report_instagram(target_id, sessionid, csrftoken)
                    except KeyError:
                        console.print('\n- [bold red]Failed[/bold red] to get target username, Try entering the Target ID manually .\n')
                        target_id = input('- Enter The Target ID : ')
                        report_instagram(target_id, sessionid, csrftoken)
        elif '"spam":true' in lookup_response.text:
            console.print("- Try again Later !")
            exit()
        else:
            try:
                target_id = str(lookup_response.json()['user_id'])
                report_instagram(target_id, sessionid, csrftoken)
            except KeyError:
                console.print('- General [bold red]Error[/bold red] ...')
                exit()
    
    elif 'ip_block' in login_response.text:
        console.print("- You Have [bold red]banned[/bold red] from Instagram ( [bold red]ip block[/bold red] ) !")
        exit()
    elif 'The password you entered is incorrect' in login_response.text:
        console.print("- Please check Your Password !")
        exit()
    elif "Please check your username and try again." in login_response.text:
        console.print("- username Not Found !")
        exit()
    elif 'two_factor_required' in login_response.text:
        console.print("- [bold orange3]Two Factor[/bold orange3] ! ...")
        exit()
    elif 'challenge_required' in login_response.text:
        console.print("- [bold orange3]Secure[/bold orange3] Account ! ...")
        exit()
    elif 'inactive user' in login_response.text:
        console.print('- This user is [bold red]banned[/bold red] from Instagram ...')
        exit()
    elif "We're working on it and we'll get it fixed as soon as we can." in login_response.text:
        console.print("- Try again in a minute !")
        exit()
    elif 'Please wait a few minutes before you try again' in login_response.text:
        console.print("- Try again in a minute !")
        exit()
    elif 'Bad request' in login_response.text:
        console.print("- [bold red]Error[/bold red] in instagram, try again in 15 minutes ...")
        exit()
    elif 'Invalid Parameters' in login_response.text:
        console.print("- [bold red]Error[/bold red] Please Reinstall The Tool From The original Source ... ")
        exit()
    else:
        console.print('- General [bold red]Error[/bold red] ...')
        exit()

if __name__ == "__main__":
    display_header()
    start_process()