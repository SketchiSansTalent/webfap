import requests
from bs4 import BeautifulSoup
import socket
import whois
import time
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(rf"""{Fore.MAGENTA}
.______   ____    ____                                              
|   _  \  \   \  /   /                                              
|  |_)  |  \   \/   /                                               
|   _  <    \_    _/                                                
|  |_)  |     |  |                                                  
|______/      |__|                                                  
                                                                    
     _______. __  ___  _______ .___________.  ______  __    __   __ 
    /       ||  |/  / |   ____||           | /      ||  |  |  | |  |
   |   (----`|  '  /  |  |__   `---|  |----`|  ,----'|  |__|  | |  |
    \   \    |    <   |   __|      |  |     |  |     |   __   | |  |
.----)   |   |  .  \  |  |____     |  |     |  `----.|  |  |  | |  |
|_______/    |__|\__\ |_______|    |__|      \______||__|  |__| |__|
            {Style.RESET_ALL}""")
    print(f"{Fore.CYAN}[ + ]If you need help or have a question (add me on discord)-> sketchi_i{Style.RESET_ALL}")

def whatweb(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error during the request : {e}{Style.RESET_ALL}")
        return

    status_code = response.status_code
    server = response.headers.get('Server', 'Inconnu')
    cookies = response.cookies
    x_powered_by = response.headers.get('X-Powered-By', 'Inconnu')
    title = BeautifulSoup(response.text, 'html.parser').title.string if BeautifulSoup(response.text, 'html.parser').title else 'Inconnu'

    ip = socket.gethostbyname(url.split('/')[2])
    country = get_country_from_ip(ip)

    if 'PHP' in x_powered_by:
        php_version = x_powered_by.split('PHP/')[-1]
    else:
        php_version = 'Inconnu'

    print(f"{Fore.GREEN}{url} [{status_code} OK]{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Apache[{server}]{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Cookies[{', '.join([cookie.name for cookie in cookies])}]{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Country[{country}]{Style.RESET_ALL}")
    print(f"{Fore.CYAN}HTML5{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}HTTPServer[Debian Linux][{server}]{Style.RESET_ALL}")
    print(f"{Fore.BLUE}IP[{ip}]{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}PHP[{php_version}]{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Script{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Title[{title}]{Style.RESET_ALL}")
    print(f"{Fore.BLUE}X-Powered-By[{x_powered_by}]{Style.RESET_ALL}")

def get_country_from_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        return f"{data['country']}[{data['countryCode']}]"
    except:
        return "Inconnu"

if __name__ == "__main__":
    banner()
    url = input(f"{Fore.YELLOW}Enter the URL of the site to scan: {Style.RESET_ALL}")
    whatweb(url)
    time.sleep(10)