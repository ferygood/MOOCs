'''
Sample Dataset:
GATGGAACTTGACTACGTAAATT
Sample Output:
GAUGGAACUUGACUACGUAAAUU
'''

from Bio.Seq import Seq

temp_seq = Seq('GATGGAACTTGACTACGTAAATT')
rna = temp_seq.transcribe()

print rna


#open with file

from Bio.Seq import Seq
temp_file = open('  ','r')
temp_seq = Seq(temp_file.readline())
rna_seq = temp_seq.transcribe()

print rna_seq


