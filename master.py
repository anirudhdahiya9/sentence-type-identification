from interrogative import interrogative
from declarative import declarative
from imperative import imperative

inlist=interrogative()
imlist=imperative()
dlist = declarative()

print inlist
print imlist
print dlist

masterdict={}
for i in range(1,430):
    masterdict[str(i)]=[]

for i in inlist.keys():
        masterdict[i]+=inlist[i]
for i in imlist.keys():
        masterdict[i]+=imlist[i]
for i in dlist.keys():
        masterdict[i]+=dlist[i]

for i in range(1,430):
    print str(i) + ' : ' +str(masterdict[str(i)])


