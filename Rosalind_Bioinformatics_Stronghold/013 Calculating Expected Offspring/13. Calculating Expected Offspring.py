'''
Genotype pairing
1.AA-AA
2.AA-Aa
3.AA-aa
4.Aa-Aa
5.Aa-aa
6.aa-aa

Sample Dataset
1 0 0 1 0 1

Sample Output
3.5
'''
#probabilty of dominant phenotype in each group
prob = {'p0':1, 'p1':1, 'p2':1, 'p3':0.75, 'p4':0.5, 'p5':0}
input_data = [1,0,0,1,0,1]
expect_value=2*(input_data[0] * prob['p0'] + input_data[1] * prob['p1'] + input_data[2] * prob['p2'] 
           + input_data[3] * prob['p3'] + input_data[4] * prob['p4'] + input_data[5] * prob['p5'])

print expect_value
