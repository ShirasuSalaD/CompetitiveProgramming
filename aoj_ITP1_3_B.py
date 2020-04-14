#テストケースの出力

def main():
  i=1
  while True:
    data = int(input())
    if data == 0:
      break
    else:
      print('Case %d: %d' % (i, data))
      i+=1

if __name__ == '__main__':
  main()
