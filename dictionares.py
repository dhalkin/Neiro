# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: John
print(person["age"])   # Output: 30

# Adding a new key-value pair
person["email"] = "john@example.com"

# Updating a value
person["age"] = 31

# Removing a key-value pair
del person["city"]

# Iterating through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "name" in person:
    print("Name is present in the dictionary")

# Getting the length of a dictionary
print(len(person))  # Output: 3

# Nested dictionary
students = {
    "student1": {
        "name": "Alice",
        "age": 24
    },
    "student2": {
        "name": "Bob",
        "age": 22
    }
}

# Accessing nested dictionary values
print(students["student1"]["name"])  # Output: Alice