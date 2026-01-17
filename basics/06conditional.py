def evaluate_number(n):
	if n > 0:
		return "positive"
	elif n < 0:
		return "negative"
	else:
		return "zero"


def main():
	x = 10
	y = 20

	# Basic comparisons
	if x < y:
		print("x is less than y")
	elif x == y:
		print("x equals y")
	else:
		print("x is greater than y")

	# Logical operators
	is_even = (x % 2 == 0)
	in_range = (5 <= x <= 15)
	if is_even and in_range:
		print("x is even and within [5, 15]")

	if is_even or y > 100:
		print("Either x is even or y is very large")

	if not (y % 2 == 0):
		print("y is odd")
	else:
		print("y is even")

	# Ternary expression
	parity = "even" if x % 2 == 0 else "odd"
	print(f"x is {parity}")

	# Membership and identity
	items = [10, 30, 50]
	print(10 in items)
	print(40 not in items)
	print(items is items)
	print(items is not list(items))

	# Function-based decision
	for n in (5, -2, 0):
		print(n, "->", evaluate_number(n))


if __name__ == "__main__":
	main()
