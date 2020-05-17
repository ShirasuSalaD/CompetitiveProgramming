def main():
  x = int(input())
  val = 100
  year=1
  while True:
    val = int(val * 1.01)
    if x <= val:
      break
    year += 1

  print(year)

if __name__ == '__main__':
  main()
