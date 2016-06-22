def getsen():

import re

f = open('compare_sentences.txt')
rsent = f.readlines()
f.close()
fsent = []
for l in range(len(rsent)):
    if rsent[l]=='\n':
        continue
    rsent[l] = rsent[l].strip()
    match = re.search(r'([^\(]*)(\(.*)',rsent[l])
    if match:
        fsent+=[str(l) + match.group(2)]
        continue
    #fsent+=[rsent[l]+'\n']

print fsent

'''
f=open('outsent.txt','w')
f.writelines(fsent)'''
