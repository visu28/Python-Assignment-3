def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Call the function with a sample number
sample_number = 5
result = factorial(sample_number)

# Print the output
print(f"The factorial of {sample_number} is {result}")
