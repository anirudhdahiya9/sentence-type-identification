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
        os.system('perl -C ~/convertor-indic-1.5.2/convertor_indic.pl -f=ssf -l=hin -s=utf -t=wx -i=temp3.out -o=temp4.out')
        os.system("sh $SHALLOW_PARSER_HIN/bin/sl/postagger/hin/postagger.sh temp4.out > temp5.out")
        #os.system('perl -C ~/convertor-indic-1.5.2/convertor_indic.pl -f=ssf -l=hin -s=utf -t=wx -i=temp5.out -o=temp6.out')
        #os.system("sh $SHALLOW_PARSER_HIN/bin/sl/chunker/hin/chunker.sh temp6.out > temp7.out")
        #os.system(" perl $SHALLOW_PARSER_HIN/bin/sl/pruning/pruning.pl --path=$SHALLOW_PARSER_HIN/bin/sl/pruning/ --resource=$SHALLOW_PARSER_HIN/data_bin/sl/pruning/mapping.dat < temp8.out | perl $SHALLOW_PARSER_HIN/bin/sl/pickonemorph/pickonemorph.pl --path=$SHALLOW_PARSER_HIN/bin/sl/pickonemorph/ | perl $SHALLOW_PARSER_HIN/bin/sl/headcomputation/headcomputation.pl --path=$SHALLOW_PARSER_HIN/bin/sl/headcomputation/ | perl $SHALLOW_PARSER_HIN/bin/sl/vibhakticomputation/vibhakticomputation.pl --path=$SHALLOW_PARSER_HIN/bin/sl/vibhakticomputation/ | perl $SHALLOW_PARSER_HIN/bin/sl/vibhakticomputation/printinput.pl")
        #os.system('perl -C ~/convertor-indic-1.5.2/convertor_indic.pl -f=ssf -l=hin -s=utf -t=wx -i=temp9.out -o=temp10.out')
        os.system('perl -C ~/convertor-indic-1.5.2/convertor_indic.pl -f=ssf -l=hin -s=wx -t=utf -i=temp5.out>>' + out)
        os.system('rm temp.out')
        os.system('rm temp1.out')
        os.system('rm temp2.out')
        os.system('rm temp3.out')
        os.system('rm temp4.out')
        os.system('rm temp5.out')
        os.system('rm temp6.out')
        os.system('rm temp7.out')
        #os.system('rm temp8.out')
        #os.system('rm temp9.out')
        print("Processed Line no " + str(count))
        count += 1
