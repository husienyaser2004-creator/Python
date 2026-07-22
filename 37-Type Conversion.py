#----------------------------------
#----Type Conversion---------------
#----------------------------------

# Str()

a = 10
print(type(a))
print(type(str(a)))

print("#" * 50)

# Tuple()

c = "Hussien" # String
d = [1, 2, 3, 4, 5] # List 
e = {"A", "B" , "C"} # Set 
f = {"A": 1, "B": 2} # Dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

print("#" * 50)

# LIst()

c = "Hussien" # String
d = (1, 2, 3, 4, 5) # Tuple
e = {"A", "B", "c"} # Set
f = {"A": 1,"B": 2} # Dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))

print("#" * 50)

# Set()

c = "Hussien" # String
d = (1, 2, 3, 4, 5) # Tuple
e = {"A", "B", "c"} # List
f = {"A": 1,"B": 2} # Dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))

print("#" * 50)

# dict()

#c = "Hussien" # String
d = (("A", 1), ("B", 2), ("C", 3)) # Tuple
e = [["one" , 1], ["Two", 2], ["Three", 3]] # List
#f = {{"A": 1}, {"B": 2}}  # Set


#print(dict(c))
print(dict(d))
print(dict(e))
#print(dict(f))
