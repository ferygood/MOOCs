'''
Sample Dataset
GATATATGCATATACTT
ATAT
Sample Output
2 4 10
'''
#website example
seq_dna = 'GATATATGCATATACTT'
motif = 'ATAT'

length = len(seq_dna)-len(motif)+1  # define the possibile range of a motif in seq_dna
motif_len = len(motif)

for i in xrange(length):
    if seq_dna[i:i+len(motif)] == motif:
        motif_position = i+1  # python start from zero
        print motif_position

#open file
#Warning, there is a unknown bug in the Rosalind download file, therefore it is recommend you to directly copy/paste the seq and motif
dataset = open(r'').readlines()
seq_dna = dataset[0]
motif = dataset[1]

length = len(seq_dna)-len(motif)+1  # define the possibile range of a motif in seq_dna
motif_len = len(motif)

for i in xrange(length):
    if seq_dna[i:i+len(motif)] == motif:
        motif_position = i+1  # python start from zero
        print motif_position
