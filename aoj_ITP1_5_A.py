#長方形の描画

while True:
  x, y = map(int, input().split())
  if x == 0 and y == 0:
      break
  for i in range(x):
    print('#' * y)

  print('')
