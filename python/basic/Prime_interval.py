lower = int(input("Enter the starting number :"))
upper = int(input("Enter the Ending number :"))
lst = []
print("The prime numbers between {} and {} :".format(lower,upper))
for num in range(lower,upper+1):
    if num >1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            lst.append(num)
print(lst)
