# Dictionary Demonstration in Python

# 1. Create a dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Initial Dictionary:", my_dict)

# 2. Accessing elements
print("Accessing 'name':", my_dict["name"])
print("Accessing 'age' with get():", my_dict.get("age"))
print("Accessing a non-existent key with get():", my_dict.get("country", "Not Found"))

# 3. Adding and updating elements
my_dict["country"] = "USA"  # Add new key-value pair
print("After adding 'country':", my_dict)
my_dict["age"] = 26  # Update existing key
print("After updating 'age':", my_dict)

# 4. Removing elements
removed_city = my_dict.pop("city")  # Remove with pop()
print("Removed 'city':", removed_city)
print("After removing 'city':", my_dict)

last_item = my_dict.popitem()  # Remove the last inserted item
print("Removed last item:", last_item)
print("After popitem():", my_dict)

del my_dict["name"]  # Delete a specific key
print("After deleting 'name':", my_dict)

my_dict.clear()  # Clear the dictionary
print("After clearing dictionary:", my_dict)

# 5. Iteration
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("\nIterating through keys:")
for key in my_dict:
    print(key)

print("\nIterating through values:")
for value in my_dict.values():
    print(value)

print("\nIterating through key-value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 6. Nested dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print("\nNested Dictionary:", nested_dict)
print("Access nested value (person1's name):", nested_dict["person1"]["name"])

# Adding a new nested entry
nested_dict["person3"] = {"name": "Charlie", "age": 35}
print("After adding 'person3':", nested_dict)

# 7. Other methods
print("\nChecking if 'age' is in dictionary:", "age" in my_dict)
print("All keys:", my_dict.keys())
print("All values:", my_dict.values())
print("All items:", my_dict.items())
