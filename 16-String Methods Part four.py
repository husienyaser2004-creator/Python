#----------------------------------------------
#---------- String Methods Part four ----------
#----------------------------------------------

# replace(old , new , count)

a = " Hello one two Three one one "
print(a.replace("one" , "1"))
print(a.replace("one" , "1" , 1))
print(a.replace("one" , "1" , 2))

# join(iterable)

mylist = ["hussien" , "yasser" , "Soudy"]
print(" ".join(mylist))
print("-".join(mylist))
print(" , ".join(mylist))

print(type(" , ".join(mylist)))