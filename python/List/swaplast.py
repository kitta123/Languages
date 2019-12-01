a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
#temp=a[0]
#a[0]=a[n-1]
#a[n-1]=temp
a[0],a[-1] = a[-1],a[0]
#a[0],a[2] = a[2],a[0]

print("New list is:",a)

''' Using Recursion '''
def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 4

print(swapPositions(List, pos1-1, pos2-1))

''' Using Recursion '''
def swapPositions(list, pos1, pos2):

    # popping both the elements from list
    first_ele = list.pop(pos1)
    second_ele = list.pop(pos2-1)

    # inserting in each others positions
    list.insert(pos1, second_ele)
    list.insert(pos2, first_ele)

    return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 2

print(swapPositions(List, pos1-1, pos2-1))
