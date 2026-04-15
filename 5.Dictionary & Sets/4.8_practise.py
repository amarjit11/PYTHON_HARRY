#Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}

s.update({8,7})
print(s)

# this is  wrong. cannot use 'list' as a set element (unhashable type: 'list')