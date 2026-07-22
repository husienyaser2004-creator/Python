#-----------------------------------
#--------------- Lists ----------
#-----------------------------------

# [1] Lista Itmes Are Enclosed in Square Brackets []
# [2] List Are Ordered , To Use Indexing To Access Items
# [3] List Are Mutable => You Can Change , Add , Delete , Edit
# [4] List Itmes Is Not Unique 
# [5] List Can Have Different Data Types
#---------------------------------------------------------------

myAwesomeList = ["One", "two", "one", 1, 100.5, True]

print(myAwesomeList)  # Whole List
print(myAwesomeList[1]) #"one"
print(myAwesomeList[-1]) # True
print(myAwesomeList[-3]) # 1

print(myAwesomeList[1:4]) # ["two", "one", 1]
print(myAwesomeList[:4]) # ["One", "two", "one", 1]
print(myAwesomeList[1:]) # ["two", "one", 1, 100.5, True]

print(myAwesomeList[1: ]) # ["two", "one", 1, 100.5, True]

print(myAwesomeList[::1]) # ["One", "two", "one", 1, 100.5, True]
print(myAwesomeList[::2]) # ["One", "one", 100.5]

print(myAwesomeList)
myAwesomeList[1] = 2
myAwesomeList[-1] = False
myAwesomeList[0:3] = ["A", "B", "C"]
print(myAwesomeList)  