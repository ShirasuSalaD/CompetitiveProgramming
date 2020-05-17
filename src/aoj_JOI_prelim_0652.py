def main():
    a, b, c = map(int, input().split())
    w = a * 7 + b
    ans = c // w * 7
    c = c % w
    d = c // a
    if c % a > 0:
        d += 1
    if d > 7:
        d = 7
    ans += d
    print(ans)

if __name__ == '__main__':
  main()
