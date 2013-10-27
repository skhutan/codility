def solution(A, B):
  heavy = 0
  for i in range(A,B + 1):
    num = str(i)
    total = sum([int(n) for n in num])
    avg = total/float(len(num))
    if avg > 7:
      heavy += 1
  return heavy

print solution(8675, 8689)