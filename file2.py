import math

# Step 1: Ask the user for a number
try:
    number = float(input("Enter a number: "))

    # Step 2: Perform calculations using the math module
    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)

    # Step 3: Display the results
    print(f"Enter a number {number}:")
    print(f"Square Root: {square_root}")
    print(f"Logarithm : {natural_log}")
    print(f"Sine : {sine_value}")

except ValueError as e:
    print(f"Error: {e}. Please enter a valid positive number.")
