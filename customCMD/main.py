import os
import sys
from colorama import init, Fore, Back, Style
import getpass
import tkinter as tk
from tkinter import messagebox

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
    #debug commands
    "debug_error_1": debug_error_1,
    #custom commands
}


if __name__ == "__main__":
 main()
