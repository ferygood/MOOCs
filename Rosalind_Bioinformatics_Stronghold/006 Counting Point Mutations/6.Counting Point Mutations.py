'''
Sample Dataset
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output
7
'''
'''
Pseudocode
1. input s and t sequence
2. count the difference of two sequence
'''
seq_file = open(' ').readlines()
s= seq_file[0]
t = seq_file[1]
count = 0

for i in xrange(len(s)):  # len(t) is also okay
    if s[i] != t[i]:
        count += 1
print count
