l = ['karthik','vik','kitta','vizag','rohan','rakesh','amar','ajay','jak']
print(l)
d = {}
for word in l:
    if(word[0] not in d.keys()):
        d[word[0]]=[]
        d[word[0]].append(word)
    else:
        if(word not in d[word[0]]):
          d[word[0]].append(word)
for k,v in d.items():
        print(k,":",v)

print(d)
