"""find smallest number in the given numbers"""

a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
c = int(input("Enter the number :"))
if a < b and a < c:
    print(a,"is a smallest number")
elif b < a and b < c:
    print(b,"is a smallest number")
else:
    print(c,"is a smallest number")

'''Using Recursion'''
def smallest_number(a,b,c):
    if a < b and a < c:
        print(a,"is a smallest number")
    elif b < a and b < c:
        print(b,"is a smallest number")
    else:
        print(c,"is a smallest number")

a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
c = int(input("Enter the number :"))
smallest_number(a,b,c)
