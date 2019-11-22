def hcf(x,y):
    while(y):
        x,y = y,x%y
    return x

x = int(input("Enter the number :"))
y = int(input("Enter the number :"))
print(hcf(x,y))

def hcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x%i==0)and(y%i==0)):
            hcf = i
    return hcf
x = int(input("Enter the number :"))
y = int(input("Enter the number :"))
print(hcf(x,y))
