#18. Overlap Graphs
from Bio.Seq import Seq
from Bio import SeqIO
import itertools

seq_dict = {seq.id:seq.seq for seq in SeqIO.parse(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_grph.txt','fasta')}
#seq_dict = {'Rosalind_0498':'AAATAAA','Rosalind_2391':'AAATTTT', 'Rosalind_2323':'TTTTCCC','Rosalind_0442':'AAATCCC','Rosalind_5013':'GGGTGGG'}

k = 3

def overlap(seq1,seq2,k):
#seq1 prefix equals to seq2 suffix
    return seq1[-k:] == seq2[:k]

                                             
for s1,s2 in itertools.combinations(seq_dict,2):          #s1,s2 are keys, 2=two sequence
    s1_seq, s2_seq = seq_dict[s1], seq_dict[s2]   
    
    if overlap(s1_seq, s2_seq, k):
        print s1, s2
    
    if overlap(s2_seq, s1_seq, k):
        print s2, s1
