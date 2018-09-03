'''
Sample Dataset
2 2 2

Sample Output
0.7833

'''
'''
Pseudocode:
(1) k (AA), m(Aa), n(aa), any two of them can mate. Calculate the phenotype(Aa) or (AA)
(2) randomly selected two of them
(3) calculate probability (1-recessive)
'''
k=2
m=2
n=2
total_population = float(k + m + n)  #for float calculation
AaAa_rec = 0.25 * (m / total_population) * ((m-1)/(total_population-1)) 
Aaaa_rec = 0.5 * (m / total_population) * (n)/(total_population-1) + 0.5 * (n/total_population) * (m/(total_population-1)) 
# notice have two possibility Aaxaa or aaxAa
aaaa_rec = 1 * n/total_population * (n-1)/(total_population-1)

dominant_allele = 1-(AaAa_rec+Aaaa_rec+aaaa_rec)
print total_population
print AaAa_rec
print Aaaa_rec
print aaaa_rec
print dominant_allele 





