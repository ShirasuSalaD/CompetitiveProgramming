from math import gcd

N = int(input())

sum = 0
for i in range(1, N+1):
  for j in range(1, N + 1):
    x=gcd(i,j)
    for k in range(1, N + 1):
      hoge = gcd(x,k)
      sum+=hoge

print(sum)
