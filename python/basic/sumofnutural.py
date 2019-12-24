num = int(input("Enter the number :"))
if num <= 0:
    print("Enter the positive number")
    if num == 1:
        print("Sum of Entered number is 1")
else:
    sum = 0
    while num>0:
        sum +=num
        num = num-1
    print("The sum of entered number is",sum)



num = int(input("Enter the number :"))
if num <= 0:
    print("Enter the positive number")
    if num == 1:
        print("Sum of entered number is 1")
else:
    sum = num*(num+1)/2
    print("Sum of entered number is :",sum)

#Using Recursion:
def sumofnatural(n):
    if num <= 0:
        print("Enter the positive number")
        if num == 1:
            print("Sum of entered number is 1")
    else:
        sum = num*(num+1)/2
        print("Sum of entered number is :",sum)

l = []
num = int(input("Enter the number :"))
sumofnatural(num)
