# Take user input and replace white space with ... (3 dots)
def main():
    text_string_quick = get_user_text()
    text_string_slow = make_text_slow(text_string_quick)
    show_slow_text(text_string_slow)

# Get the text from the user
def get_user_text():
    return input("Please type a short text and press ENTER: ")

# Replace whitespaces in the text string passed with ... (3 dots)
def make_text_slow(text_string_quick):
    return text_string_quick.replace(" ", "...")

# Print the slow text
def show_slow_text(text_string_slow):
    print(text_string_slow)


main()