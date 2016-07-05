f=open('marked_newparsed_output.txt')
rsent=f.readlines()
fsent=[]
for i in range(len(rsent)):
    if len(rsent[i].split('\t'))>1:
        if rsent[i].split('\t')[1].startswith('<'):
            continue
    fsent+=[rsent[i]]

f=open('final_newoutput.txt','w')
f.writelines(fsent)
f.close()
