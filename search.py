import os
import json
import asyncio
from truecallerpy import search_phonenumber
from colorama import Fore, Style

# ব্যানার তৈরি
def banner():
    os.system('clear')
    # Figlet ব্যবহার করে আপনার নাম দেওয়া ব্যানার
    os.system('figlet -f standard "Takbir Number Search"')
    print(f"{Fore.GREEN}           🕵️‍♂️  Verified Search Tool{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}="*50)

async def search_number():
    banner()
    print(f"{Fore.WHITE}Example: +8801XXXXXXXXX")
    number = input(f"\n{Fore.CYAN}Enter phone number: {Style.RESET_ALL}")
    
    # আপনার কন্ট্রি কোড (BD এর জন্য "BD")
    country_code = "BD"
    
    # এখানে আপনার লগিন সেশন থেকে তথ্য নেবে
    installation_id = "YOUR_INSTALLATION_ID" # এটি অটোমেটিক কাজ করবে যদি আপনি আগে লগিন করে থাকেন
    
    print(f"\n{Fore.YELLOW}[*] Searching in Database...{Style.RESET_ALL}")
    
    try:
        # সার্চ কমান্ড
        response = search_phonenumber(number, country_code, "YOUR_INSTALLATION_ID_HERE")
        
        # ডাটা প্রসেসিং
        data = response.get("data", [{}])[0]
        name = data.get("name", "Not Found")
        gender = data.get("gender", "Unknown")
        carrier = data.get("phones", [{}])[0].get("carrier", "Unknown")
        email = data.get("internetAddresses", [{}])[0].get("id") if data.get("internetAddresses") else "No Email"
        location = data.get("addresses", [{}])[0].get("city") if data.get("addresses") else "Unknown"

        print(f"\n{Fore.GREEN}✅ Results Found:")
        print(f"{Fore.WHITE}-------------------------")
        print(f"{Fore.BLUE}Name     : {Fore.YELLOW}{name}")
        print(f"{Fore.BLUE}Carrier  : {Fore.YELLOW}{carrier}")
        print(f"{Fore.BLUE}Location : {Fore.YELLOW}{location}")
        print(f"{Fore.BLUE}Email    : {Fore.YELLOW}{email}")
        print(f"{Fore.BLUE}Gender   : {Fore.YELLOW}{gender}")
        print(f"{Fore.WHITE}-------------------------")

    except Exception as e:
        print(f"{Fore.RED}Error: The number was not found please try again.")

if __name__ == "__main__":
    asyncio.run(search_number())
