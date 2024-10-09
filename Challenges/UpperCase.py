def check_uppercase(input_string):
    # Create a list to hold the uppercase letters found
    uppercase_letters = [char for char in input_string if char.isupper()]
    
    # Check if there are any uppercase letters
    if uppercase_letters:
        print(f"Uppercase letters found: {', '.join(uppercase_letters)}")
    else:
        print("No uppercase letters found.")

# Example usage
user_input = input("Enter a string: ")
check_uppercase(user_input)
