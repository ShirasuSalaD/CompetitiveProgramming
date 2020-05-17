def main():
  P_1, P_2, P_3, k = map(int, input().split())
  ans = []
  for c in range(5):
      for b in range(5):
          for a in range(5):
              # ans.append(1 * (P_1 ** a) * (P_2 ** b) * (P_3 ** c))
              val = 1 * (P_1 ** a) * (P_2 ** b) * (P_3 ** c)
              print(a, b, c)
              print(val)
              ans.append(val)


  ans.sort()
  print(ans[k-1])

if __name__ == '__main__':
  main()
