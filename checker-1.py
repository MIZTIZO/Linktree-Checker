import requests
import random
import time
from colorama import *


def get_random_word():
    word_site = "https://web.mit.edu/~mkgray/jik/src/Attic/kerberos_password_hacker/baldwin.words"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    word = random.choice(WORDS)
    word = word.decode("utf-8")
    word = word.lower()
    return word

def banner():
 word = get_random_word()
 
 try:
  check = requests.get("https://linktr.ee/"+word)
  if check.status_code == 429:
    print(Fore.RED+"[!] Rate Limited! Waiting 5 Seconds! if you are getting this error multiple times use other version of this checker")
    time.sleep(5)
  if check.status_code == 404:
   print(Fore.GREEN+"[+] "+Fore.WHITE+"https://linktr.ee/"+word)
  else:
    print(Fore.RED+"[-] "+Fore.WHITE+"https://linktr.ee/"+word)
 except:
   print("error")
while True:
  banner()
