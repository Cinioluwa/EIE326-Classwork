upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def find_index(letter, lst):
    for i in range(len(lst)):
        if letter == lst[i]:
            return i
    return -1
def shiftLetter(letter, shift):
    if letter in upperCase:
        _index = find_index(letter, upperCase)
        if _index == -1:
            return letter
        new_index = (_index + shift) % 26
        return upperCase[new_index]
    elif letter in lowerCase:
        _index = find_index(letter, lowerCase)
        if _index == -1:
            return letter
        new_index = (_index + shift) % 26
        return lowerCase[new_index]
    else:
        return letter
def caesarCipher(message, shift):
    newMessage = ''
    for letter in message:
        newMessage += shiftLetter(letter, shift)
    return newMessage

print("Welcome to the Caesar Cipher program!")
print("This program will encrypt or decrypt a message using the Caesar Cipher method.")
print("Please enter your message:")
message = input()
print("Please enter the shift value (positive for encryption, negative for decryption):")
shift = int(input())
result_message = caesarCipher(message, shift)
print("The encrypted/decrypted message is:")
print(result_message)
print("Thank you for using the Caesar Cipher program!✨")