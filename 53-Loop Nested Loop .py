#--------------------------------------
#----Loop => For-----------------------
#----Nested Loop-----------------------
#--------------------------------------


people = ["Hussien", "Ahmed", "Ali"]

Skills = ['Html', 'Css', 'Js']

for name in people : # outer loop
    print(f"{name} Skills IS : ")
    for skill in Skills : # Inner loop
        print(f"- {skill}")


people = {
    "Hussien":{
        "Html":"70%",
        "Css":"80%",
        "Js":"70%"
    },
    "Ahmed":{
        "Html":"90%",
        "Css":"80%",
        "Js":"90%"
    },
    "Ali":{
        "Html":"70%",
        "Css":"60%",
        "Js":"90%"
    }
}        

#print(people["Hussien"])
#print(people["Ahmed"])
#print(people["Ali"])
#print(people["Ali"]['Css'])

for name in people : # outer loop

    print(f"Skill and Progress for {name}  IS : ")

    for skill in people[name] : # Inner loop

        print(f"- {skill} => {people[name][skill]}")

