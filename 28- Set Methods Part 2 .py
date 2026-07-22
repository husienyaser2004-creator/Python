# --------------------------
# --==>> Set Methods Part 2 <<==--
# --------------------------

# difference()

a = {1, 2, 3, 4}
b = {1, 2, 3, "Hussien" , "Yasser"}
print(a)
print(a.difference(b)) # a-b 
print(a)

print("=" * 40) # Separator

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, 3, "Hussien" , "Yasser"}
print(c)
print(c.difference_update(d)) # c-d
print(c)

print("=" * 40) # Separator

# intersection()

e = {1, 2, 3, 4, "x", "Hussien"}
f = {"Hussien", "x", 2 }
print(e)
print(e.intersection(f)) # e & f
print(e)

print("=" * 40) # Separator


# intersection_update(h)
g = {1, 2, 3, 4, "x", "Hussien"}
h = {"Hussien", "x", 2 }
print(g)
g.intersection_update(h) # g & f
print(g)

print("=" * 40) # Separator

# symmetric_difference()

i = {1, 2, 3, 4, 5, "x"}
j = {"Hussien", "Soudy", 1, 2, 4, "x"}
print(i)
print(i.symmetric_difference(j)) # i ^ j
print(i)

print("=" * 40) # Separator

# symmetric_difference_update()

k = {1, 2, 3, 4, 5, "x"}
l = {"Hussien", "Soudy", 1, 2, 4, "x"}
print(k)
k.symmetric_difference_update(l)  # k ^ l
print(k)

