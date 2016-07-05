from interrogative import interrogative
from declarative import declarative
from imperative import imperative
from get_sen import get_sen

inlist = interrogative()
imlist = imperative()
dlist = declarative()
tagdict = get_sen()
print inlist
print imlist
print dlist


masterdict={}
for i in range(1,549):
    masterdict[str(i)]=[]

for i in inlist.keys():
        masterdict[i]+=inlist[i]
for i in imlist.keys():
        masterdict[i]+=imlist[i]
for i in dlist.keys():
        masterdict[i]+=dlist[i]

for i in range(1,549):
    print str(i) + ' : ' +str(masterdict[str(i)])

print tagdict

score = {}
for i in range(1,549):
    score[str(i)]=0



for i in range(1,549):
    if ('I1' in masterdict[str(i)]) or ('I2' in masterdict[str(i)]):  
        if 'INT' in tagdict[str(i)][0]:
            score[str(i)]=1
            continue
    if ('IM1' in masterdict[str(i)]) or ('IM2' in masterdict[str(i)]):  
        if 'IMP' in tagdict[str(i)][0]:
            score[str(i)]=1
            continue
    if ('D' in masterdict[str(i)]) or ('' in masterdict[str(i)]):  
        if 'd' in tagdict[str(i)][0].lower():
            score[str(i)]=1
            continue

count = 0
for i in score.keys():
    if score[i]==1:
        count+=1
print((float(count)/548)*100)

f=open('newdata.txt','r')
rsent = f.readlines()
f.close()
for i in range(len(rsent)):
    rsent[i] =rsent[i].strip('\n') + ' : ' + str(masterdict[str(i+1)])  + '\n'

f=open('newreport.txt','w')
f.writelines(rsent)
f.close()

#print tagdict 
print score

