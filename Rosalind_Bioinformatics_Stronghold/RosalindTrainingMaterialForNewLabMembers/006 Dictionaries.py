#6 Dictionaries
from collections import Counter

data= open(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_ini6.txt','r').read().split()
data_dict = Counter(data)
print data_dict
print
for key, value in data_dict.items():
    print key,value
    
'''
�H�U code �J��ܵu���ƪ��r�|���ƭp��A��p�p�� in ���ƶq�ɡAinternational �]���� in �ҥH�]�|�� in+1�A�ҥH�|�y�����׿��~
data_dict = {}
for word in data.split():
    data_dict[word] = data.count(word)    #�Q�ηs�W dictionary ���ت��S��
print data_dict
print 

for key,value in data_dict.items():
    print key,value 
'''
