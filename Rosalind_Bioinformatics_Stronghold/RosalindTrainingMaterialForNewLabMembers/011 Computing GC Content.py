#11. Computing GC Content
from Bio import SeqIO
from Bio.SeqUtils import GC

seq_dict = {seq.id : GC(seq.seq) for seq in SeqIO.parse(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_gc.txt','fasta')}

highest_gc = max(seq_dict.values())

for k,v in seq_dict.iteritems():
    if v == highest_gc:
        print k
        print v
