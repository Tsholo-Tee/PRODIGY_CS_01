def caesar_cipher(text, shift, mode):
    result = ""
    
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    
    return result

# Main program
def main():
    print("Welcome to the Caesar Cipher Program!")
    
    mode = input("Would you like to encrypt or decrypt a message? ").lower()
    if mode not in ["encrypt", "decrypt"]:
        print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
        return
    
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    result = caesar_cipher(text, shift, mode)
    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()
