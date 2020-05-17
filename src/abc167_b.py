def main():
  a, b, c, k = map(int, input().split())
  if a >= k:
    print(k)
  elif a + b >= k:
    print(a)
  elif a+b < k:
    print(2*a+b-k)


if __name__ == '__main__':
  main()
