x = input()
if x>='a' and x<='z':
  upper = chr(ord(x)-32)
  print(upper)
else:
  lower = chr(ord(x)+32)
  print(lower)