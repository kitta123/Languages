# def addnum(num):
#     for i, n in enumerate(num[:-1]):
#         c = target - n
#         if c in num[i+1:]:
#             print("The Solution numbers: {} and {}".format(n, c))
#             break
#     else:
#         print("No solutions exist")
#
# lst=[]
# lst1 = 0
# lst2 = []
# list1 = int(input("Enter how many numbers you want to sum :"))
# for n in range(0,list1):
#     numbers = int(input('Enter number' + str(lst1+1)+':'))
#     lst.append(numbers)
#     lst1 = lst1+1
# target = int(input('Enter the target number :'))
# for i in lst:
#     if i<=target:
#         lst2.append(i)
# print(lst2)
# addnum(lst2)


def printPairs(a, n, sum):
    lst = []
    for i in range(0, n ):
        for j in range(i + 1, n ):
            if (a[i] + a[j] == sum):
                print("The solutions for the give value :","(",a[i],",",a[j],")",sep = "")
                lst.append((arr[i],arr[j]))
    print(lst)

lst = []
lst1 = 0
lst2 = []
lst3 = []
a = int(input("Enter how many numbers you want to sum :"))
for n in range(0,a):
    numbers = int(input('Enter number' + str(lst1+1)+':'))
    lst.append(numbers)
    lst1 = lst1+1
n = len(lst)
sum = target = int(input('Enter the target number :'))
for i in lst:
    if i<=sum:
        lst2.append(i)
    else:
        lst3.append(i)

print(lst2)
print(lst3)
printPairs(lst, n, sum)
