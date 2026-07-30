                   ### Set methods ###
### Union()   ,    add()      ,    remove()   ,   discard()  ,  clear()   ###              
a = {1,2,3}
b = {4,5,6, "ahmed"}
print(a.union(b))      ##print(a|b)
a.add(10)
a.add(15)
print(a)
b.remove(5)
b.remove("ahmed")
#b.remove(20)
b.discard(5)
b.discard("ahmed")
b.discard(20)
print(b)
a.clear()
print(a)
