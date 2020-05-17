def main():
  N = int(input())
  val = N % 10
  if val == 2 or val == 4 or val == 5 or val == 7 or val == 9:
    print('hon')
  elif val == 0 or val == 1 or val == 6 or val == 8:
    print('pon')
  elif val == 3:
    print('bon')


if __name__ == '__main__':
  main()
