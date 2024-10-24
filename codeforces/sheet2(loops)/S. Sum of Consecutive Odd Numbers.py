t = int(input())
res = []
for _ in range(t):
  x,y = map(int,input().split())
  start = min(x,y)+1
  end = max(x,y)
  sum=0
  for i in range(start,end):
    if i%2 != 0:
      sum+=i
  res.append(sum)
for i in res:
  print(i)