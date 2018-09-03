'''
Sample Dataset:
AAAACCCGGT
Sample Output:
ACCGGGTTTT
'''
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

dna = Seq('AAAACCCGGT',generic_dna)
rc_dna = dna.reverse_complement()

print rc_dna


#Open with file

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

seq_file = open(r' ','r').readline()
dna = Seq(seq_file, generic_dna)
rc_dna = dna.reverse_complement()

print rc_dna
