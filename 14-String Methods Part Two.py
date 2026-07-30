#---------------------------------
#---- String Methods Part Two--
#---------------------------------

# Split() rsplit()
a = "I Love Python and PHP and MySQL"
print(a.split())

b="I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

b="I-Love-Python-and-PHP-and-MySQL"
print(b.split("-", 3))

#rsplit()
d ="I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))

# Center()

a = "hussien"
print(a.center(9)) # Spaces
print(a.center(9, "#")) # Hashes
print(a.center(15, "@")) # @

# Count()

F = "I Love Python and PHP Because PHP is Easy"
print(F.count("PHP")) # 2 PHP World
print(F.count("PHP", 0, 25)) # only one PHP World

# Swapcase()

g = "I Love python"
h = "i love PYTHON"
print(g.swapcase())
print(h.swapcase())

#startswith()  endswith()
i = "I Love Python"
print(i.startswith("I")) # True
print(i.startswith("s")) # False
print(i.startswith("p" , 7, 12)) # False

#endswith()
j = "I Love Python"
print(j.endswith("n")) # True
print(j.endswith("N")) # False
print(j.endswith("e" , 2, 6)) # true
