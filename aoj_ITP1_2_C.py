#3つの数の整列

import sys

def main():
  input = sys.stdin.readline().rstrip

  li = list(map(int, input().split()))

  print(*sorted(li))


if __name__ == '__main__':
  main()
