#長方形の中の円

import sys

def main():
  input = sys.stdin.readline().rstrip

  W, H, x, y, r = map(int, input().split())
  if x - r < 0 or W < x + r or y - r < 0 or H < y + r:
    print('No')
  else:
    print('Yes')

if __name__ == '__main__':
  main()
