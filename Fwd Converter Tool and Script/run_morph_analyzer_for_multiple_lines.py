#!/usr/bin/python
import os
import sys
import codecs


inp = sys.argv[1]
out = sys.argv[2]

count = 1
for line in codecs.open(inp, 'r', 'utf-8'):
    if line.strip() != '':
        codecs.open('temp.out', 'w', 'utf-8').write(line)
        os.system("sh $SHALLOW_PARSER_HIN/bin/sl/tokenizer/tokenizer.sh temp.out > temp1.out")
        os.system('perl -C ~/convertor-indic-1.5.2/convertor_indic.pl -f=ssf -l=hin -s=utf -t=wx -i=temp1.out -o=temp2.out')
        os.system('sh $SHALLOW_PARSER_HIN/bin/sl/morph/hin/morph.sh temp2.out>>temp3.out')
        os.system('perl -C ~/convertor-indic-1.5.2/convertor_indic.pl -f=ssf -l=hin -s=wx -t=utf -i=temp3.out>>' + out)
        os.system('rm temp.out')
        os.system('rm temp1.out')
        os.system('rm temp2.out')
        os.system('rm temp3.out')
        print("Processed Line no " + str(count))
        count += 1
