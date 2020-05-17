def main():
  n, k = map(int, input().split())
  a_list = list(map(int, input().split()))

  #初期位置
  count=0
  now_point = 1
  root_list = [a_list[0]]

  #ループをチェックする
  for i in range(1000000):
    # print(now_point,root_list,count)
    now_point = a_list[now_point - 1]
    count += 1
    if a_list[now_point - 1] in root_list:
      loop_list = root_list[root_list.index(a_list[now_point - 1]):]
      first_num = len(root_list[:root_list.index(a_list[now_point - 1])])
      loop_num = len(loop_list)
      # print(root_list,loop_list,loop_num,first_num)
      break
    else:
      root_list.append(a_list[now_point - 1])

  num = (k - first_num) % loop_num
  print(loop_list[num-1])
  # now_point = 1
  # l = (k-first_num) % loop_num
  # for i in range(first_num+l):
  #       now_point = a_list[now_point - 1]
        # print(now_point)

  # print(now_point)

  # print(now_point)

  # k = k%count
  # now_point = a_list[0]
  # for i in range(k-1):
  #   now_point = a_list[now_point - 1]

  # print(now_point)


if __name__ == '__main__':
  main()
