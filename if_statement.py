# Example 1: Simple if statement
x = 10
if x > 5:
    print("x is greater than 5")

# Example 2: if-else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# Example 3: if-elif-else statement
z = 7
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but less than or equal to 10")
else:
    print("z is 5 or less")

# Example 4: Nested if statements
a = 8
b = 12
if a > 5:
    if b > 10:
        print("a is greater than 5 and b is greater than 10")
    else:
        print("a is greater than 5 but b is not greater than 10")
else:
    print("a is not greater than 5")

# Example 5: Check if value is in the list
my_list = [1, 2, 3, 4, 5]
value = 3
if value in my_list:
    print(f"{value} is in the list")
else:
    print(f"{value} is not in the list")

