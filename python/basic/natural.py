#Nutural numbers.
num = int(input("Enter a number: "))
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0    
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)  

#using Recursion.
def listsum(num):
    t = 0
    for i in num:
        t = t + i
    return t
c =[]
e = 0
a = int(input("enter the number:"))
for i in range(0,a):
    b = int(input("enter number"+str(i+1)+':'))
    d = c.append(b)
    e +=1
print(listsum(c))
