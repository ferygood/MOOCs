#9. Complementing a Strand of DNA
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

seq_file = open(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_revc.txt','r').readline()
dna = Seq(seq_file, generic_dna)
rc_dna = dna.reverse_complement()

print rc_dna
