#-------------------------
#-Dictionary Methods Part 1-
#-------------------------

# clear()
user = {
    "name": "Hussien"
}

print(user) # Original dictionary
user.clear() # Clear the dictionary
print(user) # Empty dictionary

print("=" * 50) # Separator

# update()
member = {
    "name": "Hussien",
}
print(member) # Original dictionary
member["age"] = 22
print(member) # Dictionary after adding a new key-value pair
member.update({"country": "Egypt"}) 
print(member) # Dictionary after updating with a new key-value pair


print("=" * 50) # Separator

# copy()
main = {
    "name": "Hussien",
}

b = main.copy() # Create a copy of the dictionary
print(b)
main.update({"skill": "Python"}) # Update the original dictionary
print(main) # Original dictionary after update
print(b) # Copied dictionary remains unchanged

print("=" * 50) # Separator

# keys() + values()

print(main.keys()) # Get all keys in the dictionary
print(main.values()) # Get all values in the dictionary

print("=" * 50) # Separator

