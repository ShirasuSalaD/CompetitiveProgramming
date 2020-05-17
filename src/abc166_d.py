def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors

def main():
  X = int(input())

  # for i in make_divisors(X):
  #   for b in range(1,X):
  #     if (b + i) ^ 5 - b ^ 5 == X:
  #       print(b+i, b)
  #       break
  #   break

  # for a in range(-1000,1001):
  #   for b in range(-1000,1001):
  #     if a ** 5 - b ** 5 == X:
  #       return(a, b)
  #   return (-2000, 2000)

  def search(x: int) -> (int, int):
    for a in range(-1000, 1001):
      for b in range(-1000, 1001):
        if a ** 5 - b ** 5 == x:
          return (a, b)
    return (-2000, -2000)

  a, b = search(X)
  print(f'{a} {b}')

if __name__ == '__main__':
  main()
