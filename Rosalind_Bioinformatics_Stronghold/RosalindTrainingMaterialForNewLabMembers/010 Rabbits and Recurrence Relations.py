#10. Rabbits and Recurrence Relations
n,k = 29,5  #n = month, k=rabbit pairs
a,b = 0,1  #a = first month for maturation, b = gain reproductioin after one month

#xrange is same as range, however, it will return a generator(save storage)
for i in xrange(1,n):
        a,b = b,k*a+b

print b
