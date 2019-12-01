''' write a script to remove duplicate words from a give string '''
str = input("Enter the string :")
str = str.lower()
words = str.split()
list = []
for word in words:
    if word not in list:
        list.append(word)
        str1 = ' '.join(list)
    else:
        print("No duplicate string in the list")
print(str1)

''' Using Recursion '''
def removeDuplicate(str):
    str = str.lower()
    words = str.split()
    list = []
    for word in words:
        if word not in list:
            list.append(word)
            str1 = ' '.join(list)
        return str1

str = input("Enter the string :")
print(removeDuplicate(str))
