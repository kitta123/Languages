char = input("Please Enter Your Own character : ")

if((char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')):
    if ((char >= 'a' and char <= 'z')):
        print("The Given character ", char, "is an lowercase Alphabet")
    else:
        print("The Given character ", char, "is an uppercase Alphabet")
elif(char >= '0' and char <= '9'):
    print("The Given character ", char, "is a Digit")
else:
    print("The Given character ", char, "is a Special character")


def charCheck(char):

    if len(char)>1:
        print("Enter the Character or Digit or Special Character")

    # CHECKING FOR ALPHABET
    elif ((int(ord(char)) >= 65 and int(ord(char)) <= 90) or (int(ord(char)) >= 97 and int(ord(char)) <= 122)):
        if ((int(ord(char)) >= 65 and int(ord(char)) <= 90)):
            print("uppercase Alphabet")
        else:
            print("lowercase Alphabet")

    # CHECKING FOR DIGITS
    elif (int(ord(char)) >= 48 and int(ord(char)) <= 57):
        print(" Digit ")

    # OTHERWISE SPECIAL CHARACTER
    else:
        print(" Special Character ")

# Driver Code
char = input("Please Enter Your Own character : ")
charCheck(char)
