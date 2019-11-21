a = int(input("enter a first number :"))
b = int(input("enter a second number :"))
c = int(input("enter a third number :"))
if a>=b and a>=c:
    print("{} is large number".format(a))
elif b>=a and b>=c:
    print("{} is large number".format(b))
else:
    print("{} is large number".format(c))
