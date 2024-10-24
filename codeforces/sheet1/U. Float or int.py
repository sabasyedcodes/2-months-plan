# Input the number as a string
N = input().strip()

# Split the number into integer and decimal parts
if '.' in N:
    integer_part, decimal_part = N.split('.')
    
    # Check if the decimal part is effectively zero
    if int(decimal_part) == 0:
        print(f'int {integer_part}')
    else:
        # Format the decimal part as a float
        formatted_decimal_part = '0.' + decimal_part
        print(f'float {integer_part} {formatted_decimal_part}')
else:
    # If no decimal point, it's an integer
    print(f'int {N}')
