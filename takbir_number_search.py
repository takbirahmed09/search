import requests
from bs4 import BeautifulSoup
from figlet import Figlet
import re

def print_figlet(text):
    f = Figlet(font='standard')
    print(f.renderText(text))

def search_truecaller(phone_number):
    url = f"https://www.truecaller.com/search/{phone_number}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        name = soup.find('h1', class_='name')
        location = soup.find('div', class_='location')
        if name and location:
            print(f"Name: {name.text.strip()}")
            print(f"Location: {location.text.strip()}")
        else:
            print("Unable to find information.")
    else:
        print("Failed to retrieve information.")

def main():
    print_figlet("Takbir Number 🕵️‍♂️ Search")
    print("Example: +880**********")
    print("Enter phone number: ", end="")
    phone_number = input().strip()

    if re.match(r'^\+\d{10,15}$', phone_number):
        search_truecaller(phone_number)
    else:
        print("Invalid phone number format. Please enter a valid number.")

if __name__ == "__main__":
    main()
