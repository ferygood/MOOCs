'''
Finding a Shared Motifs
Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
Sample Output
AC
'''
from Bio import SeqIO            #BioPython
from suffix_trees import STree   #suffix_trees

dataset = open(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_lcsm (2).txt', 'r')
seq_str = [str(record.seq) for record in SeqIO.parse(dataset, "fasta")]
lcsm = STree.STree(seq_str).lcs()    #Long Common Sequence Motif

print lcsm
