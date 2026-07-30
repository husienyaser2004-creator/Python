#--------------------------------
#--- Function Default Parameters-
#-------------------------------

def say_hello(name, age, country = "Unknown"): 

   print(f"Hello {name} Your Age Is {age} And Your Country Is {country}")

say_hello("Hussien", 22, "Egypt")
say_hello("Ahmed", 25, "KSA")
say_hello("Mohamed", 30)