N = int(input())
S = list(input())

count = 0

for first_index in range(1, N+1):
  first = S[first_index-1]
  for second_index in range(first_index, N+1):
    second = S[second_index-1]
    for third_index in range(second_index, N+1):
      third = S[third_index - 1]
      # print(first,second,third)
      if first != second and second != third and first != third and second_index - first_index != third_index-second_index:
        count += 1
      # print(count)

print(count)