def sumall(list, size): 
   if (size == 0): 
     return 0
   else: 
     return list[size - 1] + sumall(list, size - 1)
   
# Driver code  
lst=[]   
lst1 = 0 
list1 = int(input("enter how many numbers you want to sum :"))
for n in range(list1):
    numbers = int(input('Enter number' + str(lst1+1)+':'))
    lst.append(numbers)
    lst1 = lst1+1
total = sumall(lst, len(lst))
print("Sum of all elements in given list: ", total) 
