import copy

# Using the copy() method
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print(copied_list)

# Using list slicing
original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:]
print(copied_list)

# Using the list() constructor
original_list = [1, 2, 3, 4, 5]
copied_list = list(original_list)
print(copied_list)

# Using the copy module
original_list = [1, 2, 3, 4, 5]
copied_list = copy.copy(original_list)
print(copied_list)

# Using the deepcopy() method from the copy module (for nested lists)
original_list = [[1, 2], [3, 4], [5, 6]]
copied_list = copy.deepcopy(original_list)
print(copied_list)