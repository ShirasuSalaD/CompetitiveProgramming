s = list(map(int, input().split()))
c = s[-1]
s.pop(-1)
s.insert(0,c)
print(*s)
