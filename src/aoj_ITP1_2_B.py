#範囲

import sys

def main():
  input = sys.stdin.readline().rstrip

  a, b, c = map(int, input().split())

  if a < b < c:
    print('Yes')
  else:
    print('No')


if __name__ == '__main__':
  main()
