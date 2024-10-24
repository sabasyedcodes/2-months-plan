a,b,c,d = map(int,input().split())
mul= a*b*c*d
res = mul%100 
print(f"{res:02d}")
