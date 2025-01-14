import random
import string
import re

def generate_random_password(password_length):
    # Ensure the password length is within the valid range
    while password_length < 8 or password_length > 64:
        print("Invalid length. Password length must be between 8 and 64.")
        password_length = int(input("\nEnter a valid length for the random password (between 8 and 64): "))
    
    # Define the character set for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password by selecting characters from the defined set
    password = ''.join(random.choice(all_characters) for i in range(password_length))
    
    # Categorize the characters used
    numbers = ''.join([c for c in password if c.isdigit()])
    characters = ''.join([c for c in password if c.isalpha()])
    symbols = ''.join([c for c in password if not c.isalnum()])
    
    # Return password along with details
    return password, numbers, characters, symbols

# Function to generate password based on personal details
def generate_personalized_password(user_input, password_length):
    # Remove spaces from the input
    user_input = user_input.replace(" ", "")
    
    # Separate numbers, characters, and symbols
    numbers = ''.join([c for c in user_input if c.isdigit()])
    characters = ''.join([c for c in user_input if c.isalpha()])
    symbols = ''.join([c for c in user_input if not c.isalnum()])
    
    # Ensure password contains at least one symbol
    if not symbols:
        print("You haven't included any symbols.")
        add_symbols = input("\nDo you want to provide some symbols? (Y/N): ").lower()
        if add_symbols == 'y':
            user_input = input("\nPlease enter the details again with symbols: ")
            user_input = user_input.replace(" ", "")
    
            # Separate numbers, characters, and symbols
            numbers = ''.join([c for c in user_input if c.isdigit()])
            characters = ''.join([c for c in user_input if c.isalpha()])
            symbols = ''.join([c for c in user_input if not c.isalnum()])
        if add_symbols == 'n':
            # Add 2 random symbols if the user denies providing symbols
            print("\nOk. I will add them by myself.")
            symbols = ''.join(random.choice(string.punctuation) for i in range(2))
    
    # If the input contains only numbers
    if numbers and not characters:
        print("You have only provided numbers. To strengthen the password, we will add characters and symbols.")
        add_chars = input("\nDo you want to provide additional character details? (Y/N): ").lower()
        if add_chars == 'y':
            user_input = input("\nPlease enter the details again with characters: ")
            user_input = user_input.replace(" ", "")
    
            # Separate numbers, characters, and symbols
            numbers = ''.join([c for c in user_input if c.isdigit()])
            characters = ''.join([c for c in user_input if c.isalpha()])
            symbols = ''.join([c for c in user_input if not c.isalnum()])

        if add_chars == 'n':
            print("\nOk. I will add them by myself.")
            # Add 4 random characters if the user denies providing characters
            characters = ''.join(random.choice(string.ascii_letters) for i in range(4))
    
    # If the input contains only characters
    elif characters and not numbers:
        print("You have only provided characters. To strengthen the password, we will add numbers and symbols.")
        add_numbers = input("\nDo you want to provide additional numeric details? (Y/N): ").lower()
        if add_numbers == 'y':
            user_input = input("\nPlease enter the details again with numbers: ")
            user_input = user_input.replace(" ", "")
    
            # Separate numbers, characters, and symbols
            numbers = ''.join([c for c in user_input if c.isdigit()])
            characters = ''.join([c for c in user_input if c.isalpha()])
            symbols = ''.join([c for c in user_input if not c.isalnum()])
        if add_numbers == 'n':
            print("\nOk. I will add them by myself.")
            # Add 4 random numbers if the user denies providing numbers
            numbers = ''.join(random.choice(string.digits) for i in range(4))
    
    # Ensure password is the correct length (mix of numbers, characters, and symbols)
    while len(numbers + characters + symbols) < password_length:
        # Add random characters and symbols until the password reaches the desired length
        characters += random.choice(string.ascii_letters)
        symbols += random.choice(string.punctuation)
    
    # Create the password by combining the numbers, characters, and symbols
    password_elements = list(numbers + characters + symbols)
    
    # Shuffle the elements to ensure randomness
    random.shuffle(password_elements)
    
    # Join elements into a final password string
    password = ''.join(password_elements[:password_length])  # Ensure the final password matches the requested length
    
    return password, numbers, characters, symbols

