#フレームの描画

while True:
  x, y = map(int, input().split())
  if x == 0 and y == 0:
      break
  for i in range(x):
    if i == 0 or i==x-1:
      print('#' * y)
    else:
      print('#%s#' %('.'*(y-2)))

  print('')
