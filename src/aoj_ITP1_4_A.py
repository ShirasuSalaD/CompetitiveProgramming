#割り算

def main():
  a, b = map(int, input().split())
  print(int(a/b), a % b, f'{ float(a / b) :.5f}')

if __name__ == '__main__':
  main()
