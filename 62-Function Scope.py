#------------------------------
#----Function Scope------------
#------------------------------

x = 1 # Global Scope

def one():

    global x # Global Scope

    x = 2 

    print(f"print Varible From Function scope : {x}") # 2

def two():

    x = 3

    print(f"print Varible From Function scope : {x}") # 3    

print(f"print Varible From Global scope : {x}") # 1
one() # Call Function One
two() # Call Function Two
print(f"print Varible From Global scope After One Function Is Called: {x}") # 2    

