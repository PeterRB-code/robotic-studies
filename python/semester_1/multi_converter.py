

# The fantastic Multi Converter program
# Converts angles and lengths
import sys
import os
import subprocess


def main():
    minimum, maximum, variable_kind, user_input_text = user_choice()
    choice = get_and_validate_user_input(minimum, maximum, variable_kind, user_input_text)
    if choice == 0:
        print("Bye Bye")
        sys.exit()
    elif choice == 1:
        print()






def clear_screen():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

def get_user_input(user_input_text):
    return input(user_input_text)


def get_and_validate_user_input(minimum, maximum, variable_kind, user_input_text):
    clear_screen()
    for counter in range(3):
        user_input = get_user_input(user_input_text)
        
        if variable_kind == "integer":
            try:
                choice = int(user_input)
            except ValueError:
                user_input_text = (f"{choice} is not an integer. Please enter 0, 1 or 2: ")
                continue
            if minimum <= choice <= maximum:
                break
            else:
                user_input_text = (f"{choice} is out of range. Please enter 0, 1 or 2: ")   
                continue

        elif variable_kind == "float":
            try:
                choice = float(user_input)
            except ValueError:
                user_input_text = ("Please type a number that is rational.")
                continue
            break


def user_choice():
    minimum = 0
    maximum = 2
    variable_kind = "integer"
    user_input_text = ("Welcome to the Fantasic MULTI CONVERTER.\nHere you have the choice of getting angles or lengths converted \n "
    "For conversion between angles (radians <-> degrees) enter 1 \n"
    "For conversion between lengths (centimeters <-> inches) enter 2 \n"
    "Or if some strange reason you want to quit enter 0: ")
    return minimum, maximum, variable_kind, user_input_text
    

main()

