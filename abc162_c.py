import math
# from functools import reduce


# def gcd(*numbers):
#     return reduce(math.gcd, numbers)


# def gcd_list(numbers):
#     return reduce(math.gcd, numbers)

N = int(input())

sum = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    for k in range(1, N + 1):
      # if i == j or j==k:
      #   hoge = gcd(i, k)
      # elif i == k:
      #   hoge = gcd(j, k)
      # elif i == j == k:
      #   hoge = 1
      # else:
      #   hoge = gcd(i, j, k)
      hoge = math.gcd(i,math.gcd(j,k))
      sum+=hoge

print(sum)
