#------------------------------------------
#--------Lists Methods Part 2--------------
#------------------------------------------

# Clear ()
a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()
b = [1, 2, 3, 4]
c = b.copy()
print(b) # Main list
print(c) # Copied list

b.append(5)
print(b) # Main list after append
print(c) # Copied list after append

# Count (value)
d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1)) # Count the number of times 1 appears in the list

# index(value, start, end)
e = ["hussien", "mohamed", "hamza", "hussien", "mohamed"]
print(e.index("hamza")) # Index of the first occurrence of "hamza"

# insert(index, value)

f = [1, 2, 3, 4, 5, "A" , "B"]
f.insert(0, "Test") # Insert "C" at index 0
f.insert(-1 , "Test") # Insert "C" at the second to last position

print(f)

# pop(index)
g = [1, 2, 3, 4, 5]
print(g.pop(3)) # Remove and return the item at index 3

