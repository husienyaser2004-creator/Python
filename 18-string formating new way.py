#--------------------------------
# -String Formatting New Way-----
#--------------------------------

name = "Hussien"
age = 36
rank = 10

print("my name is : " + name)
#print("my name is : " + name + " and my age is : " + age) #Type Error

print("my Name is: {}".format("Hussien"))
print("my Name is: {}".format(name))
print("my Name is: {} and my age is: {}".format(name, age))
print("my Name is: {} and my age is: {} and my rank is: {}".format(name, age, rank))

# {:s} : string
# {:d} : number
# {:f} : float

n = "hussien"
l = "python"
y = 10

print("my name is {} I am {} Developer with {} years Exp".format(n, l, y))

# Control Floating Point Number

myNumber = 10
print("my number is: {}".format(myNumber))
print("my number is: {:f}".format(myNumber))
print("my number is: {:.2f}".format(myNumber))

# Truncate String
mylongString = "Hello People of Elzero wed School I Love You All"
print("message is: {}".format(mylongString))
print("message is: {:.5s}".format(mylongString))
print("message is: {:.13s}".format(mylongString))


# Format Mony

myMoney = 500162350198
print("my money in Bank is: {}".format(myMoney))
print("my money in Bank is: {:_d}".format(myMoney))
print("my money in Bank is: {:,d}".format(myMoney))

# ReArrange Items
a, b, c = "One", "Two", "Three"
print("Hello {} {} {}" .format(a, b, c)) #Hello One Two Three
print("Hello {1} {2} {0}" .format(a, b, c)) #Hello Two Three One
print("Hello {2} {0} {1}" .format(a, b, c)) #Hello Three One Two

x, y, z= 10, 20, 30
print("Hello {} {} {}" .format(x, y, z)) #Hello 10 20 30
print("Hello {1:d} {2:d} {0:d}" .format(x, y, z)) #Hello 20 30 10
print("Hello {2:.2f} {0:.3f} {1:.4f}" .format(x, y, z)) #Hello 30.00 10.000 20.0000

# Format in version 3.6+

myName = "Hussien"
myAge = 36

print("my Name is : {myName} and my age is : {myAge}")
print(f"my Name is : {myName} and my age is : {myAge}")



