import math
n=int(input())
m = list(map(int,input().split()))

max = -math.inf
for i in m:
  if i>max:
    max = i
print(max)