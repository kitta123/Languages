def addnum(num):
    for i, n in enumerate(num[:-1]):
        c = target - n
        if c in num[i+1:]:
            print("The Solution numbers: {} and {}".format(n, c))
            break
    else:
        print("No solutions exist")

lst=[]
lst1 = 0
lst2 = []
list1 = int(input("Enter how many numbers you want to sum :"))
for n in range(0,list1):
    numbers = int(input('Enter number' + str(lst1+1)+':'))
    lst.append(numbers)
    lst1 = lst1+1
target = int(input('Enter the target number :'))
for i in lst:
    if i<=target:
        lst2.append(i)
print(lst2)
addnum(lst2)
