import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special_chars=True) -> None:
    
    # Define character sets based on user preferences
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if include_uppercase else ''
    digit_chars = string.digits if include_digits else ''
    special_chars = "!@#$%^&*()_+[]{}|;':,.<>?/" if include_special_chars else ''

    # Combine the character sets based on user preferences
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Check if at least one character set is selected
    if not all_chars:
        return "Please include at least one character set in the password."

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

# Example usage:
password = generate_password(length=16, include_uppercase=True, include_digits=True, include_special_chars=True)
print(password)
