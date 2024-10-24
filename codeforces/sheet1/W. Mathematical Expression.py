a,s,b,q,c = input().split()
a = int(a)
b = int(b)
c = int(c)

if s == "+" :
  res = a+b
elif s== "-":
  res = a-b
elif s=="*":
  res = a*b

if res == c:
  print("Yes")
else:
  print(res)