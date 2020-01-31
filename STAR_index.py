import os

def star_index(directory, genomeDir, filename):
  
  #indexingstar='\"STAR --runThreadN 1 --runMode genomeGenerate --genomeDir \"' + genomeDir + '\" --genomeFastaFiles \"' + directory + filename  + '\" --genomeSAindexNbases 2\"'
  indexingstar = f'STAR --runThreadN 1 --runMode genomeGenerate --genomeDir  "{genomeDir}" --genomeFastaFiles "{directory}{filename}" --genomeSAindexNbases 2'
  indexingstar = f"'{indexingstar}'"
  indexing = f"SGE_Batch -r 'genome_dir' -c {indexingstar} -P1"

  os.system(indexing)
