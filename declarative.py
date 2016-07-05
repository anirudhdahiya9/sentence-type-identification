def declarative():    
    f=open('final_newoutput.txt')
    rsent = f.readlines()
    sentid = 0
    decsent={}

    for sent in rsent:
        if sent.startswith('<Sentence'):
            sentid = sent.split('"')[1]
        if len(sent.split('\t'))>1 and sent.split('\t')[3].startswith('<fs'):
            if sent.split('\t')[2]=='VM' and  (sent.split('\t')[3].split(' ')[1].split('\'')[1].split(',')[-1].lower()=='wa' or sent.split('\t')[3].split(' ')[1].split('\'')[1].split(',')[-1]=='yA'):
                decsent[sentid]=['D']
    return decsent
