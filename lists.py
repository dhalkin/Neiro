#lists

family = ['dad', 'mom', 'Romka', 'Kejsi']
print(family[-1])

message = f"Our dog name is a {family[3].title()}"
print(message)

family.append('Ksenia')
print(family)

family.insert(0, 'myself')
print(family)

# here is del and pop, remove
del family[0]
popped = family.pop()
print(popped, family)

family.remove('Kejsi')
print(family)

family.sort(reverse=True)

# 
for value in range(1, 3):
    print(value)

numbers = list(range(1, 6))
print(numbers)

# there is a third argument in range function, it is a step
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# list statistics
digits = list(range(1, 11))
print(min(digits), max(digits), sum(digits))

# list comprehension
squares = [value ** 2 for value in range(1, 11)]
print(squares)