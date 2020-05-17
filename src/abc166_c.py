def main():
  N, M = map(int, input().split())
  H_li = list(map(int, input().split()))
  AB_li = [list(map(int, input().split())) for i in range(M)]

  print(N,M,H_li,AB_li)

if __name__ == '__main__':
  main()
