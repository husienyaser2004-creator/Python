#----------------------------------------------
#---- String Methods Part three----------------
#----------------------------------------------

# index(SubString , Start , End ) 

a = "I Love Python"
#print(a.index("P")) #index Number 7
#print(a.index("P", 0 , 10)) #index Number 7
#print(a.index("P", 0 , 5)) # Error

# Find (SubString , Start , End ) 

b = "I Love Python"
print(b.find("P")) #index Number 7
print(b.find("P", 0 , 10)) #index Number 7
print(b.find("P", 0 , 5)) # -1

# rjust(width , Fill char ) , ljust(width , Fill char)

C = "hussien"
print(C.rjust(10))
print(C.rjust(10 , "#"))

# ljust(width , Fill char)
d = "hussien"
print(d.ljust(10))
print(d.ljust(10 , "#"))

# Splitlines()

e ="""Frist Line
second Line
Third Line"""

print(e.splitlines())

f = "Frist Line\nsecond Line\nThird Line"

print(f.splitlines())

# expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

Three = " "
Four = ""
print(Three.isspace())
print(Four.isspace())

Five = 'i love python'
six = 'I Love Python'
print(Five.islower())
print(six.islower())

# identifier() => Return The Memory Address Of The Object As An Integer
Seven = "Hussien_soudy"
eight = "HussienSoudy"
nine = "Hussien--Soudy"

print(Seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaaaBbbbbbb"
y = "AaaaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaaaBbbbbbb"
z = "AaaaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())
