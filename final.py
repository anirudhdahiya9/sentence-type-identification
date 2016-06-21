import os

f=open('outsent.txt')
rsent = f.readlines()
count = 1
for line in rsent:
    q=open('temp.txt','w')
    q.write(line)
    q.close()
    os.system('shallow_parser_hin temp.txt >>output.txt')
    print(str(count) +':' +str(len(rsent)))
    count+=1