# Function to check password strength and provide details
def check_password_strength(password):
    # Check for password strength using regex patterns
    length = len(password)
    has_uppercase = bool(re.search(r"[A-Z]", password))
    has_lowercase = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    # Collect details of the password
    num_uppercase = len(re.findall(r"[A-Z]", password))
    num_lowercase = len(re.findall(r"[a-z]", password))
    num_digits = len(re.findall(r"[0-9]", password))
    num_symbols = len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    # Evaluate strength
    if length < 8 or not (has_uppercase and has_lowercase and has_digit and has_symbol):
        strength = "weak"
    elif length >= 12 and has_uppercase and has_lowercase and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"
    
    # Provide details about the password composition
    print(f"\nPassword length: {length}")
    print(f"Number of uppercase characters: {num_uppercase}")
    print(f"Number of lowercase characters: {num_lowercase}")
    print(f"Number of digits: {num_digits}")
    print(f"Number of symbols: {num_symbols}")
    
    # Provide recommendations
    if strength == "weak":
        print("\nYour password is weak. It is missing some crucial elements for strong security.")
        if num_uppercase == 0:
            print("\n- Add at least one uppercase letter.")
        if num_lowercase == 0:
            print("\n- Add at least one lowercase letter.")
        if num_digits == 0:
            print("\n- Add at least one digit.")
        if num_symbols == 0:
            print("\n- Add at least one symbol.")
        if length < 12:
            print("\n- Increase the length of your password to at least 12 characters.")
        
    else:
        print(f"\nYour password strength is: {strength}. Well done!")
    
    return strength

# Function to provide tips for remembering a personalized password
def suggest_password_reminder(password):
    suggestions = [
        "You can remember this by using your favorite personal details, such as names, dates, or hobbies.",
        "Consider storing it in a password manager if you're worried about forgetting it.",
        "Try creating a memorable phrase using parts of this password to make it easier to recall."
    ]
    return suggestions

