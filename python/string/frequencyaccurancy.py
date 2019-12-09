''' write a script to find the frequency accurance of words from a give string '''
s = input("Enter some string :")
s = s.lower()
words = s.split()
d = {}
for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] = d[word] + 1
for k in d.keys():
    print(k,":",d[k])

''' Using Recursion '''
def frequencyaccurance(s):
    s = s.lower()
    words = s.split()
    d = {}
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] = d[word] + 1
    for k in d.keys():
        print(k,":",d[k])

s = input("Enter some string :")
frequencyaccurance(s)
