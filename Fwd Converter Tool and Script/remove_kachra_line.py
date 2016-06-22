f=open('marked_parsed_output.txt')
rsent=f.readlines()
fsent=[]
for i in range(len(rsent)):
    if len(rsent[i].split('\t'))>1:
        if rsent[i].split('\t')[1].startswith('<'):
            continue
    fsent+=[rsent[i]]

f=open('final_output.txt','w')
f.writelines(fsent)
f.close()
