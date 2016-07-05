import re

f = open('newdata.txt')
rsent = f.readlines()
f.close()
fsent = []
for l in range(len(rsent)):
    if rsent[l]=='\n':
        print('hi')
        continue
    rsent[l] = rsent[l].strip()
    match = re.search(r'([^\(]*)(\(.*)',rsent[l])
    if match:
        fsent+=[ match.group(1)+'\n']
        continue
    else:
        print l
    #fsent+=[rsent[l]+'\n']

#print fsent

f=open('outsent.txt','w')
f.writelines(fsent)
