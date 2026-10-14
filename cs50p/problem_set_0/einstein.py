# Calculate mass to energy using Einsteins E=mc^2
def main():
    mass = get_user_input()
    energy = calculate_energy(mass)
    print_mass_and_calculated_result(mass, energy)

def get_user_input():
    """Take mass (integer) as user input. Do not validate input, assume correct"""
    return int(input("Type the mass in kilograms you wish to have converted to Kilo Joules and press ENTER: "))

def calculate_energy(mass):
    """Make calculation to energi in Joules (Giga Joules) e=mc^2 (e= energy m= mass c = speed of light km/s)"""
    return 30_000_000**2*mass/100_000_000

def print_mass_and_calculated_result(mass, energy):
    """Print the outcome"""
    print(f"Mass(kg) = {mass}")
    print(f"Energy(GJ) = {energy:,.0f}")


if __name__ == "__main__":
    main()