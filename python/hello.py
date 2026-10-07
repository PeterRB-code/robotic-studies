# Ask user for name (not validated)
def get_name():
    return input("Whats your name? ")
    

# Say hello to user
def say_hallo(name):
    print(f"Hello {name}")


# Get name and print it
def main():
    name = get_name()
    say_hallo(name)

main()