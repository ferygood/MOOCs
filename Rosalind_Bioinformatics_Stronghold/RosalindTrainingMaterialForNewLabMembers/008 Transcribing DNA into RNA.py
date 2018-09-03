#8. Transcribing DNA into RNA
from Bio.Seq import Seq

temp_file = open(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_rna.txt','r')
temp_seq = Seq(temp_file.readline())
rna_seq = temp_seq.transcribe()

print rna_seq
