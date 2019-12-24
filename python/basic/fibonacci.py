num = int(input("Enter the number to find fibonacci sequence :"))
a = 0
b = 1
count = 0
if num <= 0:
    print("please enter the positive number")
elif num == 1:
    print(a)
else:
    print("The Fibonacci sequence upto",num,":",a,end=' ')
    while count<num:
        print(a,end=' ')
        c = a+b
        a = b
        b = c
        count += 1
    print('\n')

#Using Recursion:
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

n = int(input("Enter the number to find fibonacci sequence :"))
lst = []
if n <= 1:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       j = fibo(i)
       lst.append(j)
print(lst)
