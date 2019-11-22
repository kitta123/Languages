num = int(input("Enter the number to check prime or not prime :"))
import math
if num>1:
    for i in range(2,math.floor(num/2)):
        if num%i==0:
            print("{} is not a prime number".format(num))
            break
    else:
        print("{} is a prime number".format(num))
else:
    print("{} is not a number".format(num))

#using Recursion
