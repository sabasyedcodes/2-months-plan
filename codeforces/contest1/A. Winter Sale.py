x,p = map(float,input().split())
original = p/(1-x/100)
ans = "{:.2f}".format(original)
print(ans)