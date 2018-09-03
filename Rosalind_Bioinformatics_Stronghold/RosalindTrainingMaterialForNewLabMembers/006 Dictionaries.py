#6 Dictionaries
from collections import Counter

data= open(r'C:\Users\Yao-Chung Chen\Downloads\rosalind_ini6.txt','r').read().split()
data_dict = Counter(data)
print data_dict
print
for key, value in data_dict.items():
    print key,value
    
'''
以下 code 遇到很短重複的字會重複計算，比如計算 in 的數量時，international 因為有 in 所以也會讓 in+1，所以會造成答案錯誤
data_dict = {}
for word in data.split():
    data_dict[word] = data.count(word)    #利用新增 dictionary 項目的特性
print data_dict
print 

for key,value in data_dict.items():
    print key,value 
'''
