#大小関係

import sys

def main():
  input = sys.stdin.readline().rstrip

  a, b = map(int, input().split())

  if a < b:
    print('a < b')
  elif a > b:
    print('a > b')
  elif a == b:
    print('a == b')


if __name__ == '__main__':
  main()
