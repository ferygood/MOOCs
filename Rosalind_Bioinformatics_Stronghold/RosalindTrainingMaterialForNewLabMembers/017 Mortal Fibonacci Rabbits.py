#17. Mortal Fibonacci Rabbits
# n = number of months # m = rabbit can live for m month
n,m = 88,19  

#Keys=months, Values=rabbit numbers, From the third month, F(n) = F(n-1) + F(n-2)
rab_num = {1:1,2:1}

for i in range(3,n+1):
    if i <= m:
        rab_num[i] = rab_num[i-1] + rab_num[i-2]
    elif i == m + 1 or i == m + 2 :
        rab_num[i] = rab_num[i-1] + rab_num[i-2] - 1
    else:
        rab_num[i] = rab_num[i-1] + rab_num[i-2] - rab_num[i-(m+1)]            #rab_num[i-(m+1)] 為需要扣掉的死亡的兔子數

print rab_num[n] 
