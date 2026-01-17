def main():
	# for loop with range
	for i in range(5):
		print("for-range:", i)

	# for loop over a sequence
	fruits = ["apple", "banana", "cherry"]
	for f in fruits:
		print("for-list:", f)

	# while loop
	count = 0
	while count < 3:
		print("while:", count)
		count += 1

	# break and continue
	for n in range(1, 7):
		if n == 2:
			continue
		if n == 5:
			break
		print("loop-control:", n)

	# loop else clause
	for n in range(3):
		print("else-loop:", n)
	else:
		print("for-else executed (no break)")


if __name__ == "__main__":
	main()
