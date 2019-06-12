import numpy as np
chars = input('Enter the string of characters')
if(len(chars)>500):
    chars=chars[:500]
count={}
for char in chars:
    if char in count.keys():
        count[char]+=1
    else:
        count[char]=1
for v in sorted( count.values() ,reverse=True):
    for key in count:
        if count[ key ] == v:
            print(key)

for k,v in count.items():
    if(v>5):
        del(count[k])
chars = list(chars)
for k,v in count.items():
    if(count[k]==1):
        if(len(chars) >499):
            del(np.random(count[k])
        count[k]+=1    
