#---------------------------------
#------Function Lambda------------
#---------------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can It In Return Data From Another Function
# [4] Lambde Used For Simple Function and Def Handle The Function 
# [5] Lambda is One Single Expression not Block Of Code 
# [6] Lambde Type is Function 
#-------------------------------------------------------------------

from unicodedata import name


from os import name


def say_hello(name, age ) : return f"Hello {name} Your Age Is {age}"

hello = lambda name, age : f"Hello {name} Your Age Is {age}"

print(say_hello("Hussien", 22))
print(hello("Hussien" , 22))

print(say_hello.__name__)
print(hello.__name__)

