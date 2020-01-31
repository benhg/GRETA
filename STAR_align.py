import os

directory = '/home/users/ellenrichards/'
mvalue = 's009_c61203_g3_i2'
strsvalue = "1"
genomeDir = '/home/users/ellenrichards/s009_c61203_g3_i2/gd/'
rawread1 = 'lane1-s009-indexRPI9-GATCAG-MP2fe_S9_L001_R1_001.fastq'
rawread2 = 'lane1-s009-indexRPI9-GATCAG-MP2fe_S9_L001_R2_001.fastq'

def star_align(directory, mvalue, strsvalue, genomeDir):
 
    outfilenameprefix = directory + mvalue +"/"+ strsvalue

    alignstar= f'STAR --runMode alignReads --runThreadN 15 --genomeDir "{genomeDir}"  --readFilesIn /home/users/ellenrichards/binfordlab/raw_reads/"{rawread1}"  /home/users/ellenrichards/binfordlab/raw_reads/"{rawread2}" --outFileNamePrefix "{outfilenameprefix}" --outSAMtype BAM SortedByCoordinate --limitBAMsortRAM 40000000000'
    alignstar = f"'{alignstar}'"

    align = "SGE_Batch -r align" + strsvalue + " -c " + alignstar + " -P 15"

    os.system(align)
