
# This program takes a string as argument and ensures that all the chars in it, will be lowercase
def main():
    input_string = get_input_string()
    low_input_string = make_low_input_string(input_string)
    show_low_input_string(low_input_string)

# Get hold of a string from user
def get_input_string():
    return input("Please enter some CAPITALIZED chars and press enter: ")

# Make chars in the string the user provided into lowercase
def make_low_input_string(input_string):
    return input_string.lower()

# Print the string with lowercase chars onto the screen
def show_low_input_string(low_input_string):
    print(low_input_string)


main()