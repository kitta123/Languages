''' Function to demonstrate printing pattern of alphabets '''
def  contalpha(n):

    # ASCII value
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            # explicitely converting to char
            ch = chr(num)
            print(ch, end=" ")
            num = num +1
        print("\r")

n = int(input("Enter the number to get Alphabet Pattern :"))
contalpha(n)
