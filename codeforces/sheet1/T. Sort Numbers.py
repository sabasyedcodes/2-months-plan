a,b,c = map(int,input().split())
orginal_a,orginal_b,orginal_c = a,b,c
if a>b:
  a,b = b,a
if a>c:
  a,c = c,a
if b>c:
  b,c = c,b
print(a)
print(b)
print(c)

print()

print(orginal_a)
print(orginal_b)
print(orginal_c)