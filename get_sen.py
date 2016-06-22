def get_sen():
    import re
    tagsent={}
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
            tagsent[str(l+1)]=[match.group(2)]
            continue
        #fsent+=[rsent[l]+'\n']

    return tagsent

    '''
    f=open('outsent.txt','w')
    f.writelines(fsent)'''
