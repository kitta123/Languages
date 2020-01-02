''' Function to demonstrate printing pyramid pattern '''

def pypart(n):

    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")

n = int(input("Enter the number to get pyramid_Pattern :"))
pypart(n)
