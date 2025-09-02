import pathlib
from ascii import ascii_art


print(ascii_art)
user = input("Welcome to PySort. Type \"start\" or \"s\" to iniate the Script.\nUser: ").lower().strip()
if user == "start" or user == "s":
    print("Lets go")