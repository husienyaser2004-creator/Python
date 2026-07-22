#---------------------------------------------
#------String Formatting----------------------
#---------------------------------------------

name = "Hussien"
age = 36
rank = 10

print("my name is : " + name)
#print("my name is : " + name + " and my age is : " + age) #Type Error

print("my Name is: %s" % " Hussien")
print("my Name is: %s " % name)
print("my Name is: %s and my age is: %d" % (name , age))
print("my Name is: %s and my age is: %d and my rank is: %f" % (name , age , rank))

# %s : string
# %d : Namber
# %f : float

n = "hussien"
l = "python"
y = 10

print("my name is %s I am %s Developer with %d years Exp" % (n , l , y))

# Control Floating Point Number

myNumber = 10
print("my number is: %d" % myNumber)
print("my number is: %f" % myNumber)
print("my number is: %.2f" % myNumber)

# Truncate String
mylongString = "Hello People of Elzero wed School I Love You All"
print("message is: %s" % mylongString)
print("message is: %.5s" % mylongString)
