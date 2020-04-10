import math

data = input().split()
N = int(data[0])
Q = int(data[1])

a_li = input().split()
# a_li = list(map(int, a_li))

s_li = input().split()
# s_li = list(map(int, s_li))

result = []
for s_val in s_li:
  x = int(s_val)
  # print(x)
  for a_val in a_li:
    if not int(a_val) % x == 0:
      x = math.gcd(x, int(a_val))
    # print(x)
    if x == 1:
      x = a_li.index(a_val)+1
      # print(x)
      break
  result.append(x)

for i in result:
  print(i)
