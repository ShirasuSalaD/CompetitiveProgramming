n = int(input())
li = [input().split() for i in range(n)]

l_in_B = [s for s in li if 'B' in s]
l_in_R = [s for s in li if 'R' in s]


l_B = []
for j in l_in_B:
  l_B.append(int(j[0]))

l_B = sorted(l_B)

l_R = []
for j in l_in_R:
  l_R.append(int(j[0]))

l_R = sorted(l_R)

for i in l_R:
  print(i)

for i in l_B:
  print(i)
