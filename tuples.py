# Creating a tuple
tuple1 = (1, 2, 3, 4, 5)
print("Tuple 1:", tuple1)

# Tuple with mixed data types
tuple2 = (1, "Hello", 3.4)
print("Tuple 2:", tuple2)

# Nested tuple
tuple3 = ("mouse", [8, 4, 6], (1, 2, 3))
print("Tuple 3:", tuple3)

# Creating a tuple with one element
tuple4 = ("hello",)
print("Tuple 4:", tuple4)

# Accessing elements in a tuple
print("First element of tuple1:", tuple1[0])
print("Last element of tuple2:", tuple2[-1])

# Slicing a tuple
print("Sliced tuple1 (1:3):", tuple1[1:3])

# Concatenating tuples
tuple5 = tuple1 + tuple2
print("Concatenated tuple:", tuple5)

# Tuple unpacking
a, b, c = tuple2
print("Unpacked tuple2:", a, b, c)