from clint.textui import colored, puts, indent
from pyfiglet import Figlet
from os import system, name
from datetime import datetime
from time import sleep
from random import randint

class Calc:
    def __init__(self):
        self.running = True
        self.response = None

    def stop(self):
        self.running = False

    def await_action(self):
        input("\nPress enter to continue...")

    def clear(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def print_success(self, t):
        puts(colored.green(t))
        sleep(1)

    def print_error(self, t):
        puts(colored.red(t))
        sleep(1) 

    def menu(self, title, options):
        self.clear()

        result = Figlet()
        print(colored.yellow(result.renderText(title)))

        for i in range(len(options)):
            with indent(3, quote=">"):
                puts(f"{i}. -> {options[i]}")

    def get_response(self, options):
        now = datetime.now().strftime("%H:%M:%S")

        try:
            self.response = int(input(f"\n({now}) - R: "))
        except:
            self.response = randint(len(options), len(options) + 1)

        if options.index("Quit") == self.response:
            self.stop()
        else:
            if self.response <= len(options) - 1:
                return self.response

            else:
                self.print_error("Invalid option...")
                return -1