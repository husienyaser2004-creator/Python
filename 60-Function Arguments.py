#-------------------------------------------------------
#--- Function Packing, Unpacking Arguments ** KWArgs ---
#-------------------------------------------------------

from unicodedata import name


from os import name


mySkills = {
  "Html" : "90%",
    "Css" : "80%",
    "Js" : "70%",
    "PHP" : "60%",
    "Python" : "50%",
}

def show_skills( **skills ):

 print(type(skills)) # <class 'dict'>

  #print(f"Hello {name} Your Skills Is : ")

 for skill, value in skills.items():

  print(f"{skill} => {value}")

show_skills(**mySkills)