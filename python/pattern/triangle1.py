''' Function to demonstrate printing Triangle pattern '''

def triangle(n):

    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1

        for j in range(0, i+1):
            print("* ", end="")
        print("\r")

n = int(input("Enter the number to get Triangle_Pattern :"))
triangle(n)
