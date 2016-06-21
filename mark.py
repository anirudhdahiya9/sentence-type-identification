import re

f=open('output.txt')
rsent = f.readlines()
count = 1

fsent = []
for sent in rsent:
    if sent.startswith('<Sentence'):
        fsent += ['<Sentence id="'+str(count)+'">\n']
        count+=1
        print count
        continue
    fsent += sent
        

f=open('marked_output.txt','w')
f.writelines(fsent)
f.close()
