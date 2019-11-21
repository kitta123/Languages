table = int(input("Enter the number for multication table :"))
count = 1
for count in range(1,11):
    print(table,"*",count,"=",table*count)
    count +=1

table = int(input("Enter the number for multication table :"))
count = 1
while count<11:
    print(table,"*",count,"=",table*count)
    count +=1

#Using Recursion
def mul(table):
    count = 1
    for count in range(1,11):
        print(table,"*",count,"=",table*count)
        count +=1
table = int(input("Enter the number for multication table :"))
mul(table)
