import math

# Read input values
A, B, C, D = map(int, input().split())

# Calculate the logarithmic values for comparison
left = A**B
right = C**D

# Compare the two sides
if left > right:
    print("YES")
else:
    print("NO")