#Introduction to the Bioinformatics Armory
from Bio.Seq import Seq
Sample_dataset = Seq('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
# convert to Seq(), so Biopython can manipulate
print Sample_dataset.count('A'),Sample_dataset.count('C'),Sample_dataset.count('G'),Sample_dataset.count('T')

#open with file
seq = Seq(open(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_ini.txt','r').read())
print seq.count('A'),seq.count('C'),seq.count('G'),seq.count('T')
