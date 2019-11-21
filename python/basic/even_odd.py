def isEven(n) :
    return (n & 1);

n = int(input("Enter the number to check even or odd :"));
if(isEven(n) == 0) :
    print ("Even");
else :
    print ("Odd");

n = int(input("Enter the number to check even or odd :"))
if n%2==0:
    print("Entered number is even")
else:
    print("Entered number is odd")
