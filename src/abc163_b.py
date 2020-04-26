def main():
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    s = 0
    for i in range(M):
      s += li[i]

    if s <= N:
      print(N-s)
    else:
      print('-1')

if __name__ == '__main__':
  main()
