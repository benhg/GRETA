import time
import os 
import sys

from data_generation import generate_data
from STAR_index import star_index
from STAR_align import star_align

proteomefile = sys.argv[1]
directory = '/home/users/ellenrichards'

generate_data(proteomefile)

for filename in open("filenames.txt"):
    mvalue = str(filename)
    mvalue = mvalue.split("/n")[0]
    mvalue= mvalue.split('.fasta')[0]

    svalue = filename.split("_")[0]
    strsvalue = str(svalue.split('s')[1])
    svalue = int(strsvalue)

    os.makedirs(mvalue)
    genomeDir = f"{mvalue}/gd"
    os.makedirs(genomeDir)

    os.chdir(directory + mvalue)  #change directory to mvalue folder we just made

    star_index(directory, genomeDir, filename)

    #wait until done
    while not 'Log.out':
        wait(15) 
    
    star_align(directory, mvalue, strsvalue, genomeDir)
    
    #wait until output is ready! 

    output = 0
    uniquely = os.popen("awk 'FNR == 9{print $6}' " + strsvalue + "Log.final.out").read()
    if uniquely == 0 : 
        uniquely = 1
    multi = os.popen("awk 'FNR == 24{print $9}' " + strsvalue + "Log.final.out").read()
    if multi == 0: 
        multi = 1
    totalreads = os.popen("awk 'FNR == 6{print $6}' " + strsvalue+ "Log.final.out").read()

    if originaloutput >= threshold: 
        uniquelyC = 'NO'
        multiC = 'NO'
        totalreadsC = 'NO'
        percRatio = 'NO'
        csv_row = {"filename": str(filename), "uniquely": str(uniquely), "multi": str(multi), "totalReads": str(totalreads), "uniquelyAGAINST": str(uniquelyC), "multiAGAINST": str(multiC), "totalReadsAGAINST": str(totalreadsC), "percratio": str(percRatio)}
        csv_writer.writerow(csv_row)
        output = 1
    if svalue <12: counter = 1
    elif (svalue >=12): counter = 15

    while output  == 0 and counter > 0:
        os.system("echo" + filename + " >> maybehopper.txt")
        if counter == svalue: 
            counter +=1
        if counter == 20 or counter == 7: 
            counter = 0
        elif counter == 17: 
            counter = 19

        strcounter = str(counter)

        star_align(directory, mvalue, strcounter, genomeDir)

        threshold = 1000
        uniquelyC = os.popen("awk 'FNR == 9{print $6}' " + strcounter + "Log.final.out").read()
        if uniquelyC == 0: 
            uniquelyC = 1
        multiC =  os.popen("awk 'FNR == 24{print $9}' " + strcounter + "Log.final.out").read()
        if multiC == 0: 
            multiC = 1
        allC = multiC + uniquelyC
        totalreadsC = os.popen("awk 'FNR == 6{print $6}' " + strcounter + "Log.final.out").read()
        percRatio = 
        
        if allC > threshold and (allC/originaloutput)>100: 
            #OUTPUT
            os.system("echo " + filename + ">> hopper.txt")
        else:
            if counter == 17: 
                counter = 19
            elif counter == 20 or counter == 7: 
                counter = 0
            else: 
                counter = counter + 1

    if output == 0:
        #LIST AS NEVER
        pass
