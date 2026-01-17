def main():
	# Numeric types
	integer_val = 42
	float_val = 3.14159
	complex_val = 2 + 3j

	# Boolean
	is_active = True

	# String
	text = "Hello, Python!"

	# None
	nothing = None

	# Sequence types
	numbers_list = [1, 2, 3]
	mixed_tuple = ("a", 10, 2.5)

	# Set types
	unique_set = {1, 2, 2, 3}
	frozen = frozenset({"x", "y", "z"})

	# Mapping type
	person = {"name": "Alice", "age": 30}

	# Bytes
	raw_bytes = b"abc"

	# Show values and their types
	values = [
		integer_val,
		float_val,
		complex_val,
		is_active,
		text,
		nothing,
		numbers_list,
		mixed_tuple,
		unique_set,
		frozen,
		person,
		raw_bytes,
	]

	for v in values:
		print(v, "->", type(v).__name__)

	# Basic operations
	numbers_list.append(4)
	unique_set.add(4)
	person.update({"city": "Wonderland"})
	print("list:", numbers_list)
	print("set:", unique_set)
	print("dict:", person)


if __name__ == "__main__":
	main()
