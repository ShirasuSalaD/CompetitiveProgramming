def main():
    table = [[[0]*10 for i in range (0,3)] for j in range (0,4)]

    N = int(input())
    for i in range(N):
         b_num, f_num, r_num, v_num = map(int, input().split())
         table[b_num-1][f_num-1][r_num-1] += v_num

    # print(table)

    x = 0

    for i in range(4):
        if x != 0:
            print("#"*20)
        x += 1

        for a in range(3):
            for b in range(10):
                print(" %d" % (table[i][a][b]), end="")
            print()

if __name__ == '__main__':
  main()
