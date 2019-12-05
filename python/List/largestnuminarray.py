lst = int(input("Enter the number :"))
a  = []
for i in range(lst):
    numbers = int(input("Enter the number" + str(1+i) + ":"))
    a.append(numbers)
m = a[0]
for i in range(0,len(a)):
   if(a[i] > m):
       m = a[i]

print("Largest element present in given array: " + str(m))
