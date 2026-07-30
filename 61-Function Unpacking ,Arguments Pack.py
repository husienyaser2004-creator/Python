#------------------------------------
#--Function Unpacking ,Arguments Pack
#------------------------------------

myTuple = ("Html", "Css", "Js") 

mySkills = {
    "Html" : "90%",
    "Css" : "80%",
    "Js" : "70%",
    "PHP" : "60%",
    "Python" : "50%",
}

def show_skills(name, *skills, **skillsWithProgress):

  print(f"Hello {name} \nSkills without Progress Is : ")

  for skill in skills:

    print(f"- {skill}")

  print("Skills With Progress Is : ")

  for skill_Key, skill_Value in skillsWithProgress.items():

    print(f"-{skill_Key} => {skill_Value}")

show_skills("Hussien", *myTuple, **mySkills)    