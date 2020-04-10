# #ルンルン数
# #隣の桁の差が1であるもの

# #1~9
# #10,11,12 21,22,23 /// 87,88,89 98,99,
# #100,101,  110,111,112,  121,122,123,

def checkLunlun(n):
  check = 0
  s=str(n)
  for i in range(len(s)-1):
    # print(i)
    if not abs(int(s[i]) - int(str(s[i+1]))) <= 1:
      check += 1
    if check > 0:
      break
  if check == 0:
    return True
  else:
    return False

K = int(input())
n = 0
count = 0
while not count == K:
  n+=1
  if checkLunlun(n):
    count += 1
print(n)
