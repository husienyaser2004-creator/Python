#-----------------------------------------
#----Modules Part 2 - Create Your Module--
#-----------------------------------------

#import sys
#sys.path.append(r"D:\Games")
#print(sys.path)

import elzero 
print(dir(elzero))


elzero.sayHello("Ahmed")
elzero.sayHello("Hussien")
elzero.sayHello("Mohamed")

elzero.sayHowAreYou("Ahmed")
elzero.sayHowAreYou("Hussien")
elzero.sayHowAreYou("Mohamed")

# Alias 

import elzero as ee 

ee.sayHello("Ahmed")
ee.sayHello("Hussien")
ee.sayHello("Mohamed")

ee.sayHowAreYou("Ahmed")
ee.sayHowAreYou("Hussien")
ee.sayHowAreYou("Mohamed")


from elzero import sayHello

sayHello("Hussien")


from elzero import sayHello as ss

ss("Hussien")

