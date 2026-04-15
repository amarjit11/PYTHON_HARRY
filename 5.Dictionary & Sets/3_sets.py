#A set in Python is a collection of unique elements, where duplicates are not allowed and the elements are unordered. ITS MUTABLE

# Initial sets
a = {1, 2, 3}
b = {3, 4, 5}

print("Original sets:")
print("a =", a)
print("b =", b)

# add() → adds a single element to the set
a.add(6)
print("\nAfter add (added 6):", a)

# update() → adds multiple elements (list, tuple, set)
a.update([7, 8])
print("After update (added 7,8):", a)

# remove() → removes element, gives error if not found
a.remove(8)
print("After remove (removed 8):", a)

# discard() → removes element, NO error if not found
a.discard(10)
print("After discard (tried removing 10):", a)

# pop() → removes a random element and returns it
removed = a.pop()
print("Popped element:", removed)
print("After pop:", a)

# copy() → creates a shallow copy of the set
c = a.copy()
print("Copy of a:", c)

# union() → combines both sets (all unique elements)
print("\nUnion (a U b):", a.union(b))

# intersection() → common elements in both sets
print("Intersection (a ∩ b):", a.intersection(b))

# difference() → elements in a but not in b
print("Difference (a - b):", a.difference(b))

# symmetric_difference() → elements not common in both
print("Symmetric Difference:", a.symmetric_difference(b))

# issubset() → checks if all elements of a are in b
print("\nIs a subset of b?", a.issubset(b))

# issuperset() → checks if b contains all elements of a
print("Is b superset of a?", b.issuperset(a))

# isdisjoint() → checks if sets have no common elements
print("Are a and b disjoint?", a.isdisjoint(b))

# clear() → removes all elements from the set
c.clear()
print("\nAfter clear c:", c)

'''a={1,2,3}
print(type(a))
f={} # this will create an empty dict
e=set() # this will creat an empty set
print(type(e))

s={ 4,65,24,7,21,67,43,87,2,"amar"}
print(s)
#order=sorted(s)
#print(order)
#print(sorted(s, reverse=True))
s.add(566)
print(s,type(s))'''