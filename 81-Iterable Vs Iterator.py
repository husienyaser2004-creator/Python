#-------------------------------------------
#----Iterable Vs Iterator-------------------
#-------------------------------------------
#Iterator
# [1] Object Contains Date That Can Be Iterated Upon 
# [2] Examples (String, List, Set, Tuple, Dictionary)
#-----------------------------------------------------
# Iterator
# [1] Object Used To Iterate over Iterable Using next() Method Return 1 Elemet At A Time
# [2] You Can Generate Iterator From Iterable When Using Iter() Method
# [3] For Loop Already Calls Iter() Method On The Iterable Behind The Scene 
# [4] Gives "StopIteration" If Theres No Next Elemet
#------------------------------------------
myString = "Hussien"

myList = [1, 2, 3, 4, 5, 6, 7]

for Letter in myString:

    print(Letter, end=" ")

for number in myList: 

    print(number, end=" ")

myIterator = iter(myString)

print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))
print(next(myIterator))

for letter in iter("Hussien"):

    print(letter, end=" ")