''' Write a script to swap
    first integer with second integer,
    third integr with fourth integer,
    and so on from a give list'''
list = [15,20,25,12,32,63,17,81]
print("Unswaped List is :",list)
i = 0
n = len(list)
while i < n:
    temp = list[i]
    list[i] = list[i+1]
    list[i+1] = temp
    i = i + 2
print("Swaped List is :",list)


''' Using Recursion '''
def swaplist(n):
    i = 0
    n = len(list)
    while i < n:
        temp = list[i]
        list[i] = list[i+1]
        list[i+1] = temp
        i = i + 2
    print("Swaped List is :",list)

num = int(input("Enter the Even number :"))
list = []
for i in range(0,num):
    number = int(input("Enter the number "+str(i+1)+":"))
    list.append(number)
print("Unswaped List is :",list)
swaplist(list)
