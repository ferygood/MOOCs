'''
Sample Dataset
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output
20 12 17 21
'''

import collections

seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
counts = collections.Counter(seq)

print counts['A'], counts['C'], counts['G'], counts['T']


#open with files

import collections

seq_file = open('','r')
seq_nt = seq_file.readline()
counts = collections.Counter(seq_nt)

print counts['A'], counts['C'], counts['G'],counts['T']



