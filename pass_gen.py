import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols):
    """
    Generates a random password based on specified criteria.

    Args:
        length (int): The desired length of the password.
        include_lowercase (bool): True to include lowercase letters.
        include_uppercase (bool): True to include uppercase letters.
        include_digits (bool): True to include digits (0-9).
        include_symbols (bool): True to include common symbols.

    Returns:
        str: The generated password, or an error message if no character types are selected.
    """
    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        # Common symbols, you can customize this set
        characters += string.punctuation

    if not characters:
        return "Error: Please select at least one character type (lowercase, uppercase, digits, or symbols)."

    # Ensure the password contains at least one character from each selected type, if possible
    password = []
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_digits:
        password.append(random.choice(string.digits))
    if include_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random choices from all selected characters
    if length > len(password):
        for _ in range(length - len(password)):
            password.append(random.choice(characters))
    else:
        # If length is too short for all selected types, trim the initial password
        password = password[:length]

    # Shuffle the password list to randomize the order of characters
    random.shuffle(password)

    return "".join(password)

def run_password_generator():
    """Main function to run the password generator application."""
    print("--- Password Generator ---")

    while True:
        try:
            length = int(input("Enter desired password length (e.g., 12): "))
            if length <= 0:
                print("Password length must be a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number for length.")

    print("\nSelect character types to include (type 'yes' or 'no'):")
    include_lowercase = input("Include lowercase letters (a-z)? (yes/no): ").lower() == 'yes'
    include_uppercase = input("Include uppercase letters (A-Z)? (yes/no): ").lower() == 'yes'
    include_digits = input("Include numbers (0-9)? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols (!@#$%^&*)? (yes/no): ").lower() == 'yes'

    generated_pwd = generate_password(
        length,
        include_lowercase,
        include_uppercase,
        include_digits,
        include_symbols
    )

    print(f"\nGenerated Password: {generated_pwd}")
    print("------------------------\n")

if __name__ == "__main__":
    run_password_generator()
