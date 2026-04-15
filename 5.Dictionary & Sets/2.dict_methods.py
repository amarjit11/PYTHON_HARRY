

marks= {
	"Amarjit":100,
	"shubham":78,
	"Rohan":45,
	0:"Harry"

}

a={}
print(type(a))
print(type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Amarjit":99})
print(marks.get("Amarjit"))# returns none if not matches
print(marks["Amarjit"]) # returns error
print(marks.pop(0)) # 👉 pop() removes a key-value pair using the key and returns its value
print(marks)

'''# Initial dictionary
student = {
    "name": "Amarjit",
    "age": 22,
    "marks": 85
}

print("Original dictionary:")
print(student)

# get() → safely gets value (no error if key missing)
print("\nGet name:", student.get("name"))
print("Get city (not present):", student.get("city"))  # returns None

# keys() → returns all keys
print("\nKeys:", student.keys())

# values() → returns all values
print("Values:", student.values())

# items() → returns key-value pairs as tuples
print("Items:", student.items())

# update() → updates existing keys and adds new ones
student.update({"age": 23, "city": "Patna"})
print("\nAfter update (age changed, city added):", student)

# pop() → removes a key and returns its value
removed_value = student.pop("marks")
print("\nPopped 'marks':", removed_value)
print("After pop:", student)

# popitem() → removes last inserted key-value pair
last_item = student.popitem()
print("\nPopitem (last inserted removed):", last_item)
print("After popitem:", student)

# setdefault() → returns value if key exists, else adds key with default value
student.setdefault("marks", 0)
print("\nAfter setdefault (marks added if missing):", student)

# copy() → creates a shallow copy of dictionary
new_student = student.copy()
print("\nCopy of dictionary:", new_student)

# clear() → removes all elements from dictionary
new_student.clear()
print("After clear (new_student):", new_student)'''