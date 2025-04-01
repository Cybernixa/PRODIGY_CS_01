def shift_char(char, shift):
    """
    Shifts a single character by the given shift value.
    Handles both uppercase and lowercase letters.
    Non-alphabetic characters are returned unchanged.
    """
    

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts the given text using the Caesar Cipher algorithm.
    """
    if mode == "decrypt":
        shift = -shift  # Reverse the shift for decryption
    result = ""
    for char in text:
        result += shift_char(char, shift)
    return result

def get_user_input():
    """
    Prompts the user for input and returns the message, shift value, and mode.
    """
    print("Welcome to the Caesar Cipher Program!")
    print("Choose an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    
    choice = input("Enter your choice (1 or 2): ")
    if choice not in ["1", "2"]:
        print("Invalid choice. Please try again.")
        return None, None, None
    
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (an integer): "))
    mode = "encrypt" if choice == "1" else "decrypt"
    
    return message, shift, mode

def main():
    """
    Main function to run the Caesar Cipher program.
    """
    message, shift, mode = get_user_input()
    if message is None:
        return  # Exit if input is invalid
    
    result = caesar_cipher(message, shift, mode)
    print(f"{mode.capitalize()}ed message: {result}")

if __name__ == "__main__":
    main()
