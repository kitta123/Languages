'''' Count the Non unique elements in the given list '''

lst = [1,2,3,1,4,2,3,1,2,4,5,2,1,2]
temp = set(lst)
result = {}
for i in temp:
    result[i] = lst.count(i)
print(result)


'''' Using Recursion '''
def countNonUnique(lst):
    temp = set(lst)
    result = {}
    for i in temp:
        result[i] = lst.count(i)
    print(result)

lst = int(input("Enter the number :"))
lst1 = []
for i in lst:
    numbers = int(input("Enter the numbers :"))
    lst1.append(numbers)
countNonUnique(lst1)
