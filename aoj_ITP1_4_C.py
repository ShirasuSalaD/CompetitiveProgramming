#計算機

while True:
  a, ope, b = input().split()
  result = 0
  if ope == '?':
    break

  if ope == '+':
    result = int(a) + int(b)
  elif ope == '-':
    result = int(a) - int(b)
  elif ope == '*':
    result = int(a) * int(b)
  elif ope == '/':
    result = int(int(a) / int(b))
  print(result)
