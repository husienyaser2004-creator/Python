#------------------------------------------
#------- Set ------------------------------
#------------------------------------------
# [1] Set Items Are Enclosed in Curly Braces {}
# [2] Set Itmes Are Not Ordered And Not Indexed
# [3] Set Indexing And Slicing Cant Be Done 
# [4] Set Has Only Immutable Data Types (String , Number , Tuple) List And Dict Are Not
# [5] Set Itmes Is Unique 
#-------------------------------------------

# Not Ordered And Not Indexed
mySetone = {"Hussien", "Ahmed" , 100}
print(mySetone) # Output: {'Hussien', 'Ahmed', 100}

# Slicing Cant Be Done 
mySetTwo = {1, 2, 3, 4, 5, 6}
#print(mySetTwo[0:3]) # Output: (1, 2, 3)

# Has Only Immutable Data Types
#mySetThree = {"Osama", 100, 10.5, True , [1, 2, 3]} # Unhashable Type: 'list' 
mysetThree = {"Osama", 100, 10.5, True , (1, 2, 3)} # Output: {'Osama', 100, 10.5, True, (1, 2, 3)} 

#Set Itmes Is Unique 
mysetFour = { 1, 2, "Hussien", "one" , "Hussien", 1}
print(mysetFour) # Output: {1, 2, 'Hussien', 'one'}