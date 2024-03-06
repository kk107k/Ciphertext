def decrypt_caesar_cipher(ciphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(1, 26):
        decrypted_text = ''
        for char in ciphertext.lower():
            if char in alphabet:
                decrypted_char = alphabet[(alphabet.index(char) - key) % 26]
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        print(f"Key: {key}, Decrypted Text: {decrypted_text}")

def encrypt_caesar_cipher(plaintext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for char in plaintext.lower():
        if char in alphabet:
            encrypted_char = alphabet[(alphabet.index(char) + key) % 26]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    print(f"Encrypted Text: {encrypted_text}")

def find_encryption_key(plaintext, ciphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plaintext_char = plaintext[0].lower()
    ciphertext_char = ciphertext[0].lower()
    plaintext_index = alphabet.index(plaintext_char)
    ciphertext_index = alphabet.index(ciphertext_char)
    key = (ciphertext_index - plaintext_index) % 26
    return key

def decrypt_with_substitution_table(ciphertext, plaintext_sub, ciphertext_sub):
    substitution_dict = {c: p for p, c in zip(plaintext_sub, ciphertext_sub)}
    plaintext = ''.join(substitution_dict.get(char, char) for char in ciphertext)
    return plaintext

# Main interface
choice = input("Would you like to decrypt (1), encrypt (2), find the key (3), or decrypt with a substitution table (4)? ")

if choice == "1":
    ciphertext = input("Enter the ciphertext: ")
    decrypt_caesar_cipher(ciphertext)
elif choice == "2":
    plaintext = input("Enter the plaintext: ")
    key = int(input("Enter the key (shift amount): "))
    encrypt_caesar_cipher(plaintext, key)
elif choice == "3":
    plaintext = input("Enter the plaintext: ")
    ciphertext = input("Enter the ciphertext you want to achieve: ")
    key = find_encryption_key(plaintext, ciphertext)
    print(f"The key needed to transform “{plaintext}” into “{ciphertext}” is: {key}")
elif choice == "4":
    plaintext_sub = input("Enter plaintext substitution characters: ").upper()
    ciphertext_sub = input("Enter ciphertext substitution characters: ").upper()
    ciphertext = input("Enter the ciphertext: ")
    plaintext = decrypt_with_substitution_table(ciphertext, plaintext_sub, ciphertext_sub)
    print(f"The plaintext is: {plaintext}")
else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")
