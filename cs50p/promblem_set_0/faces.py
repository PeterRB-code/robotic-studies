def main():
    # Aske the user for text. Convert happy and sad emoticons to emojis, then print result
    emoticon_string = get_emoticon_string()
    converted_string = convert_string(emoticon_string)
    print_the_result(converted_string)

def get_emoticon_string():
    """Prompt the user for a string and return it as typed."""
    return input("Type a short string and also use either :) or :( and press ENTER: ")

def convert_string(emoticon_string):
    """
    Return the input with :) swapped for 🙂 and :( swapped for 🙁.
    All other text is returned unchanged.
    """
    return emoticon_string.replace(":)", "🙂").replace(":(", "🙁")

def print_the_result(string_to_print):
    """Print the given string (kept separate so it's easy to reuse)."""
    print(string_to_print)


main()