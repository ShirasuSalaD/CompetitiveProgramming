def main():
  k = int(input())
  s = input()
  val = len(s)-k
  if val > 0:
    print(s[:k] + '...')
  else:
    print(s)


if __name__ == '__main__':
  main()
