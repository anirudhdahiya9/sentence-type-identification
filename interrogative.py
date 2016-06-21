import re

f=open('marked_output.txt')
rsent = f.readlines()
#improve
sentid = 0
isent = []

for i in range(len(rsent)):
    if rsent[i].startswith('<Sentence'):
        sentid = rsent[i].split('"')[1]
    if len(rsent[i].split('\t'))>1:
        if (rsent[i].split('\t')[1]=='?') and ((rsent[i+2].startswith('</Sentence')) or ((rsent[i+1].split('\t')[1]=='"' and rsent[i+3].startswith('</Sentence')))):
            print sentid
            isent += [sentid]

print isent
