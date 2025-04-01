Program Overview
The Caesar Cipher works by shifting letters in the alphabet by a fixed number of positions. For example, with a shift of 3:

"A" becomes "D" (encryption)

"D" becomes "A" (decryption).

This program allows users to:

Encrypt a message by shifting letters forward.

Decrypt a message by shifting letters backward.

Key Components
1. shift_char(char, shift) (Incomplete)
Purpose: Shifts a single character by the shift value.

Intended Behavior:

Handles uppercase (A-Z) and lowercase (a-z) letters.

Leaves non-alphabetic characters (e.g., numbers, symbols) unchanged.

Wraps around the alphabet (e.g., Z → C with shift 3 for encryption).

Current State: This function is unimplemented in the provided code. Without it, the cipher cannot process characters, rendering the program non-functional. To fix this, logic for shifting and wrapping characters must be added here.

2. caesar_cipher(text, shift, mode)
Purpose: Applies the Caesar Cipher to an entire string.

Workflow:

Reverses the shift for decryption (e.g., shift +3 becomes -3).

Iterates over each character in text, using shift_char to transform it.

Builds and returns the result string.

Note: Depends on shift_char to work correctly.

3. get_user_input()
Purpose: Collects user input and configures the cipher.

Steps:

Prompts the user to choose encryption or decryption.

Validates the choice (only accepts 1 or 2).

Collects the message and shift value.

Returns mode as "encrypt" or "decrypt".

Handling Invalid Input: Returns None for invalid choices, causing the program to exit gracefully.

4. main()
Purpose: Orchestrates the program flow.

Calls get_user_input() to get user data.

Exits if input is invalid.

Runs caesar_cipher with the provided parameters.

Prints the encrypted/decrypted result.

Critical Missing Piece: shift_char Implementation
For the program to work, shift_char must:

Check if the character is alphabetic.

Calculate its shifted position using modular arithmetic (to wrap around the alphabet).

Preserve case (uppercase/lowercase) and non-alphabetic characters.

Example Implementation:

python
Copy
def shift_char(char, shift):
    if char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    elif char.islower():
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        return char  # Non-alphabetic characters
Limitations & Improvements
Shift Handling: The current code does not handle shifts >26 (e.g., shift 30). Using modulo 26 in shift_char would resolve this.

Input Validation: The shift value is accepted as any integer but should ideally be constrained to avoid overly large values.

Edge Cases: Symbols, spaces, and numbers are preserved but not processed.

Usage Example
Encrypt:
Input: "HELLO", shift=3 → Output: "KHOOR".

Decrypt:
Input: "KHOOR", shift=3 → Output: "HELLO".
