def main():
  N = int(input())
  a_list = list(map(int, input().split()))
  count = 0

  # def divide(n):
  #   return n // 2

  # while True:
  #   a_list = list(map(divide, a_list))
  #   print(a_list)
  #   if a_list.count(1) > 0:
  #     break
  #   count += 1

  flag = 0
  while flag == 0:
    for i in range(N):
        if a_list[i] % 2 == 0:
            a_list[i] = a_list[i]/2
        else:
            flag = 1
    if flag == 0:
        count += 1

  print(count)




if __name__ == '__main__':
  main()
