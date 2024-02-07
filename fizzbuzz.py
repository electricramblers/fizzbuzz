import os
from termcolor import colored
from datetime import datetime
import traceback


class FizzBuzz:
    def __init__(self, limit=100):
        self.limit = limit

    def fizz_buzz(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return str(number)

    def print_fizz_buzz(self):
        for number in range(1, self.limit + 1):
            print(colored(self.fizz_buzz(number), "green"))


def main():
    os.system("clear")
    print(colored(str(datetime.now()), "yellow"))
    print(colored("Welcome to FizzBuzz!", "red"))

    def fizz_something():
        fizz_buzz = FizzBuzz(limit=100)
        fizz_buzz.print_fizz_buzz()
        fizz_buzz.method()

    try:
        fizz_sommething()
    except AttributeError as e:
        print(colored("Something went wrong. Please try again later.", "red"))
        print(colored("Traceback:", "red"))
        traceback.print_exc()


if __name__ == "__main__":
    main()
