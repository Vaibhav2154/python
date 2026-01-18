"""
Python Lambda Functions
Author: ---
Description: Examples of lambda (anonymous) functions in Python
"""

# --------------------------------------------------
# 1. Basic Lambda Function Example
# --------------------------------------------------

# String to convert to uppercase
s1 = "GeeksforGeeks"

# Lambda function that converts a string to uppercase
s2 = lambda func: func.upper()

# Calling the lambda function
print(s2(s1))  # Output: GEEKSFORGEEKS


# --------------------------------------------------
# 2. Lambda with Condition Checking (if-else)
# --------------------------------------------------

# Lambda to classify a number as Positive, Negative, or Zero
check_sign = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(check_sign(5))    # Output: Positive
print(check_sign(-3))   # Output: Negative
print(check_sign(0))    # Output: Zero


# --------------------------------------------------
# Lambda to check Even or Odd
# --------------------------------------------------

check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_even_odd(4))  # Output: Even
print(check_even_odd(7))  # Output: Odd


# --------------------------------------------------
# 3. Lambda with List Comprehension
# --------------------------------------------------

# Creating a list of lambda functions
# Each lambda multiplies its value by 10
li = [lambda arg=x: arg * 10 for x in range(1, 5)]

# Executing each lambda function
for i in li:
    print(i())

# Output:
# 10
# 20
# 30
# 40


# --------------------------------------------------
# 4. Lambda Returning Multiple Results (Tuple)
# --------------------------------------------------

# Lambda that returns sum and product of two numbers
calc = lambda x, y: (x + y, x * y)

result = calc(3, 4)
print(result)  # Output: (7, 12)


# --------------------------------------------------
# 5. Lambda with filter()
# --------------------------------------------------

# List of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Filter only even numbers using lambda
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  # Output: [2, 4, 6]


# --------------------------------------------------
# 6. Lambda with map()
# --------------------------------------------------

# List of numbers
a = [1, 2, 3, 4]

# Double each element using map and lambda
b = map(lambda x: x * 2, a)

print(list(b))  # Output: [2, 4, 6, 8]


# --------------------------------------------------
# 7. Lambda with reduce()
# --------------------------------------------------

from functools import reduce

# List of numbers
a = [1, 2, 3, 4]

# Multiply all elements using reduce and lambda
product = reduce(lambda x, y: x * y, a)

print(product)  # Output: 24


# --------------------------------------------------
# 8. Difference Between lambda and def
# --------------------------------------------------

# Using lambda
sq = lambda x: x ** 2
print(sq(3))  # Output: 9


# Using def
def sqdef(x):
    return x ** 2

print(sqdef(3))  # Output: 9
