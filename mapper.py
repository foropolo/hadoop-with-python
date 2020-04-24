#!/usr/bin/env python3
import json
import sys

counterforkeepthenumberofbook=0
keepmiddlename=None
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    #line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    i=0
    counterof_firstnameandlastname=0
    counterofquee=0
    for word in words:
        if (word == '"authors":' ):  #flag gia na katalavainoyme oti apo edw kai pera exei onomata
            i=1 
            counterforkeepthenumberofbook=counterforkeepthenumberofbook+1
        if(word== '"n_citation":'):  #flag oti stamatane ta onomata apo dw kai pera
            i=0


        if(i==1 and word != '"authors":'):  #enwnw to onoma me to epitheto giati alliws to pairnei ksexorista
            if('"' not in word): #krataei to messaio onoma i ta messaia onomata 
                if keepmiddlename is None:
                    keepmiddlename=word
                else:
                    keepmiddlename=keepmiddlename+" "+word
                    #print(keepmiddlename)    
            elif(counterof_firstnameandlastname==0):   #krataw to onoma edw kai diwxnw ta skoupidia poy exei
                word=word.replace('[', "")
                word=word.replace('"', "")
                keepfirstname=word
                counterof_firstnameandlastname=1
            elif(counterof_firstnameandlastname==1):   #krataw to epitheto edw ,to enwnw me to onoma  kai diwxnw ta skoupidia poy exei
                word=word.replace(',', "")
                word=word.replace('"', "")
                word=word.replace(']', "")
                if keepmiddlename is None:
                    #finallyword=keepfirstname+" "+word
                    counterofquee=counterofquee+1
                    #finallyword=[keepfirstname+" "+word,counterforkeepthenumberofbook,counterofquee]
                    finallyword=keepfirstname+" "+word+" ,"+str(counterofquee)
                else :
                    #finallyword=keepfirstname+" "+keepmiddlename+" "+word
                    counterofquee=counterofquee+1
                    #finallyword=[keepfirstname+" "+keepmiddlename+" "+word,counterforkeepthenumberofbook,counterofquee]
                    finallyword=keepfirstname+" "+keepmiddlename+" "+word+" ,"+str(counterofquee)
                print ( "%s\t%s" %(finallyword, 1))
                keepmiddlename=None 
                counterof_firstnameandlastname=0

