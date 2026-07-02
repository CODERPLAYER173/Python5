
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text1 = input("Type your message:\n").lower()
shift1 = int(input("Type the shift number:\n"))
if direction == 'encode':
    def encrypt(shift,text):
        cipher = ""
        for letter in text:
            shift_position = alphabet.index(letter) + shift
            cipher += alphabet[shift_position]

        print(f"your encoded result is {cipher}")
    encrypt(shift=shift1, text=text1)

#___________________________________________________________________________________________________________________________________
elif  direction == "decode":
    text2 = input("what is the text sent to you\n")
    shift2 = int(input("pls enter the shift value\n"))
    def decrypt(shift,text):
        cipher = ""
        for letter in text:
            shift_position = alphabet.index(letter) - shift
            cipher += alphabet[shift_position]

        print(f"your encoded result is {cipher}")

    decrypt(shift=shift2,text=text2)

else:
    print("Invalid input")

again = input("Do you want to continue pls type \'yes\' or \'no\'\n")
while again == 'yes':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode':
        text1 = input("Type your message:\n").lower()
        shift1 = int(input("Type the shift number:\n"))
        def encrypt(shift, text):
            cipher = ""
            for letter in text:
                shift_position = alphabet.index(letter) + shift
                cipher += alphabet[shift_position]

            print(f"your encoded result is {cipher}")


        encrypt(shift=shift1, text=text1)

    # ___________________________________________________________________________________________________________________________________
    elif direction == "decode":
        text2 = input("what is the text sent to you\n")
        shift2 = int(input("pls enter the shift value\n"))


        def decrypt(shift, text):
            cipher = ""
            for letter in text:
                shift_position = alphabet.index(letter) - shift
                cipher += alphabet[shift_position]

            print(f"your encoded result is {cipher}")


        decrypt(shift=shift2, text=text2)
        again = input("Do you want to continue pls type \'yes\' or \'no\'\n")

    else:
        print("Invalid input")
while again == "no":
    break



