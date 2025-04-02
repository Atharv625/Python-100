s={2,5,6,3,9,8,7,4,1}
s2={1,2,3,4,5}
print(s.union(s2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s.intersection(s2))  # Output: {1, 2, 3, 4, 5}
print(s.difference(s2))  # Output: {6, 7, 8, 9}
print(s.issubset(s2))  # Output: False
print(s.issuperset(s2))  # Output: True
print(s.symmetric_difference(s2))
# s.update(s2)
# print(s)  
print(s2.issubset(s))  # Output: True
print(s.isdisjoint(s2))  # Output: False
print(s.discard(s2))  # Output: {1, 2, 3, 4, 5}
del s2
print(s2)  # Output: set()

