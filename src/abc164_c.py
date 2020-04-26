def main():
  N = int(input())
  li = [input() for i in range(N)]
  print(len(list(set(li))))


if __name__ == '__main__':
  main()
