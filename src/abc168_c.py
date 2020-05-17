import math
def main():
  n, m = map(int, input().split())
  data = [list(map(int, input().split())) for i in range(m)]
  print(n, m, data)

if __name__ == '__main__':
  main()
