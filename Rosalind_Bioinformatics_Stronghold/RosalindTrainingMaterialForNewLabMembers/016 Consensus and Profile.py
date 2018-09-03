#16. Consensus and Profile
from Bio import motifs
from Bio.Seq import Seq
from Bio import SeqIO
seq_dict = {seq.id:seq.seq for seq in SeqIO.parse(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_cons.txt','fasta')}

instances = []
for k,v in seq_dict.items():
    s = Seq(str(v))
    instances.append(s)
    
motif = motifs.create(instances)
print motif.degenerate_consensus
print motif.counts 
