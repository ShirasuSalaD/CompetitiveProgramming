def main():
  c = {
      'S': [0]*13,
      'H': [0]*13,
      'C': [0]*13,
      'D': [0]*13
  }
  N = int(input())
  for i in range(N):
      s, num = input().split()
      c[s][int(num)-1] = 1
  for i in["S", "H", "C", "D"]:
      for j in range(13):
          if c[i][j] == 0:
              print(i, j+1)

if __name__ == '__main__':
  main()
