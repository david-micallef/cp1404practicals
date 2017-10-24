"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        return 0
    print(n ** 2)
    do_something(n - 1)

# TODO: 3. write down what you think the output of this will be,
# TODO: 4. use the debugger to step through and see what's actually happening
do_something(4)

# TODO: 5. fix do_something() so that it works the way it probably should :)

test = 0
n = 6
for i in range(n, 0, -1):
    test += i
print(test)


entered_number = int(input("Please enter the number of rows: "))


def from_scratch(n):
    if n < 0:
        return 0
    else:
        return n + from_scratch(n - 1)

print(from_scratch(entered_number))

