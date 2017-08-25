numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])
# The number is 3

print(numbers[-1])
# The number is 2

print(numbers[3])
# The number is 1

print(numbers[:-1])
# The list is [3, 1, 4, 1, 5, 9]

print(numbers[3:4])
# The list is [1]

print(5 in numbers)
# True

print(7 in numbers)
# False

print("3" in numbers)
# False

print(numbers + [6, 5, 3])
# The list is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

numbers[0] = 10
print(numbers)

numbers[-1] = 1
print(numbers)

print(numbers[2:])

print(9 in numbers)
