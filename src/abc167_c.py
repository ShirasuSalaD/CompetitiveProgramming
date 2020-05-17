import numpy as np


def python_list_add(in1, in2):
    wrk = np.array(in1) + np.array(in2)
    return wrk.tolist()

def main():
  n, m, x = map(int, input().split())
  data = [list(map(int, input().split())) for i in range(n)]
  val = []
  for i in range(0,n):
    val+=python_list_add(val,data[i])

  print(val)

if __name__ == '__main__':
  main()
