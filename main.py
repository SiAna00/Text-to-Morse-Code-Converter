import json

with open("data.json", mode="r") as file:
    morse_code = json.load(file)


print("Welcome to Text to Morse Code Converter")

# Making the encrypting function
def encrypt(text):
    encrypted = ""
    for i in text.lower():
        if i == " ":
            encrypted += "/ "
            continue

        if i not in morse_code:
            return "Invalid Characters found!"
        encrypted += morse_code[i]
        encrypted += " "
    return encrypted

# Making the decryption function code
def decrypt(text):
    text_list = text.split()
    print(text_list)
    decrypted = ""
    for i in text_list:
        if i == "/":
            decrypted += " "
            continue
        for j in morse_code:

            if i == morse_code[j]:
                decrypted += j

    return decrypted

# Taking on User Input
while True:
    user = input("Would you like to encrpyt or decrypt text or Quit? Type(encrypt/decrypt/q):\n").lower()
    if user == "encrypt":
        encrypted_message = encrypt(input("\nType the Message...\n"))
        print(f"\nEncrypted Message:\n{encrypted_message}\n")
    elif user== "decrypt":
        decrypted_message = decrypt(input("\nType the Message...\n"))
        print(f"\nDecrypted Message:\n{decrypted_message}\n")
    elif user == "q":
        break
    else:
        print("Invalid Input")