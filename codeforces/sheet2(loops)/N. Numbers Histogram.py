s = input()
n = int(input())
numbers = list(map(int,input().split()))

for i in numbers:
  while(i>0):
    print(s,end="")
    i-=1
  print()
