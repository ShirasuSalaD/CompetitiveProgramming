import sys

def main():
  input = sys.stdin.readline().rstrip

  # abcde  # s = ['a', 'b', 'c', 'd', 'e']
  s = list(input())
  # 5(1 つだけ)  # a = 5
  N = int(input())
  #N行複数の整数
  data = [int(input()) for i in range(N)]
  # 1 2  # x = 1, y = 2
  x, y = map(int, input().split())
  # 1 2 3 4 5...n  # li = ['1', '2', '3', ..., 'n']
  li = input().split()
  # 1 2 3 4 5...n  # li = [1, 2, 3, 4, 5, ..., n]
  li = list(map(int, input().split()))
  # FFFTFTTFF  # li = ['FFF', 'F', '', 'FF']
  li = input().split('T')

  print()

if __name__ == '__main__':
    main()