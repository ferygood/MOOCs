'''
#10 Consensus and Profile
Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6

'''
from Bio import motifs
from Bio.Seq import Seq
instances = [Seq('ATCCAGCT'),Seq('GGGCAACT'),Seq('ATGGATCT'),Seq('AAGCAACC'),Seq('TTGGAACT'),Seq('ATGCCATT'),Seq('ATGGCACT')]
motif = motifs.create(instances)
print motif.degenerate_consensus
print motif.counts

#open with file
from Bio import motifs
from Bio.Seq import Seq
from Bio import SeqIO
seq_dict = {seq.id:seq.seq for seq in SeqIO.parse(r'','fasta')}

instances = []
for k,v in seq_dict.items():
    s = Seq(str(v))
    instances.append(s)
    
motif = motifs.create(instances)
print motif.degenerate_consensus
print motif.counts 
