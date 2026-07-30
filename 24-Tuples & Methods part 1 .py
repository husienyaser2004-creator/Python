#------------------------------------------
#------- Tuples & Methods part 1-----------
#------------------------------------------
# [1] Tuple Items Are Enclosed in parentheses
# [2] You Can Remove The Prentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item 
# [4] Tuple Are Immutable => You Cant Add Or Delete 
# [5] Tuple Items Is Not Unique
# [6] Tuple Items Can Be Of Any Data Type
# [7] Operators Used in Strings and Lists Available in Tuple

# Tuple Syntax & Type Test
myAwesomeTupleone = ("Hussien", "Yasser")
myAwesomeTupletwo = "Hussien", "Yasser"
print(myAwesomeTupleone)
print(myAwesomeTupletwo)
print(type(myAwesomeTupleone))
print(type(myAwesomeTupletwo))

# Tuple Indexing

myAwesomeTupleThree = ( 1, 2, 3, 4, 5 )
print(myAwesomeTupleThree[0]) # Accessing the first item
print(myAwesomeTupleThree[-1]) # Accessing the last item
print(myAwesomeTupleThree[-3]) # Accessing the third item from the end

# Tuple Assign Values
#myAwesomeTupleFour = ( 1, 2, 3, 4, 5 )
#myAwesomeTupleFour[2] = "Three"
#print(myAwesomeTupleFour) # 'tuple' object does not support item assignment

# Tuple items 

myAwesomeTupleFive = ( "Hussien", "Hussien", 1, 2, 3, 100.5 , True)
print(myAwesomeTupleFive[1])
print(myAwesomeTupleFive[-1])
