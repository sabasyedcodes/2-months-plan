input_str = input()

# Find the position of the operator
for operator in "+-*/":
    if operator in input_str:
        # Split the input based on the operator
        a, b = map(int, input_str.split(operator))
        s = operator
        break
result = 0
if s == '+':
    result = a + b
elif s == '-':
    result = a - b
elif s == '*':
    result = a * b
elif s == '/':
    result = a // b 
else:
    result = 0

print(result)
