import random
import string

def is_valid_password(password, use_uppercase, use_digits, use_special):
    # Check if the password meets the complexity requirements
    if use_uppercase and not any(c.isupper() for c in password):
        return False
    if use_digits and not any(c.isdigit() for c in password):
        return False
    if use_special and not any(c in string.punctuation for c in password):
        return False
    return True

def generate_password(length, use_uppercase, use_digits, use_special):
    # Define the character sets to use for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_characters = string.punctuation if use_special else ''

    # Combine all character sets based on user preferences
    all_characters = lowercase + uppercase + digits + special_characters

    # Ensure at least one character from each selected set is included
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special_characters))

    # Fill the rest of the password length with random choices from all characters
    if length > len(password):
        password += random.choices(all_characters, k=length - len(password))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")

    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 8): "))
            if length < 8:
                print("Password length should be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Prompt the user for complexity options
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Ensure at least one character set is selected
    if not (use_uppercase or use_digits or use_special):
        print("You must select at least one character set (uppercase, digits, special characters).")
        return

    # Ask the user if they want to provide a password
    provide_password = input("Do you want to provide a password? (y/n): ").strip().lower()
    if provide_password == 'y':
        user_password = input("Enter your password: ")
        if len(user_password) != length:
            print(f"Password must be exactly {length} characters long.")
        elif is_valid_password(user_password, use_uppercase, use_digits, use_special):
            print("Your provided password is accepted.")
            print("Generated Password:", user_password)
        else:
            print("Your provided password does not meet the complexity requirements.")
            print("Generating a new password...")
            password = generate_password(length, use_uppercase, use_digits, use_special)
            print("Generated Password:", password)
    else:
        # Generate the password
        password = generate_password(length, use_uppercase, use_digits, use_special)
        print("Generated Password:", password)

if __name__ == "__main__":
    main()