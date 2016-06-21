def imperative():
    f=open('marked_output.txt')
    rsent = f.readlines()
    sentid = 0
    imsent = {}
    for i in range(len(rsent)):
        if rsent[i].startswith('<Sentence'):
            sentid = rsent[i].split('"')[1]
        if len(rsent[i].split('\t'))>1 and rsent[i].split('\t')[3].startswith('<fs'):#vm tag lagana h;if vm has no suffix and next word isnt VAUX
            if (rsent[i].split('\t')[3].split(' ')[1].split('\'')[1].split(',')[-1].lower()=='ie' or rsent[i].split('\t')[3].split(' ')[1].split('\'')[1].split(',')[-1].lower()=='o' or rsent[i].split('\t')[3].split(' ')[1].split('\'')[1].split(',')[-1].lower()=='em') and (rsent[i].split('\t')[2]=='VM'):
                if sentid in imsent.keys():
                    imsent[sentid] += ['IM1']
                else:
                    imsent[sentid] = ['IM1']
                print str(sentid) + ' : ' +  rsent[i]
            if rsent[i].split('\t')[2]=='VM' and rsent[i].split('\t')[3].split(' ')[1].split('\'')[1].split(',')[-1]=='0' and rsent[i+1].split('\t')[2]!='VAUX' :
                if sentid in imsent.keys():
                    imsent[sentid] += ['IM2']
                else:
                    imsent[sentid] = ['IM2']
                print str(sentid) + ' ~ ' + rsent[i]

    return imsent
