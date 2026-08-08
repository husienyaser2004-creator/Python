#---------------------------------
#---Built In Functions Part ------
#--------------------------------
# abs()
# pow()
# min()
# max()
# slice()
#----------------------------------------

# abs ()
print(abs(100))
print(abs(-100))
print(abs(10.19))
print(abs(-10.19))

print("#" * 50)

# pow (base,exp , mod) => power
print(pow(2, 5)) # 2*2*2*2*2 = 32
print(pow(2, 5 , 10)) # (2*2*2*2*2) % 10 = 2
print("#" * 50)

# min (item, item , item or iterable)
myNumber = [1 , 20, -50 , -100 , 100]
print(min(1, 10, -50 , 20 , 30))
print(min("x" , "Z" , "hussien"))
print(min(myNumber)) 

print("#" * 50)

# max (item, item , item or iterable)
myNumber = [1 , 20, -50 , -100 , 100]
print(max(1, 10, -50 , 20 , 30))
print(max("x" , "Z" , "hussien"))
print(max(myNumber)) 

print("#" * 50)

# slice (start, stop, step)
a = ["A" , "B" , "C" , "D" , "E" , "F"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2 , 5)])



