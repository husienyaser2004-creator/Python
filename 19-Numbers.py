#-----------------------------------------
#----Numbers--------------------
#-----------------------------------------

# Integer
print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# Float
print(type(1.500))
print(type(100.99))
print(type(-100.99))
print(type(.99))

# Complex
print(type(5+6j))

mycomplexNumber = 5+6j

print(type(mycomplexNumber))

print("Real part Is: {}".format(mycomplexNumber.real))
print("Imaginary part Is: {}".format(mycomplexNumber.imag))


#[1] You can Convert Form Int To Float or Complex
#[2] You can Counvert Form Float To Int or Complex
#[3] You can Canvert Form Complex To Float Or Int But You Will Get An Error

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(5+6j)
print(int(5+6j))
print(float(5+6j))
