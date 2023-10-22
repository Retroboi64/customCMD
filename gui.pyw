import os
import sys
from colorama import init, Fore
import tkinter as tk
from tkinter import Text, Scrollbar, Entry, Button

# Initialize colorama
init()

class CustomCmdApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CustomCmd GUI")
        
        self.setup_gui()
        self.commands = {
            "help": self.help_command,
            "clear": self.clear_screen,
            "custom": self.example_command,
            "exit": self.exit,
        }

    def setup_gui(self):
        banner_text = """
        
 ██████ ██    ██ ███████ ████████  ██████  ███    ███      ██████ ███    ███ ██████  
██      ██    ██ ██         ██    ██    ██ ████  ████     ██      ████  ████ ██   ██ 
██      ██    ██ ███████    ██    ██    ██ ██ ████ ██     ██      ██ ████ ██ ██   ██ 
██      ██    ██      ██    ██    ██    ██ ██  ██  ██     ██      ██  ██  ██ ██   ██ 
 ██████  ██████  ███████    ██     ██████  ██      ██      ██████ ██      ██ ██████  
                                                                                                                                                                                                                                                                                                                                            
        BY Retroboi64
        For help, type help
        Example command, type custom
        """
        
        self.banner_label = tk.Label(root, text=banner_text, justify="left", anchor="w", font=("Courier", 14))
        self.banner_label.pack(fill="x")
        
        self.output_text = Text(root, wrap="word", height=10, width=80)
        self.output_text.pack()
        self.scrollbar = Scrollbar(root, command=self.output_text.yview)
        self.output_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        
        self.input_entry = Entry(root, width=80)
        self.input_entry.pack()
        
        self.submit_button = Button(root, text="Submit", command=self.handle_command)
        self.submit_button.pack()

    def handle_command(self):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        self.output_text.insert(tk.END, f"CustomCmd> {user_input}\n")
        
        if user_input == "exit":
            self.exit()
        elif user_input in self.commands:
            self.commands[user_input]()
        elif user_input.endswith(".py"):
            self.run_python_script(user_input)
        else:
            self.output_text.insert(tk.END, "Command not recognized. Type 'help' for assistance.\n")
        
    def help_command(self):
        help_text = """
        CustomCmd Help:

        Command            Description
        --------------------------------------------------
        help               Display this help message
        clear              Clear the screen
        custom             An example of a custom command
        exit               Quit CustomCmd

        ---------------- Add your own below ----------------

        <your-command>     Add your custom commands here
        <script.py>        Run a Python script (e.g., my_script.py)
        """
        self.output_text.insert(tk.END, help_text)
    
    def clear_screen(self):
        self.output_text.delete("1.0", tk.END)
    
    def example_command(self):
        self.output_text.insert(tk.END, "Make them in custom commands editor!\nNot made yet just use vscode or notepad.\n")

    def exit(self):
        self.root.destroy()
    
    def run_python_script(self, script_name):
        try:
            os.system(f"python {script_name}")
        except Exception as e:
            self.output_text.insert(tk.END, f"Error running script: {e}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomCmdApp(root)
    root.mainloop()
