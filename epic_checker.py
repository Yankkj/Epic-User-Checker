"""
EPIC USERNAME CHECKER v2.0
Created by Gon (GitHub: Yankkj)

DISCLAIMER:
This tool is for educational purposes only. 
Do not use it for any illegal or unethical activities.
The creator is not responsible for any misuse of this tool.
Please respect Epic Games' Terms of Service.
"""

import requests
import random
import string
import time
from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init()

class EpicUsernameChecker:
    def __init__(self):
        self.total_checked = 0
        self.available_found = 0
        self.start_time = time.time()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json'
        })
        
    def show_banner(self):
        """Display custom ASCII banner"""
        print(Fore.RED + r"""
   ██████╗  ██████╗ ███╗   ██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
  ██╔════╝ ██╔═══██╗████╗  ██║    ██╔════╝██╔════╝██╔══██╗████╗  ██║
  ██║  ███╗██║   ██║██╔██╗ ██║    ███████╗██║     ███████║██╔██╗ ██║
  ██║   ██║██║   ██║██║╚██╗██║    ╚════██║██║     ██╔══██║██║╚██╗██║
  ╚██████╔╝╚██████╔╝██║ ╚████║    ███████║╚██████╗██║  ██║██║ ╚████║
   ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
        """ + Style.RESET_ALL)
        print(Fore.RED + "="*60)
        print(f"{Fore.WHITE}CREATOR: {Fore.WHITE}Gon {Fore.WHITE}| GITHUB: {Fore.WHITE}Yankkj")
        print(f"{Fore.WHITE}VERSION: {Fore.WHITE}2.0 {Fore.WHITE}| {Fore.WHITE}EPIC GAMES USERNAME CHECKER")
        print(Fore.RED + "="*60 + Style.RESET_ALL)
        print()
    
    def generate_username(self, length_option, pronounceable=False):
        """Generate username based on selected options"""
        if pronounceable:
            return self._generate_pronounceable_username(length_option)
        
        if length_option == "4":
            length = 4
        elif length_option == "5":
            length = 5
        elif length_option == "6":
            length = 6
        elif length_option == "7":
            length = 7
        elif length_option == "4-5":
            length = random.choice([4, 5])
        elif length_option == "4-6":
            length = random.choice([4, 5, 6])
        elif length_option == "4-7":
            length = random.randint(4, 7)
        
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    
    def _generate_pronounceable_username(self, length_option):
        """Generate pronounceable usernames"""
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        
        if length_option == "4":
            patterns = ['CVCV', 'VCVC']
        elif length_option == "5":
            patterns = ['CVCVC', 'VCVCV']
        elif length_option == "6":
            patterns = ['CVCVCV', 'VCVCVC']
        elif length_option == "7":
            patterns = ['CVCVCVC', 'VCVCVCV']
        elif length_option == "4-5":
            patterns = ['CVCV', 'VCVC', 'CVCVC', 'VCVCV']
        elif length_option == "4-6":
            patterns = ['CVCV', 'VCVC', 'CVCVC', 'VCVCV', 'CVCVCV', 'VCVCVC']
        elif length_option == "4-7":
            patterns = ['CVCV', 'VCVC', 'CVCVC', 'VCVCV', 'CVCVCV', 'VCVCVC', 'CVCVCVC', 'VCVCVCV']
        
        pattern = random.choice(patterns)
        username = []
        
        for char in pattern:
            if char == 'V':
                username.append(random.choice(vowels))
            else:
                username.append(random.choice(consonants))
        return ''.join(username)
    
    def check_availability(self, username):
        """Check username availability on Epic Games"""
        url = f"https://www.epicgames.com/account/v2/personal/ajaxCheckDisplayName?displayName={username}"
        
        try:
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('available', False)
            return False
        except Exception as e:
            print(f"\n{Fore.RED}Error checking {username}: {str(e)}{Style.RESET_ALL}")
            return False
    
    def save_username(self, username):
        """Save available username to file"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('epic_usernames.txt', 'a', encoding='utf-8') as f:
            f.write(f"{username} - Found at: {timestamp}\n")
    
    def print_stats(self):
        """Show real-time statistics"""
        elapsed = time.time() - self.start_time
        rate = self.total_checked / elapsed if elapsed > 0 else 0
        print(
            f"\r{Fore.RED}Checked: {Fore.WHITE}{self.total_checked} {Fore.RED}| "
            f"Available: {Fore.WHITE}{self.available_found} {Fore.RED}| "
            f"Rate: {Fore.WHITE}{rate:.2f}/sec {Fore.RED}| "
            f"Time: {Fore.WHITE}{time.strftime('%H:%M:%S', time.gmtime(elapsed))}",
            end='', flush=True
        )
    
    def get_menu_option(self):
        """Display menu options"""
        print(f"\n{Fore.RED}LENGTH OPTIONS:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}1{Style.RESET_ALL} - 4 letters only")
        print(f"{Fore.WHITE}2{Style.RESET_ALL} - 5 letters only")
        print(f"{Fore.WHITE}3{Style.RESET_ALL} - 6 letters only")
        print(f"{Fore.WHITE}4{Style.RESET_ALL} - 7 letters only")
        print(f"{Fore.WHITE}5{Style.RESET_ALL} - 4-5 letters (random)")
        print(f"{Fore.WHITE}6{Style.RESET_ALL} - 4-6 letters (random)")
        print(f"{Fore.WHITE}7{Style.RESET_ALL} - 4-7 letters (random)")
        
        while True:
            choice = input(f"\n{Fore.WHITE}Select option (1-7): {Style.RESET_ALL}")
            if choice in ['1', '2', '3', '4', '5', '6', '7']:
                options = {
                    '1': '4',
                    '2': '5',
                    '3': '6',
                    '4': '7',
                    '5': '4-5',
                    '6': '4-6',
                    '7': '4-7'
                }
                return options[choice]
            print(f"{Fore.RED}Invalid option! Choose 1-7.{Style.RESET_ALL}")
    
    def run(self):
        """Run the checker"""
        self.show_banner()
        
        length_option = self.get_menu_option()
        pronounceable = input(f"\n{Fore.WHITE}Generate pronounceable names? (y/n): {Style.RESET_ALL}").lower() == 'y'
        
        print(f"\n{Fore.RED}Starting verification...{Style.RESET_ALL}\n")
        
        try:
            while True:
                username = self.generate_username(length_option, pronounceable)
                self.total_checked += 1
                
                if self.check_availability(username):
                    self.available_found += 1
                    self.save_username(username)
                    print(f"\n{Fore.WHITE}[+] {username.ljust(7)} AVAILABLE!{Style.RESET_ALL}")
                
                self.print_stats()
                
                delay = max(1, 3 - (self.available_found / 10))
                time.sleep(delay)
                
        except KeyboardInterrupt:
            print(f"\n\n{Fore.RED}Stopping checker...{Style.RESET_ALL}")
            print(f"\n{Fore.RED}Final summary:{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Total checked:{Style.RESET_ALL} {self.total_checked}")
            print(f"{Fore.WHITE}Available usernames found:{Style.RESET_ALL} {self.available_found}")
            if self.available_found > 0:
                print(f"{Fore.WHITE}Names saved to:{Style.RESET_ALL} 'epic_usernames.txt'")

if __name__ == "__main__":
    checker = EpicUsernameChecker()
    checker.run()