import random
import string

def generate_password():
    print("Welcome to the Strong Password Generator!")
    
    while True:
        length_input = input("Enter desired password length (8-20): ")
        if length_input.isdigit():
            length = int(length_input)
            if 8 <= length <= 20:
                break
            else:
                print("Password length should be between 8 and 20.")
        else:
            print("Please enter a valid number.")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password list & convert to string
    random.shuffle(password)
    password = ''.join(password)

    print(f"Your strong password is: {password}")

# Run
generate_password()
