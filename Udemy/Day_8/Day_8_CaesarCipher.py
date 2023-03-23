from Cipher_Art import logo


def caesar(direction, text, shift):
    en_cipher = []
    de_cipher = []
    for letter in text:
        if (letter not in alphabet):
            en_cipher.append(letter)
            de_cipher.append(letter)
        else:
            index = alphabet.index(letter) + 26
            en_cipher.append(alphabet[(index + shift) % 26])
            de_cipher.append(alphabet[(index - shift) % 26])
    if (direction == "encode"):
        print("The encoded text is " + "".join(en_cipher))
    else:
        print("The decoded text is " + "".join(de_cipher))


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
repeat = "yes"
while (repeat == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    caesar(direction, text, shift)

    repeat = input(
        "If you wnat to repeat the caesar cipher? If so, type 'Yes' else type 'No' : ").lower
print("Good bye. Thanks you for using!")

# def encrypt(text, shift):
#     cipher = []
#     for letter in text:
#         index = (alphabet.index(letter) + shift) % 26
#         cipher.append(alphabet[index])
#     print("The encoded text is " + "".join(cipher))


# def decrypt(text, shift):
#     cipher = []
#     for letter in text:
#         index = alphabet.index(letter) - shift % 26
#         if (index < 0):
#             index += 26
#         cipher.append(alphabet[index])
#     print("The decoded text is " + "".join(cipher))
# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


# if (direction == "encode"):
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)
