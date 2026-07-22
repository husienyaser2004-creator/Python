#---------------------------------
#------Loop=> For-----------------
#------Trainings------------------
#---------------------------------

# Range 

#myRange = range(1, 101)

#for number in myRange:
    
#    print(number)

# Dictionary

mySkills = {
    "Html":"90%",
    "Css":"60%",
    "PHP":"70%",
    "Js":"80%",
    "python":"90%"

}

#print(mySkills['Js'])
#print(mySkills.get("python"))

for skill in mySkills :
    #print(skill)

    print(f"My progress in lang {skill} Is: {mySkills[skill]}")