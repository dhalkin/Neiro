# Example list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing from index 2 to 5
slice1 = my_list[2:6]
print("Slice from index 2 to 5:", slice1)

# Slicing from the beginning to index 4
slice2 = my_list[:5]
print("Slice from beginning to index 4:", slice2)

# Slicing from index 5 to the end
slice3 = my_list[5:]
print("Slice from index 5 to end:", slice3)

# Slicing with a step of 2
slice4 = my_list[::2]
print("Slice with a step of 2:", slice4)

# Slicing with negative indices
slice5 = my_list[-5:-2]
print("Slice with negative indices:", slice5)

# Slicing with negative step (reversing the list)
slice6 = my_list[::-1]
print("Slice with negative step (reversed list):", slice6)

# Looping through a slice from index 2 to 5
for i in my_list[2:6]:
    print("Looping through slice from index 2 to 5:", i)

# Looping through a slice from the beginning to index 4
for i in my_list[:5]:
    print("Looping through slice from beginning to index 4:", i)

# Looping through a slice from index 5 to the end
for i in my_list[5:]:
    print("Looping through slice from index 5 to end:", i)

# Looping through a slice with a step of 2
for i in my_list[::2]:
    print("Looping through slice with a step of 2:", i)

# Looping through a slice with negative indices
for i in my_list[-5:-2]:
    print("Looping through slice with negative indices:", i)

# Looping through a slice with negative step (reversing the list)
for i in my_list[::-1]:
    print("Looping through slice with negative step (reversed list):", i)