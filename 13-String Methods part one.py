#----------------------
#---String Methods --
#-----------------------

a = "I love Python"
b = "    I love Python     "
print(len(a))
print(len(b))

# Strip() rstrip() lstrip()  
a = "         I love Python        "
print(a.strip())   # Strip() => Remove Spaces From Both Sides
print(a.rstrip())  # rstrip() => Remove Spaces From Right Side
print(a.lstrip())  # lstrip() => Remove Spaces From Left Side

a = "#####I love Python#####"
print(a.strip("#"))   # Strip() => Remove Spaces From Both Sides
print(a.rstrip("#"))  # rstrip() => Remove Spaces From Right Side
print(a.lstrip("#"))  # lstrip() => Remove Spaces From Left Side

#title() => Convert The First Character Of Each Word To Uppercase

b = "I Love 2d Graphics and 3g Technology and Python"
print(b.title())   # I Love 2D Graphics And 3G Technology And Python


#capitalize() => Convert The First Character Of The String To Uppercase And The Rest To Lowercase

b = "I Love 2d Graphics and 3g Technology and Python"
print(b.capitalize())   # I love 2d graphics and 3g technology and python

# Zfill() => Fill The String With Zeros Until It Reaches The Specified Width
c, b, e, f = "1", "11", "111", "1111"
print(c)
print(b)
print(e)
print(f)

print(c.zfill(4))   # 0001
print(b.zfill(4))   # 0011
print(e.zfill(4))   # 0111
print(f.zfill(4))   # 1111

#Upper() => Convert All Characters To Uppercase
g = "hussien"

print(g.upper())   # HUSSIEN

# Lower() => Convert All Characters To Lowercase
h = "HUSSIEN" 

print(h.lower())   # hussien