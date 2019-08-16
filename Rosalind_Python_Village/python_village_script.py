#!usr/bin/python
#coding=utf-8
#python 3.6.5
#Rosalind_Python_Village

# 1. Installing Python
import this

# 2. Variables and Some Arithmetic
# input: 3,5
# output: 3^2 + 5^2 = 34

def square_sum(*args):
# This function add all the input**2 to sum     
    sum = 0
    for n in args:
        sum = sum + n**2
    return sum

print (square_sum(3,4,5)) #50
    
# 3. Strings and Lists
def slice_string(input_string,a,b,c,d):
    #slice a string in two range
    string_1 = input_string[a:b+1]
    string_2 = input_string[c:d+1]
    output_string = string_1 + ' ' + string_2
    return output_string

#input a long string
with open('rosalind_ini3.txt','r') as string_200:
    string_read = str(string_200.read())
    print (slice_string(string_read, 11, 20, 65, 74)) #Hyperoodon ampullatus
    
# 4. Conditions and Loops
# two positive integers a and b (a<b<10000)
# The sum of all odd integers from a through b, inclusively
def sum_odd(a,b):
    sum = 0
    for n in range(a,b+1):
        if n % 2 == 1:
            sum = sum + n
    return sum

print (sum_odd(100,200)) #7500

# 5. Working with Files
# a file containing at most 1000 lines
# return a file containing all even-numbered lines, 
# assume 1-based numbering of lines
with open('rosalind_ini5.txt', 'r') as f:
    paragraph = f.readlines()

# you have to create an empty text file first
output_file = open('rosalind_ini5_output.txt', 'w')
    
def even_numbered_line(paragraph_readlines, output_file_name):
    for i in range(len(paragraph_readlines)):
        if i % 2 == 1:
            output_file_name.write(paragraph_readlines[i])
    return output_file_name.close()
        
even_numbered_line(paragraph, output_file)
 
# 6. Dictionaries
with open('rosalind_ini6.txt', 'r+') as f:
    string_content = f.readline().rstrip()
    print (string_content)

dict = {}
for i in string_content.split(' '):
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

print (dict)

for k,v in dict.items():
    print(k,v)