#--------------------------------------
#---function Arguments Unpack ,pack----
#--------------------------------------

def say_hello(*peoples):
 
 #peoples = [n1, n2, n3, n4]

 for name in peoples:

    print(f"Hello {name}")

say_hello("Hussien", "Ahmed", "Ali", "Sayed", "Mahoud")   



def say_hello(name, *skills):

  print(f"Hello {name} Your Skills Is : ")

  for skill in skills:

    print(skill)

say_hello("Hussien", "Html", "Css", "Js", "PHP", "Python")
say_hello("mohamed", "Html", "Css", "Js", "PHP", "Python", "mySQL")



