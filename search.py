import os
import time
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

def banner():
    os.system('clear')
    os.system('figlet -f standard "Takbir Number Search" | lolcat 2>/dev/null || figlet "Takbir Number Search"')
    print(f"{Fore.GREEN}🕵️‍♂️  Welcome to Takbir Number Search Tool{Style.RESET_ALL}")
    print("-" * 45)

def search_number(phone):
    print(f"\n{Fore.YELLOW}[*] Searching for: {phone}...{Style.RESET_ALL}")
    
    # এটি গুগল সার্চের মাধ্যমে পাবলিক ডেটা খোঁজার চেষ্টা করবে
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    query = f"site:truecaller.com OR site:facebook.com \"{phone}\""
    url = f"https://www.google.com/search?q={query}"
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        results = soup.find_all('h3')
        
        if results:
            print(f"\n{Fore.CYAN}[+] Potential Information Found:{Style.RESET_ALL}")
            for i, result in enumerate(results[:3]):
                print(f"{Fore.WHITE}{i+1}. {result.get_text()}")
        else:
            print(f"\n{Fore.RED}[!] No direct public information found without login.")
            print(f"{Fore.YELLOW}[ Tip: Truecaller now requires official login to show private details. ]")
            
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")

banner()
print(f"{Fore.WHITE}Example: +88017XXXXXXXX")
phone_number = input(f"\n{Fore.BLUE}Enter phone number: {Style.RESET_ALL}")

if phone_number:
    search_number(phone_number)
else:
    print("Invalid Input!")
