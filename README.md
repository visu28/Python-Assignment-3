# Python-Assignment-3
# Python Programs: Factorial Calculator and Math Function Evaluator

This repository contains two Python programs demonstrating basic concepts of recursion, input handling, and use of the standard `math` module.

## 1. file1.py – Factorial Calculator

This program defines a recursive function to compute the factorial of a number.

### Description:
- The `factorial` function is defined recursively.
- The base case is when the input is 0 or 1; the result is 1.
- For all other positive integers, the function calls itself with the argument decremented by 1 and multiplies the result.
- The program then calls this function with a sample number (5) and prints the result.

### Sample Output:
The factorial of 5 is 120



---

## 2. file2.py – Math Function Evaluator

This program prompts the user to input a number and performs the following calculations using Python's built-in `math` module:

- Square root
- Natural logarithm
- Sine (in radians)

### Description:
- Accepts user input as a float.
- Calculates square root using `math.sqrt()`.
- Calculates natural logarithm using `math.log()`.
- Calculates sine using `math.sin()`.
- If invalid input is provided (e.g., negative numbers for square root or log), an error message is displayed.

### Sample Output:
Enter a number: 4
Enter a number 4.0:
Square Root: 2.0
Logarithm : 1.3862943611198906
Sine : -0.7568024953079282


---

## Requirements

- Python 3.x
- No additional libraries are required beyond the standard library.

---

## How to Run

Use the following commands to execute the programs:

