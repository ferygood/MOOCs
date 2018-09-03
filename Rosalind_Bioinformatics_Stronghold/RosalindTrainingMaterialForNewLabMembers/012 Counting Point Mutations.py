#12. Counting Point Mutations
seq_file = open(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_hamm.txt','r').readlines()
s= seq_file[0]
t = seq_file[1]
count = 0

for i in xrange(len(s)):  # len(t) is also okay
    if s[i] != t[i]:
        count += 1
print count
