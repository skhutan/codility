def solution(A):
  length = len(A)
  sum_a = sum(A)
  leftsum = 0
  i = 0
  while( i < length):
    value = A[i]
    if leftsum == sum_a - value:
      return i
    leftsum += value
    sum_a -= value
    i += 1
  return -1

solution([-7, 1, 5, 2, -4, 3, 0])