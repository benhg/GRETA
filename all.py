import time
import os 
import sys

from .data_generation import generate_data

proteomefile = sys.argv[1]

generate_data(proteomefile)

#data_generate.py creates filenames.txt

for filename in open(filenames.txt):
    mvalue = str(filename)
    mvalue = mvalue.split("/n")[0]
    mvalue= mvalue.split('.fasta')[0]

    svalue = filename.split("_")[0]
    strsvalue = str(svalue.split('s')[1])
    svalue = int(strsvalue)

    os.sys("mkdir " + mvalue)
    os.sys("mkdir " + mvalue + "/gd")

    #change directory to mvalue folder we just made

    #CALL STAR_index.py(mvalue)

    #wait until done

    #CALL STAR_align.py(mvalue, svalue)
    output = 0

    if originaloutput >= threshold: 
        #CALL AGGREGATE????
        #OUTPUT
        output = 1
    if svalue <12: counter = 1
    elif (svalue >=12): counter = 15

    while output == 0 and counter > 0:
        #LIST AS MAYBEHOPPER?
        if counter == svalue: counter +=1
        if counter == 20 or counter == 7: counter = 0
        elif counter == 17: counter = 19

        strcounter = str(counter)

        #CALL STAR_align.py(mvalue, strcounter), output newoutput

        if newoutput > threshold and (newoutput/originaloutput)>100: 
            #OUTPUT
            #LIST AS DEFINITE HOPPER

        else :
            if counter == 17: counter = 19
            elif counter == 20 or counter == 7: counter = 0
            else : counter = counter + 1

    if output == 0:
        #LIST AS NEVER
