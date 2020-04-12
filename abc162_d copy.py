def main():
    N = int(input())
    S = input()
    ans = S.count('R')*S.count('G')*S.count('B')
    for i in range(N):
        for d in range(N):
            j = i+d
            k = j+d
            if k >= N:
                break
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)


main()
