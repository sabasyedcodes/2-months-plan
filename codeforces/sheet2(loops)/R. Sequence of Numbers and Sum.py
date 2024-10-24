# Read all input lines
inputs = []
while True:
    try:
        line = input().strip()
        if line:  # Only add non-empty lines
            inputs.append(line)
        else:
            break  # Stop if an empty line is encountered
    except EOFError:
        break  # Handle end of input gracefully

# Process each line
for line in inputs:
    N, M = map(int, line.split())
    
    # Check termination condition
    if N <= 0 or M <= 0:
        break
    
    # Determine the range
    start, end = min(N, M), max(N, M)
    
    # Generate the sequence and calculate the sum
    sequence = list(range(start, end + 1))
    sequence_sum = sum(sequence)
    
    # Prepare and print output
    print(" ".join(map(str, sequence)) + f" sum ={sequence_sum}")
