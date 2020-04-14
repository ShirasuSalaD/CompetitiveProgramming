#長方形の面積と周の長さ

import sys

def main():
  input = sys.stdin.readline().rstrip

  a,b = map(int, input().split())
  print(a*b, (a+b)*2)


if __name__ == '__main__':
  main()
