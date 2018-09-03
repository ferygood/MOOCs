#4 Conditions and Loops
a,b = 4813,9189
sum_odd = 0
for i in range(a,b+1):
    if i%2 != 0:
        sum_odd = sum_odd + i
print sum_odd
