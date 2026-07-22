#------------------------
#--Set Methods Part 1
#------------------------

# Clear()
a = {1, 2, 3, 4}
a.clear()
print(a)

# Union 

b = {"one", "two", "three"}
c = {"1","2","3"}
x = {"Zero" , "cool"}

print(b | c)
print(b.union(c,x))

# add()
d = {1, 2, 3, 4}
d. add(5)
d. add(6)
print(d)

# Copy()
e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)

# Remove()

g = {1, 2, 3, 4}
g.remove(1)
#g.remove(7)
print(g)

# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)

# pop()
i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())

#update()

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update(['Html', "css"])
j.update(k)

print(j)




