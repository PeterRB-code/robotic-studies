def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """Remove $ at the start of string"""
    return float(d.removeprefix("$"))


def percent_to_float(p):
    """Remove % at end of string and make amount into decimal"""
    return float(p.removesuffix("%"))/100


if __name__ == "__main__":
    main()