# def main():
#     N, *A = map(int, open(0).read().split())
#     cnt_subordinates = [0] * (N + 1)
#     for a in A:
#         cnt_subordinates[a] += 1
#     print("\n".join(map(str, cnt_subordinates[1:])))


# if __name__ == "__main__":
#     main()

import collections
import numpy as np
N = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
for i in range(1, N+1):
print(c[i])

# import sys
# # sys.path.append('/Users/hiroki/anaconda3/lib')
# print(sys.version)
# print(sys.path)
