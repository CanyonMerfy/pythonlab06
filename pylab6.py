alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere_sq():
    for i in range(len(alphabet)):
        shifted = alphabet[i:] + alphabet[:i]
        formatted_row = f"{alphabet[i]}|{'|'.join(shifted)}|"
        print(formatted_row)



def letter_to_index(letter):
    index = -1
    for i in alphabet:
        index += 1
        if i == letter.upper():
            return index


def index_to_letter(index):
    return alphabet[index]


def vigenere_index(key_letter, plaintext_letter):
    key_index = letter_to_index(key_letter)
    plaintext_index = letter_to_index(plaintext_letter)

    cipher_index = (key_index + plaintext_index) % 26
    return cipher_index

def encrypt_vigenere(key, plaintext):
    cipher_text = ""
    key_index = 0

    for letter in plaintext:
        if letter.isalpha():
            cipher_index = vigenere_index(key[key_index], letter)

            cipher_letter = index_to_letter(cipher_index)

            cipher_text += cipher_letter

            key_index = (key_index + 1) % len(key)
        else:
            cipher_text += letter

    return cipher_text

print(encrypt_vigenere("key", "plaintext"))
