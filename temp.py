import sys

def main():
  input = sys.stdin.readline().rstrip

  # 5(1 つだけ)  # a = 5
  N = int(input())

  # abcde  # s = ['a', 'b', 'c', 'd', 'e']
  # s = list(input())

  # #N行複数の整数
  # data = [int(input()) for i in range(N)]

  # #N行に複数の整数
  # data = [list(map(int, input().split())) for i in range(N)]

  # # 1 2  # x = 1, y = 2
  # x, y = map(int, input().split())

  # # 1 2 3 4 5...n  # li = ['1', '2', '3', ..., 'n']
  # li = input().split()

  # # 1 2 3 4 5...n  # li = [1, 2, 3, 4, 5, ..., n]
  # li = list(map(int, input().split()))

  # # FFFTFTTFF  # li = ['FFF', 'F', '', 'FF']
  # li = input().split('T')

  #NxMの行列Aを読み取る
  # A = [[] for i in range(N)]
  # for i in range(N):
  #   A[i] = list(map(int, input().split()))


  print(N)

if __name__ == '__main__':
  main()
