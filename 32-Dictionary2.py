#----------------------------------------
#---dictionary Methods Part 2---
#----------------------------------------

# setdefault(key, default_value)
user = {
    "name" : "Osama"
}

print(user)
print(user.setdefault("age", 36))
print(user)

print("=" * 40)

# popitem()

member = {
    "name" : "osama",
    "skill" : "ps4"
}
print(member)
member.update({"age": 36})
print(member.popitem())

print("=" * 40)

# items()

view = {
    "name":"osama",
    "skill" : "xBox"
}

allItmes = view.items
print(view)
view["age"] = 36

print(allItmes)

print("=" * 40)

# fromkeys()

a = ('Mykeyone', 'MykeyTwo', 'MykeyThree')
b = "x"

print(dict.fromkeys(a, b))
