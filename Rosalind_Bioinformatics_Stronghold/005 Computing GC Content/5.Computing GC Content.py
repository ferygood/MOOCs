'''
Sample Dataset:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT

Sample Output:
Rosalind_0808
60.919540
'''
'''
Pseudocode:
1. Split the title and sequence to dict
2. calculate GC content and find the highest one
3. output the title and GC content
'''
from Bio import SeqIO
from Bio.SeqUtils import GC

seq_dict = {seq.id : GC(seq.seq) for seq in SeqIO.parse(r'D:\R316yao\rosalind\rosalind_gc.txt', "fasta")}

highest_gc = max(seq_dict.values())

for k,v in seq_dict.iteritems():
    if v == highest_gc:
        print k
        print v


