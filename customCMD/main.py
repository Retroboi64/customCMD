import os
import sys
from colorama import init, Fore, Back, Style
import getpass
import tkinter as tk
from tkinter import messagebox
import socket
import fnmatch
import time
import uuid
import py_compile
import subprocess
import shutil
import socket
from settings import *
import random
import requests


# Initialize colorama
init()

# Your ASCII art banner
banner = f"""
{Fore.RED}
  ▄▄· ▄• ▄▌.▄▄ · ▄▄▄▄▄      • ▌ ▄ ·.      ▄▄· • ▌ ▄ ·. ·▄▄▄▄  
 ▐█ ▌▪█▪██▌▐█ ▀. •██  ▪     ·██ ▐███▪    ▐█ ▌▪·██ ▐███▪██▪ ██ 
 ██ ▄▄█▌▐█▌▄▀▀▀█▄ ▐█.▪ ▄█▀▄ ▐█ ▌▐▌▐█·    ██ ▄▄▐█ ▌▐▌▐█·▐█· ▐█▌
 ▐███▌▐█▄█▌▐█▄▪▐█ ▐█▌·▐█▌.▐▌██ ██▌▐█▌    ▐███▌██ ██▌▐█▌██. ██ 
 ·▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀    ·▀▀▀ ▀▀  █▪▀▀▀▀▀▀▀▀• 
 BY Retroboi64
________________________________________________________________
{Fore.RESET}

{Fore.CYAN}||{Fore.RESET}For help, type {Fore.YELLOW}help{Fore.CYAN}||{Fore.RESET}
{Fore.CYAN}||{Fore.RESET}Example command, type {Fore.YELLOW}custom{Fore.CYAN}||{Fore.RESET}
\n
"""

def Example_command():
    print("\n")
    print("Make them in custom commands editor!\n Not made yet just use vscode or notepad.\n")
    print("\n")

def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def help_command():
    print("\n")
    print("CustomCmd Help:")
    print("\n")
    print(f"{Fore.CYAN}Command            Description{Fore.RESET}")
    print(f"{'-' * 50}")
    print(f"{'help':<20}Display this help message")
    print(f"{'clear':<20}Clear the screen")
    print(f"{'custom':<20}An example of a custom command")
    print(f"{'cd':<20}to change the current directory")
    print(f"{'exit':<20}Quit CustomCmd")
    print(f"{'all':<20} To display all commands")
    print(f"{'date':<20}To show the current date")
    print(f"{'ip':<20}To show your computer's IP address")
    print(f"{'calculator':<20}It calculates numbers")
    print(f"{'ver':<20}To display version of CustomCmd")
    print(f"{'qr':<20}make a QR code")
    print("For all commands, type 'all'")
    print("\n")
    print(f"{'________________________':<20}")
    print(f"{' Add your own below':<20}")
    print(f"{'------------------------':<20}")
    print("\n")
    print(f"{'<your-command>':<20}Add your custom commands here")
    print(f"{'<script.py>':<20}Run a Python script (e.g., my_script.py)")
    print("\n")


def main():
    clear_screen()
    print(banner)  # Print the banner at the beginning of the custom command prompt
    while True:
        username = getpass.getuser()
        computername = os.environ['COMPUTERNAME']
        current_directory = os.getcwd()

        # Customize the prompt format using ANSI escape codes
        prompt = f"{Fore.LIGHTWHITE_EX}╔══{Fore.RESET}({Fore.LIGHTGREEN_EX}{username}{Fore.RESET}@{Fore.LIGHTMAGENTA_EX}{computername}{Fore.RESET})-[{Fore.LIGHTRED_EX}{current_directory}{Fore.RESET}]> "
        
        user_input = input(prompt)
        
        if user_input == "exit":
            break
        elif user_input in commands:
            commands[user_input]()
        elif user_input.endswith(".py"):
            run_python_script(user_input)

        elif user_input.endswith(".pyw"):
            run_python_script(user_input)    

        else:
            print(f"{Fore.RED}Command not recognized. Type 'help' for assistance.{Fore.RESET}")

def exit():
    print(f"{Fore.RED}Exiting CustomCmd...{Fore.RESET}")
    sys.exit()

def run_python_script(script_name):
    try:
        exec(open(script_name).read())
    except FileNotFoundError:
        print(f"{Fore.RED}File not found.{Fore.RESET}")

def change_directory():

    new_directory = input("Enter the directory path: ")

    try:
        os.chdir(new_directory)  # Change the current working directory
        print(f"Current directory changed to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory not found: {new_directory}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def all_commands():
    print("\n")
    print(f"{Fore.CYAN}Commands:{Fore.RESET}")
    print(f"{'-' * 50}")
    for command in commands:
        print(f"{command:<20}{commands[command]}")
    print("\n")
    print(f"{'________________________':<20}")
    pass

def date():
    from datetime import date
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    print("Today's date is:", d2)


def ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    hostname = socket.gethostname()
    s.close()
    print(f"Your computer's hostname is: {hostname}")
    print(f"Your computer's IP address is: {ip}")

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print("Result: " + str(result))
    elif choice == '2':
        result = num1 - num2
        print("Result: " + str(result))
    elif choice == '3':
        result = num1 * num2
        print("Result: " + str(result))
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print("Result: " + str(result))
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid input")



def ver():
    ver = "0.3"
    print(f"{Fore.CYAN}Version: {ver}{Fore.RESET}")
    print("(C) 2023 Retroboi64, All Rights Reserved.")



def roll_dice():
    return random.randint(1, 6)


def get_joke():
    jokes = ["Why did the scarecrow win an award? Because he was outstanding in his field!", "Why don't scientists trust atoms? Because they make up everything!"]
    return random.choice(jokes)



import qrcode

def generate_qr_code():
    """Generate a QR code"""
    print("This is were it well generate a QR code in this path: ", os.getcwd())
    file_name = input("Enter the file name: ")
    data = input("Enter the url or data: ")
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)



# debug commands
def debug_error_1():
    messagebox.showerror("Error", "This is a test error.")
    pass
     

#custem commands

# All commands
commands = {
    # built-in commands
    "help": help_command,
    "clear": clear_screen,
    "custom": Example_command,
    "exit": exit,
    "cd": change_directory,
    "all": all_commands,
    "date": date,
    "ip": ip,
    "calculator": calculator,
    "ver": ver,
    "roll dice": roll_dice,
    "get joke": get_joke,
    "qr": generate_qr_code,
    #debug commands
    "debug_error_1": debug_error_1,
    #custom commands
}


if __name__ == "__main__":
 main()
