''' Function to demonstrate printing pattern of inverted pyramid '''

def inverted(n):

    for i in range (n,0,-1):
        for j in range(0, i + 1):
            print("*", end=' ')

        print("\r")

n = int(input("Enter the number to print pattern of inverted pyramid: "))
inverted(n)
