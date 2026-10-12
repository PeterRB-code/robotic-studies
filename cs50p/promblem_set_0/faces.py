def main():
    emoticon_string = get_emoticon_string()
    converted_string = convert_string(emoticon_string)
    print_the_result(converted_string)

def get_emoticon_string():
    return input("Type a short string and also use either :) or :( and press ENTER: ")

def convert_string(emoticon_string):
    return emoticon_string.replace(":)", "🙂").replace(":(", "🙁")

def print_the_result(string_to_print):
    print(string_to_print)


main()