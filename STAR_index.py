import os

directory ='/home/users/ellenrichards/'
genomeDir = '/home/users/ellenrichards/s009_c61203_g3_i2/gd'
filename = 's009_c61203_g3_i2.fasta'

#indexingstar='\"STAR --runThreadN 1 --runMode genomeGenerate --genomeDir \"' + genomeDir + '\" --genomeFastaFiles \"' + directory + filename  + '\" --genomeSAindexNbases 2\"'
indexingstar = f'STAR --runThreadN 1 --runMode genomeGenerate --genomeDir  "{genomeDir}" --genomeFastaFiles "{directory}{filename}" --genomeSAindexNbases 2'
indexingstar = f"'{indexingstar}'"
indexing = f"SGE_Batch -r 'genome_dir' -c {indexingstar} -P1"

os.system(indexing)
