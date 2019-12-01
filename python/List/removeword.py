def RemoveIthWord(lst, word, N):
    newList = []
    count = 0
    for i in lst:
        if(i == word):
            count = count + 1
            if(count != N):
                newList.append(i)
        else:
            newList.append(i)

    lst = newList
    if count == 0:
        print("Item not found")
    else:
        print("Updated list is: ", lst)
    return newList

# Driver code
list = ["geeks", "for", "geeks"]
word = "geeks"
N = 3
RemoveIthWord(list, word, N)

#=======================================#

def RemoveithWord(list, word, N):
    count = 0
    for i in range(0, len(list)):
        if (list[i] == word):
            count = count + 1
            if(count == N):
                del(list[i])
                return True
    return False

# Driver code
list = ['geeks', 'for', 'geeks']
word = 'geeks'
N = 3
flag = RemoveithWord(list, word, N)
if (flag == True):
    print("Updated list is: ", list)
else:
    print("Item not Updated")
