''' Function to demonstrate printing pattern of inverted pyramid '''

def sidetrinagle(n):

    for i in range (0, n):
        for j in range(0, i + 1):
            print("*", end=' ')
        print("\r")

    for i in range (n, 0, -1):
        for j in range(0, i -1):
            print("*", end=' ')
        print("\r")

n = int(input("Enter the number to get side triangle pattern :"))
sidetrinagle(n)
