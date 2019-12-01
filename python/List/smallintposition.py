''' write a script to find out smallest integer along with its position froma given list of integers '''

num = int(input("Enter the Even number :"))
list = []
for i in range(num):
    number = int(input("Enter the number "+str(i+1)+":"))
    list.append(number)
k = min(list)
k1 = list.index(min(list))
print("The list is :",list)
print(k,"is the smallest integer")
print(k1,"is the index position of the smallest number")



''' Using Recursion '''
def smallintposition(list):

    k = min(list)
    k1 = list.index(min(list))
    print(k,"is the smallest integer")
    print(k1,"is the index position of the smallest number")

num = int(input("Enter the Even number :"))
list = []
for i in range(num):
    number = int(input("Enter the number "+str(i+1)+":"))
    list.append(number)
print("The list is :",list)
smallintposition(list)
