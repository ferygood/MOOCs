#7. Counting DNA Nucleotides
from collections import Counter
seq_file = open(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_dna.txt','r').readline()
counts = Counter(seq_file)

print counts['A'],counts['C'],counts['G'],counts['T']
