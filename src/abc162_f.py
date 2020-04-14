N = int(input())
li = list(map(int, input().split()))
num = int(N / 2)

if N % 2 == 0:
  hoge1 = sum(li[0::2])
  hoge2 = sum(li[1::2])
  # if hoge1 > hoge2:
  #   ans = hoge1
  # else:
  #   ans = hoge2
  ans=max([hoge1,hoge2])
else: #どこか1箇所だけ2つ飛ばしがある場合を用意できない...
  hoge1 = sum(li[0::2])
  hoge2 = sum(li[1::2])
  hoge3 = sum(li[2::2])
  ans = max([hoge1,hoge2,hoge3])

print(ans)
