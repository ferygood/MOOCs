#5 Working with Files
data = open(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_ini5.txt','r').readlines()

for k in range(0,1001):
    if k%2 != 0:
        print data[k].strip()
