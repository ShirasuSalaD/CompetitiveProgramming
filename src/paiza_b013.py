import math

def main():
  a, b, c = map(int, input().split())
  N = int(input())
  val = 0

  for i in range(N):
    h,m = map(int, input().split())
    eki = h * 60 + m
    minute = eki
    minute += b+c
    if minute < 540:
      val = eki - a
    else:
      break

  print('{0:0>2d}:{1:0>2d}'.format(math.floor(val / 60), val % 60))

if __name__ == '__main__':
  main()
