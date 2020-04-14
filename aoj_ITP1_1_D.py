#時計

import sys


def main():
  input = sys.stdin.readline().rstrip

  S = int(input())
  h, m, s = 0, 0, 0
  h = int(S / 60 / 60)
  m = int(S / 60 % 60)
  s = S % 60
  print(str(h)+':'+str(m)+':'+str(s))


if __name__ == '__main__':
  main()
