num = int(input("Enter the number :"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum = sum + digit**3
    temp = temp//10
if num == sum:
    print("{} is a armstring number".format(num))
else:
    print("{} is not a armstring nuber".format(num))


#Using Recursion:
def armstring(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit**3
        temp = temp//10
    if num == sum:
        print("{} is a armstring number".format(num))
    else:
        print("{} is not a armstring number".format(num))

num = int(input("Enter the number :"))
armstring(num)
