''' To count Even Length words from a given string '''
str = input("Enter the string :")
str = str.lower()
k = str.split()
count = 0
for i in k:
    if len(i) % 2 == 0:
        count += 1
        print(i,"is a even word")
print(count)

''' Using Recursion '''
def countEven(str):
    str = str.lower()
    k = str.split()
    count = 0
    for i in k:
        if len(i) % 2 == 0:
            count += 1
            print(i,"is a even word")
    print(count)

str = input("Enter the string :")
countEven(str)
