def interrogative():
    f=open('marked_output.txt')
    rsent = f.readlines()
    #improve
    sentid = 0
    isent = {}

    for i in range(len(rsent)):
        if rsent[i].startswith('<Sentence'):
            sentid = rsent[i].split('"')[1]
        if len(rsent[i].split('\t'))>1:
            if (rsent[i].split('\t')[1]=='?') and ((rsent[i+2].startswith('</Sentence')) or ((rsent[i+1].split('\t')[1]=='"' and rsent[i+3].startswith('</Sentence')))):
                print sentid
                if sentid not in isent.keys():
                    isent[sentid]=['I1']
                else:
                    isent[sentid]+=['I1']
            if rsent[i].split('\t')[1]=='\xe0\xa4\x95\xe0\xa4\xb9\xe0\xa4\xbe\xe0\xa4\x81' or rsent[i].split('\t')[1]=='\xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xbe' or rsent[i].split('\t')[1]=='\xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa5\x8b\xe0\xa4\x82' or rsent[i].split('\t')[1]=='\xe0\xa4\x95\xe0\xa5\x8c\xe0\xa4\xa8' or rsent[i].split('\t')[1]=='\xe0\xa4\x95\xe0\xa4\xac' or rsent[i].split('\t')[1]=='\xe0\xa4\x95\xe0\xa4\xbf\xe0\xa4\xa4\xe0\xa4\xa8\xe0\xa5\x87' or rsent[i].split('\t')[1]=='\xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87' :
                print sentid
                if sentid not in isent.keys():
                    isent[sentid]=['I2']
                else:
                    isent[sentid]+=['I2']

    return isent
