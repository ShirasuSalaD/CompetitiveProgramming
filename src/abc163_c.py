def main():
  N = int(input())
  li = list(map(int, input().split()))
  now_num = 0
  count = 0

  for val in li:
    now_num = val
    for i in range(N - 1):
      while now_num == li[i]:
        count += 1
        break

      if now_num != li[i]:
        # print(now_num, li[i])
        print(count)

if __name__ == '__main__':
  main()
