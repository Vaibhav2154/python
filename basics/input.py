# string input
a = input()
print(type(a))
print(a)

# Taking multiple input
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# taking a list input
arr = input().split()
print(arr)
print(type(arr))

# This code takes a single line of numeric input, splits it and converts all elements to integers
li = list(map(int, input().split()))
print(li)