# Main program logic
def main():
    print("\nWelcome to the Password Generator and Strength Checker!")
    action = input("Do you want to generate a password or check the strength of your existing password? (Generate[g]/Check[c]): ").lower()

    if action == 'c':
        password_to_check = input("\nPlease enter the password you want to check: ")
        strength = check_password_strength(password_to_check)
        
        if strength == "weak":
            print("\nYour password is weak. You can generate a new strong password using the program.")
            generate_new_password = input("\nDo you want to generate a new password? (Y/N): ").lower()
            if generate_new_password == 'y':
                choice = input("\nDo you want to generate a random password or one based on personal details? (Random[r]/Personal[p]): ").lower()
                if choice == 'r':
                    length = int(input("\nEnter the length of the password (between 8 and 64): "))
                    while length < 8 or length > 64:
                        print("Invalid length. Please enter a length between 8 and 64.")
                        length = int(input("Enter the length of the password (between 8 and 64): "))
                    while True:
                        password, numbers, characters, symbols = generate_random_password(length)
                        print(f"\nYour new random password is: {password}") # initial password display
                        satisfaction = input("\nAre you satisfied with this password? (y/n): ").lower()
                        if satisfaction == 'y':
                            break
                        else:
                            improvement_choice = input("What would you like to improve? (length[l]/characters[c]/numbers[n]/symbols[s]/all[a]): ").lower()
                            if improvement_choice == 'l':
                                length = int(input("Enter the new length (between 8 and 64): "))
                                while length < 8 or length > 64:
                                    print("Invalid length. Please enter a length between 8 and 64.")
                                    length = int(input("Enter the length of the password (between 8 and 64): "))
                                password, numbers, characters, symbols = generate_random_password(length)
                                print(f"\nYour new random password is: {password}")
                                # Password is regenerated with the new length in the next loop iteration
                            elif improvement_choice in ('c', 'n', 's', 'a'):
                                all_characters = string.ascii_letters + string.digits + string.punctuation
                                if improvement_choice == 'c':
                                    new_chars = ''.join(random.choice(string.ascii_letters) for _ in range(length))
                                    password = new_chars + ''.join(random.choice(string.digits + string.punctuation) for _ in range(length - len(new_chars)))
                                elif improvement_choice == 'n':
                                    new_nums = ''.join(random.choice(string.digits) for _ in range(length))
                                    password = new_nums + ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(length - len(new_nums)))
                                elif improvement_choice == 's':
                                    new_syms = ''.join(random.choice(string.punctuation) for _ in range(length))
                                    password = new_syms + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - len(new_syms)))
                                else: # all
                                    password = ''.join(random.choice(all_characters) for _ in range(length))

                                numbers = ''.join([c for c in password if c.isdigit()])
                                characters = ''.join([c for c in password if c.isalpha()])
                                symbols = ''.join([c for c in password if not c.isalnum()])
                                #print(f"\nYour new random password is: {password}") # Display the new password
                            else:
                                print("Invalid improvement choice.")
                    print(f"\nDetails of what has been included in your password:")
                    print(f"\n- Numbers used: {numbers}")
                    print(f"- Characters used: {characters}")
                    print(f"- Symbols added: {symbols}")
                    print("Here are some tips to help you remember the password:")
                    for tip in suggest_password_reminder(password):
                        print("\n- " + tip)
                elif choice == 'personal':
                    user_input = input("\nEnter personal details you want to base the password on (e.g., names, hobbies, or birthdate): ")
                    length = int(input("\nEnter the length of the password (between 8 and 64): "))
                    while length < 8 or length > 64:
                        print("Invalid length. Please enter a length between 8 and 64.")
                        length = int(input("Enter the length of the password (between 8 and 64): "))
                    while True:
                        password, numbers, characters, symbols = generate_personalized_password(user_input, length)
                        print(f"\nYour personalized password is: {password}")
                        satisfaction = input("\nAre you satisfied with this password? (y/n): ").lower()
                        if satisfaction == 'y':
                            break
                        else:
                            improvement_choice = input("\nWhat would you like to improve? (length[l]/characters[c]/numbers[n]/symbols[s]/all[a]): ").lower()
                            if improvement_choice == 'l':
                                length = int(input("Enter the new length (between 8 and 64): "))
                                while length < 8 or length > 64:
                                    print("Invalid length. Please enter a length between 8 and 64.")
                                    length = int(input("Enter the length of the password (between 8 and 64): "))
                                password, numbers, characters, symbols = generate_random_password(length)
                                print(f"\nYour new password is: {password}")
                                # Password is regenerated with the new length in the next loop iteration
                            elif improvement_choice in ('c', 'n', 's', 'a'):
                                all_characters = string.ascii_letters + string.digits + string.punctuation
                                if improvement_choice == 'c':
                                    new_chars = ''.join(random.choice(string.ascii_letters) for _ in range(length))
                                    password = new_chars + ''.join(random.choice(string.digits + string.punctuation) for _ in range(length - len(new_chars)))
                                elif improvement_choice == 'n':
                                    new_nums = ''.join(random.choice(string.digits) for _ in range(length))
                                    password = new_nums + ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(length - len(new_nums)))
                                elif improvement_choice == 's':
                                    new_syms = ''.join(random.choice(string.punctuation) for _ in range(length))
                                    password = new_syms + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - len(new_syms)))
                                else: # all
                                    password = ''.join(random.choice(all_characters) for _ in range(length))

                                numbers = ''.join([c for c in password if c.isdigit()])
                                characters = ''.join([c for c in password if c.isalpha()])
                                symbols = ''.join([c for c in password if not c.isalnum()])
                                #print(f"\nYour new random password is: {password}") # Display the new password
                            else:
                                print("Invalid improvement choice.")
                    print("\nDetails of what has been included in your password:")
                    print(f"\n- Numbers used: {numbers}")
                    print(f"- Characters used: {characters}")
                    print(f"- Symbols added: {symbols}")
                    print("Here are some tips to help you remember the password:")
                    for tip in suggest_password_reminder(password):
                        print("\n- " + tip)
            else:
                print("Please consider updating your password for better security.")
        else:
            print("Your password is of medium or strong strength. Good job!")
            
    elif action == 'g':
        choice = input("\nDo you want to generate a random password or one based on personal details? (Random[r]/Personal[p]): ").lower()
        if choice == 'r':
            length = int(input("Enter the length of the password (between 8 and 64): "))
            while length < 8 or length > 64:
                print("Invalid length. Please enter a length between 8 and 64.")
                length = int(input("Enter the length of the password (between 8 and 64): "))
            while True:
                        password, numbers, characters, symbols = generate_random_password(length)
                        print(f"\nYour new random password is: {password}") # initial password display
                        satisfaction = input("\nAre you satisfied with this password? (y/n): ").lower()
                        if satisfaction == 'y':
                            break
                        else:
                            improvement_choice = input("\nWhat would you like to improve? (length[l]/characters[c]/numbers[n]/symbols[s]/all[a]): ").lower()
                            if improvement_choice == 'l':
                                length = int(input("Enter the new length (between 8 and 64): "))
                                while length < 8 or length > 64:
                                    print("Invalid length. Please enter a length between 8 and 64.")
                                    length = int(input("Enter the length of the password (between 8 and 64): "))
                                password, numbers, characters, symbols = generate_random_password(length)
                                print(f"\nYour new random password is: {password}")
                                # Password is regenerated with the new length in the next loop iteration
                            elif improvement_choice in ('c', 'n', 's', 'a'):
                                all_characters = string.ascii_letters + string.digits + string.punctuation
                                if improvement_choice == 'c':
                                    new_chars = ''.join(random.choice(string.ascii_letters) for _ in range(length))
                                    password = new_chars + ''.join(random.choice(string.digits + string.punctuation) for _ in range(length - len(new_chars)))
                                elif improvement_choice == 'n':
                                    new_nums = ''.join(random.choice(string.digits) for _ in range(length))
                                    password = new_nums + ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(length - len(new_nums)))
                                elif improvement_choice == 's':
                                    new_syms = ''.join(random.choice(string.punctuation) for _ in range(length))
                                    password = new_syms + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - len(new_syms)))
                                else: # all
                                    password = ''.join(random.choice(all_characters) for _ in range(length))

                                numbers = ''.join([c for c in password if c.isdigit()])
                                characters = ''.join([c for c in password if c.isalpha()])
                                symbols = ''.join([c for c in password if not c.isalnum()])
                                #print(f"\nYour new random password is: {password}") # Display the new password
                            else:
                                print("Invalid improvement choice.")
            print(f"\nDetails of what has been included in your password:")
            print(f"\n- Numbers used: {numbers}")
            print(f"- Characters used: {characters}")
            print(f"- Symbols added: {symbols}")
            print("Here are some tips to help you remember the password:")
            for tip in suggest_password_reminder(password):
                print("\n- " + tip)

        elif choice == 'personal':
            user_input = input("\nEnter personal details you want to base the password on (e.g., names, hobbies, or birthdate): ")
            length = int(input("Enter the length of the password (between 8 and 64): "))
            while length < 8 or length > 64:
                print("Invalid length. Please enter a length between 8 and 64.")
                length = int(input("Enter the length of the password (between 8 and 64): "))
            while True:
                        password, numbers, characters, symbols = generate_personalized_password(user_input, length)
                        print(f"\nYour personalized password is: {password}")
                        satisfaction = input("\nAre you satisfied with this password? (y/n): ").lower()
                        if satisfaction == 'y':
                            break
                        else:
                            improvement_choice = input("\nWhat would you like to improve? (length[l]/characters[c]/numbers[n]/symbols[s]/all[a]): ").lower()
                            if improvement_choice == 'l':
                                length = int(input("Enter the new length (between 8 and 64): "))
                                while length < 8 or length > 64:
                                    print("Invalid length. Please enter a length between 8 and 64.")
                                    length = int(input("Enter the length of the password (between 8 and 64): "))
                                password, numbers, characters, symbols = generate_random_password(length)
                                print(f"\nYour new password is: {password}")
                                # Password is regenerated with the new length in the next loop iteration
                            elif improvement_choice in ('c', 'n', 's', 'a'):
                                all_characters = string.ascii_letters + string.digits + string.punctuation
                                if improvement_choice == 'c':
                                    new_chars = ''.join(random.choice(string.ascii_letters) for _ in range(length))
                                    password = new_chars + ''.join(random.choice(string.digits + string.punctuation) for _ in range(length - len(new_chars)))
                                elif improvement_choice == 'n':
                                    new_nums = ''.join(random.choice(string.digits) for _ in range(length))
                                    password = new_nums + ''.join(random.choice(string.ascii_letters + string.punctuation) for _ in range(length - len(new_nums)))
                                elif improvement_choice == 's':
                                    new_syms = ''.join(random.choice(string.punctuation) for _ in range(length))
                                    password = new_syms + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length - len(new_syms)))
                                else: # all
                                    password = ''.join(random.choice(all_characters) for _ in range(length))

                                numbers = ''.join([c for c in password if c.isdigit()])
                                characters = ''.join([c for c in password if c.isalpha()])
                                symbols = ''.join([c for c in password if not c.isalnum()])
                                #print(f"\nYour new random password is: {password}") # Display the new password
                            else:
                                print("Invalid improvement choice.")
            print("\nDetails of what has been included in your password:")
            print(f"\n- Numbers used: {numbers}")
            print(f"- Characters used: {characters}")
            print(f"- Symbols added: {symbols}")
            print("Here are some tips to help you remember the password:")
            for tip in suggest_password_reminder(password):
                print("\n- " + tip)
    else:
        print("Invalid input. Please restart the program and choose a valid action.")

# Run the main program
if __name__ == "__main__":
    main()
