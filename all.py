import os
import sys
import math
import time
import fnmatch
import datetime
from datetime import datetime 
import csv

from data_generation import generate_data
from STAR_index import star_index
from STAR_align import star_align

proteomefile = sys.argv[1]
directory = '/home/users/ellenrichards/'
threshold = 1000

generate_data(proteomefile)

os.system("touch hopper.txt")
os.system("touch final.txt")
os.system("touch never.txt")
os.system("touch maybehopper.txt")
os.system("touch index_hopping_output.txt")

#csv_filename = "index_hopping_output.csv"
#csv_fh = open(csv_filename, "write")
#csv_writer = csv.DictWriter(csv_fh, fieldnames=["filename", "uniquely", "multi", "totalReads", "uniquelyAGAINST", "multiAGAINST", "totalReadsAGAINST", "percratio"])
#csv_row = {"filename": "filename ", "uniquely": "uniquely ", "multi": "multi ", "totalReads": "totalreads ", "uniquelyAGAINST": "uniquelyC ", "multiAGAINST": "multiC ", "totalReadsAGAINST": "totalreadsC ", "percratio": "percRatio "}
#csv_writer.writerow(csv_row)
os.system("echo 'filename  uniquely  multi  totalReads  uniquelyAGAINST  multiAGAINST  totalreadsAGAINST  percRatio'  >> index_hopping_output.txt")

for filename in open("filenames.txt"):
    os.chdir(directory)
    mvalue = str(filename)
    mvalue = mvalue.split("/n")[0]
    mvalue= mvalue.split('.fasta')[0]

    svalue = filename.split("_")[0]
    svalue = str(svalue.split('s')[1])
    svalue  = int(svalue)
    strsvalue = str(svalue)

    os.makedirs(mvalue)
    genomeDir = f"{directory}{mvalue}/gd"
    os.makedirs(genomeDir)

    os.chdir(directory + mvalue)  #change directory to mvalue folder we just made

    star_index(directory, genomeDir, filename)

    #wait until done
    while not os.path.exists("Log.out"): 
        time.sleep(5) 
            
    star_align(directory, mvalue, strsvalue, genomeDir)
    
    #wait until output is ready! 

    while not os.path.exists(strsvalue + "Log.final.out" ): 
        time.sleep(15) 
        
    output = 0

    uniquely = os.popen("awk 'FNR == 9{print $6}' " + strsvalue + "Log.final.out").read()
    if uniquely == 0 : 
        uniquely = '1'
    uniquely = int(uniquely)

    multi = os.popen("awk 'FNR == 24{print $9}' " + strsvalue + "Log.final.out").read()
    if multi == '0': 
        multi = '1'
    multi = int(multi)

    totalreads = os.popen("awk 'FNR == 6{print $6}' " + strsvalue+ "Log.final.out").read()

    if uniquely + multi >= threshold:
        os.system("echo " + filename + ">> final.txt") 
        output = 1
        uniquelyC = 'NO'
        multiC = 'NO'
        totalreadsC = 'NO'
        percRatio = 'NO'
#        csv_row = {"filename": str(filename), "uniquely": str(uniquely), "multi": str(multi), "totalReads": str(totalreads), "uniquelyAGAINST": str(uniquelyC), "multiAGAINST": str(multiC), "totalReadsAGAINST": str(totalreadsC), "percratio": str(percRatio)}
#        csv_writer.writerow(csv_row)


    if svalue <12: 
        counter = 1
    else: 
        counter = 15

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
        if uniquelyC == '0': 
            uniquelyC = '1'
        uniquelyC = int(uniquelyC)

        multiC =  os.popen("awk 'FNR == 24{print $9}' " + strcounter + "Log.final.out").read()
        if multiC == '0': 
            multiC = '1'
        multiC = int(multiC)

        totalreadsC = os.popen("awk 'FNR == 6{print $6}' " + strcounter + "Log.final.out").read()

        percRatio = (multiC + uniquelyC)/(multi + uniquely)
        
        if (multiC + uniquelyC) > threshold and percRatio > 100:
            output = 1
            os.system("echo " + filename + ">> hopper.txt")
        else:
            if counter == 17: 
                counter = 19
            elif counter == 20 or counter == 7: 
                counter = 0
            else: 
                counter = counter + 1


    if output == 1: #it needs to be added to a file
 #       csv_row = {"filename": str(filename), "uniquely": str(uniquely), "multi": str(multi), "totalReads": str(totalreads), "uniquelyAGAINST": str(uniquelyC), "multiAGAINST": str(multiC), "totalReadsAGAINST": str(totalreadsC), "percratio": str(percRatio)}
  #      csv_writer.writerow(csv_row)
        os.system("echo " + str(filename) + "  " +  str(uniquely) + "  " + str(multi) + "  " + str(totalreads) + "  " +  str(uniquelyC) + "  " +   str(multiC) + "  " + str(totalreadsC) + "  " +  str(percRatio)   + "  >> ../index_hopping_output.txt")


    if output == 0:
        os.system("echo " + filename + ">> never.txt")
