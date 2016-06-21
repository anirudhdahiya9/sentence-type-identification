import re

f = open('sentences.txt')
rsent = f.readlines()
f.close()
fsent = []
for l in range(len(rsent)):
    if rsent[l]=='\n':
        continue
    rsent[l] = rsent[l].strip()
    match = re.search(r'([^\(]*)\(.*',rsent[l])
    if match:
        fsent+=[match.group(1) + '\n']
        continue
    fsent+=[rsent[l]+'\n']

f=open('outsent.txt','w')
f.writelines(fsent)
