data = list(map(int, input().split()))
N = data[0]
K = data[1]

N=N%K

start = N
ans = 0

def hoge(i, j):
  return abs(i - j)

ans = hoge(N, K)

if start <= ans:
  print(start)
else:
  while ans >= hoge(ans, K):
    ans = hoge(ans, K)
  print(ans)