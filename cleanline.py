import re

f=open('marked_output.txt')
rsent = f.readlines()
fsent=[]
for i in range(len(rsent)):
    if len(rsent[i].split('\t'))>1:
        if rsent[i].split('\t')[1].startswith('<'):
            print rsent[i]
            continue
    fsent+=[rsent[i]]

f=open('finalfinaldata.txt','w')
f.writelines(fsent)
f.close()


