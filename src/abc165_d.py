import math

def main():
  a, b, n = map(int, input().split())
  # hoge = []
  # for x in range(n):
  #   val = math.floor(a * x / b) - a * math.floor(x / b)
  #   hoge.append(val)
  #   print(val)
  # print(max(hoge))
  val = math.floor(a * math.trunc(n) / b) - a * math.floor(math.trunc(n) / b)
  print(val)

if __name__ == '__main__':
  main()
