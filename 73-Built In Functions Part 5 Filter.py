#------------------------------------
#--Built-In Functions => Filter------
#------------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every
# [3] The Function Can Be Pre Defined Function Or Lambda Function
# [4] Filter Out Elements s For Which The Function Return False
# [5] The Function Need To Return Boolean Value
#---------------------------------------------------------------------


# Example 1 

def checkNumber(num):
        
        return num > 10

myNumber = [0, 0, 1, 19, 10, 20, 100, 5, 0]  

myResult = filter(checkNumber, myNumber)

for number in myResult:
    
    print(number)


print("#" * 50)


# Example 2 

def checkName(name):
        
        return name.startswith("H")

myText = ["Hussien", "Ali", "Hassan", "Amr", "Harm"]  

myReturnDate = filter(checkName, myText)

for person in myReturnDate:
    
    print(person)


print("#" * 50)


# Example 3

#def checkName(name):
        
#        return name.startswith("H")

myNames = ["Hussien", "Ali", "Hassan", "Amr", "Harm", "Araby"]  

myReturnDate = filter(checkName, myNames)

for p in filter(lambda name: name.startswith("A"), myNames):
    
    print(p)
