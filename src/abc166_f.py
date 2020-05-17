def main():
  n, a, b, c = map(int, input().split())
  ab_num = 0
  ac_num = 0
  bc_num = 0
  s_li = []
  for i in range(n):
    s = input()
    s_li.append(s)
    if s == 'AB':
      ab_num += 1
    elif s == 'AC':
      ac_num += 1
    elif s == 'BC':
      bc_num += 1

  ab_num = ab_num % 2
  ac_num = ac_num % 2
  bc_num = bc_num % 2

  print(ab_num, ac_num, bc_num)

  if (a == 0 and b == 0 and ab_num > 0) or (a == 0 and c == 0 and ac_num > 0) or (b == 0 and c == 0 and bc_num > 0):
    print('No')
  else:
    print('Yes')
    # for i in s_li:
      # 

if __name__ == '__main__':
  main()
