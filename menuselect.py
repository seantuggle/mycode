#!/usr/bin/python3
"""I made this and I'm Sean. This is used to present a menu on the command line using a while loop."""

option_1 = "1. Walk the dog."
option_2 = "2. Eat lunch."
option_3 = "3. Launch all the missiles."
option_4 = "4. Quit."

lines = "*"*50

def show_menu():
    print(lines)
    print("Please make a selection from the following options")
    print(lines)
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    print(lines)

def main():
    show_menu()

if __name__ == "__main__": 
    main()

