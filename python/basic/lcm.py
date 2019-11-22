def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Enter the first lcm number :"))
num2 = int(input("Enter the second lcm number :"))
print("Them Lcm of the Two numbers is",lcm(num1,num2))

#Using Euclidian Algorithm.
def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x

def lcm(x,y):
    lcm = (x*y)//gcd(x,y)
    return lcm

num1 = int(input("Enter the first lcm number :"))
num2 = int(input("Enter the second lcm number :"))
print("Them Lcm of the Two numbers is",lcm(num1,num2))
