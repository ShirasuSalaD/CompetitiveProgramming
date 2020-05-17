import itertools

def main():
  n, k = map(int, input().split())
  d_li = []
  a_li = []
  for i in range(k):
    d_li.append(int(input()))
    a_li.append(list(map(int, input().split())))

  res = itertools.chain(*a_li)
  res = list(res)
  print(n-len(list(set(res))))

if __name__ == '__main__':
  main()
