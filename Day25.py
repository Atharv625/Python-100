c = (1, 2, 3, 4, 5)
temp = list(c)  # Convert tuple to a list (this allows modification)
print(temp)  # [1, 2, 3, 4, 5]

# The following lines will give an error because tuples are immutable:

# c.append(6)  # ❌ AttributeError: 'tuple' object has no attribute 'append'
# c.pop()      # ❌ AttributeError: 'tuple' object has no attribute 'pop'
# c.remove(1)  # ❌ AttributeError: 'tuple' object has no attribute 'remove'
# c.insert(1, 6)  # ❌ AttributeError: 'tuple' object has no attribute 'insert'
# c.sort()     # ❌ AttributeError: 'tuple' object has no attribute 'sort'
# c.reverse()  # ❌ AttributeError: 'tuple' object has no attribute 'reverse'

# However, these operations work on tuples because they do not modify them:
print(c.count(1))   # ✅ 1 (Counts occurrences of 1 in the tuple)
print(c.index(1))   # ✅ 0 (Finds the index of 1 in the tuple)
