#A number is called prime number if it is only divisible by 1 and itself.
num = int(input("Enter a number: "))
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           # print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

elif num <= 0:
    print("Enter the positive number")

else:
   print(num,"is not a prime number")


#Using Recursion.
def isPrime(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number")
               # print(i,"times",num//i,"is",num)
               break
       else:
           print(num,"is a prime number")

    elif num <= 0:
        print("Enter the positive number")

    else:
       print(num,"is not a prime number")

num = int(input("Enter a number: "))
isPrime(num)
