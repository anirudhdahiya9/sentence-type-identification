import re

f = open('final_unparsed_compare.txt')
rsent = f.readlines()
f.close()
fsent = []
for l in range(len(rsent)):
    if rsent[l]=='\n':
        continue
    rsent[l] = rsent[l].strip()
    match = re.search(r'([^\(]*)(\(.*)',rsent[l])
    if match:
        fsent+=[match.group(1)+'\n']
        continue
    fsent+=[rsent[l]]

print fsent

f=open('final_unparsed.txt','w')
f.writelines(fsent)
f.close()
