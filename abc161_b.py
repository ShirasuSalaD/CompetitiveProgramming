data = list(map(int, input().split()))
n = data[0]
m = data[1]
li = list(map(int, input().split()))
S = sum(li)
count=0
for i in li:
  if i < S*(1 / 4 / m):
    count+=1

if n-count < m:
  print('No')
else:
  print('Yes')