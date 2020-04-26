def main():
  s = tuple(input())
  count = 0
  for j in range(4,len(s)+1):
    for i in range(len(s) - j + 1):
      if int(''.join(s[i:i + j])) % 2019 == 0:
        count += 1
      if len(s) - j < 4:
        break
  # count = [1 for j in range(4, len(s)+1) for i in range(len(s)-j+1) if int(''.join(s[i:i + j])) % 2019 == 0]
  # print(sum(count))
  print(count)

if __name__ == '__main__':
  main()
