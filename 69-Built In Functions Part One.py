#---------------------------------
#--Built In Functions Part One----
#---------------------------------
# all()
# any()
# bin()
# id()
#----------------------------------


x = [1, 2, 3, 4]

if all(x):

    print("All Elements Are True")

else:

    print("Theres At Least One Element That Is False")    


x = [0, 0, []]

if any(x):

    print(" There's At Least One Element Is True")

else:

       print("Theres No Any True Element ")    


print(bin(100))

a = 1
b = 2

print(id(a))
print(id(b))


    