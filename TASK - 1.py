#IMPLEMENTING THE CAESAR CIPHER ALGORITHM
def encrypt(text, shift_value):
    output = ""
    for ch in text:
        if ch == " ":
            output += " "
        elif ch.isupper():
            output += chr((ord(ch) + shift_value - 65) % 26 + 65)
        else:
            output += chr((ord(ch) + shift_value - 97) % 26 + 97)
    return output

def decrypt(text, shift_value):
    output = ""
    for ch in text:
        if ch == " ":
            output += " "
        elif ch.isupper():
            output += chr((ord(ch) - shift_value - 65) % 26 + 65)
        else:
            output += chr((ord(ch) - shift_value - 97) % 26 + 97)
    return output

if __name__=="__main__": 
    print("1. ENCRYPTION")
    print("2. DECRYPTION")
    result = ""
    ch='y'
    while(ch.lower()=='y'):
        mode = int(input("Enter any one of the 2 modes: "))
        if mode == 1:
            text = input("Enter the input text: ")
            shift_value = int(input("Enter the shift value: "))
            result = encrypt(text, shift_value)
            print("After Encryption:", result)
        elif mode == 2:
            text = input("Enter the input text: ")
            shift_value = int(input("Enter the shift value: "))
            result = decrypt(text, shift_value)
            print("After decryption:", result)
        else:
            print("Invalid option")
        ch=input("Do you want to continue y/n:")
