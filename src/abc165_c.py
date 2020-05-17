def main():
  n, m, q = map(int, input().split())
  ans=0
  for i in range(q):
    a, b, c, d = map(int, input().split())
    if b - a == c:
      ans += d

  print(ans)

if __name__ == '__main__':
  main()
