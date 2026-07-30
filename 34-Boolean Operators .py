#-------------------------
#---Boolean Operators-----
#-------------------------
# and
# or
# not

age = 36
country = "Egypt"
rank = 10


print(age > 16 )
print(country == "Egypt")

print("=" * 50)

# and

print(age > 16 and country == "Egypt" and rank > 0) # True
print(age > 16 and country == "KSA" and rank > 0) # Fales


print("=" * 50)

# or

print(age > 16 or country == "Egypt" or rank > 0) # True
print(age > 16 or country == "KSA" or rank > 0) # True


print("=" * 50)

# Not

print(age > 16 ) # True
print( not age > 16 ) # Not True = Fales