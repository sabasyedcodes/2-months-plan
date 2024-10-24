import math
x,y = map(int,input().split())
floor_result = math.floor(x / y)
ceil_result = math.ceil(x / y)
result = (x / y)
roundoff = round(x / y)

print(f"floor {x} / {y} = {floor_result}")
print(f"ceil {x} / {y} = {ceil_result}")
print(f"round {x} / {y} = {roundoff+1 if result-int(result)== .5 else roundoff}")
