#find the sum of 2 numbers
a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
c = a + b
print("The sum of two numbers is :",c)


#Using Recursion
def add2num(a,b):
    c = a + b
    print(c)

a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
print("The sum of {} and {} :".format(a,b))
add2num(a,b)
