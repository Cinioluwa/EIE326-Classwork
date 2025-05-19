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

print("Hi. So I've made a Caesar Cipher Encryptor. You can try it out!")
print("It'll encrypt or decrypt a message using the Caesar Cipher method. You can read on it to familiarize yourself with the concept.")
print("Please enter any message to be encrypted:")
message = input()
print("How many times do you want to shift it? (positive number for encryption, negative for decryption):")
shift = int(input())
result_message = caesarCipher(message, shift)
print("Alright then. Your encrypted/decrypted message is:")
print(result_message)
print("Thank you for using my Caesar Cipher Encryptor!")
