#----------------------------------
# Strings Indexing & Slicing
# [1] All Data in python is object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing(Index Start From 0)
# [5] Use [] To Access An Element In The String 
# [6] Enable Accessing Part Of The String, Tuples or Lists 
#----------------------------------

# Indexing ( Access Single Item )

mystring = "I Love Python"

print(mystring[0])      # Index 0 => I 
print(mystring[9])      # Index 9 => t 

print(mystring[-1])      # Index -1 => n Frist Index Character The End
print(mystring[-6])      # Index -6 => P Frist Index Character The End

# Slicing ( Access Multiple Sequence Items )
# [Start : End ]
# [Start : End : Step ]
print(mystring[8:11])     # Index 8:11 => yth 
print(mystring[3:5])      # Index 3:5 => Ov

print(mystring[:10])     # If Start Is Not Here Will Start From 0 # Index :10 => (I Love Pyt)
print(mystring[5:])      # If End Is Not Here Go To The End # Index 5: => (e Python) 
print(mystring[:])   # Full Data 

print(mystring[0::1])   #  Full Data 
print(mystring[::1])   #  Full Data 

print(mystring[::2])   # Step 2 => I o ePton
print(mystring[::3])   # Step 3 => I L yhn
