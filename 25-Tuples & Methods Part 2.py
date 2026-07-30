#------------------------------------
#---- 25-Tuples & Methods Part 2-----
#------------------------------------

# Tuple With One Element
myTuple1 = ("Hussien")
myTuple2 = "Hussien"

print(myTuple1) # Output: Hussien
print(myTuple2) # Output: Hussien

print(type(myTuple1)) # Output: <class 'str'>
print(type(myTuple2)) # Output: <class 'str'>

print(len(myTuple1)) # Output: 8
print(len(myTuple2)) # Output: 8

# Tuple Concatenation
a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A" , "B" , True) + b 

print(c) # Output: (1, 2, 3, 4, 5, 6)
print(d) # Output: (1, 2, 3, 4, 'A', 'B', True, 5, 6)

# Tuple, List, String Repeat(*)

myString = "Hussien"
myList = [1, 2, 3]
myTuple = ("A" , "B")

print(myString * 6) # Output: HussienHussienHussien
print(myList * 6) # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(myTuple * 6) # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Methods => Count()
a = (1, 2, 3, 4, 5, 1, 2, 1)
print(a.count(1)) # Output: 3

# Methods => Index()
b = (1, 3, 7, 8, 2, 6, 5)
#print("The Position of index Is: " + b.index(7)) # Output: The Position of 6 is: 5
print("The Position of Index Is : {:d}".format(b.index(7))) # Output: The Position of 6 is: 5
print(f"The Position of Index Is : {b.index(7)}") # Output: The Position of 6 is: 5

# Tuple Destruct

a = ("A" , "B" , 4 , "C" )
x, y, _, z = a
print(x) # Output: A
print(y) # Output: B
print(z) # Output: C