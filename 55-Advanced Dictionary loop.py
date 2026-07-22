#-------------------------------------
#------Advanced Dictionary loop-------
#-------------------------------------

mySkills = {
    "Html":"90%",
    "Css":"60%",
    "PHP":"70%",
    "Js":"80%",
}

#print(mySkills.items())
#for skill in mySkills:

    #print(f"{skill} => {mySkills[skill]}")

#for skill_key, skill_progress in mySkills.items():
 #   print(f"{skill_key} => {skill_progress}")    


myUltimateSkills = {
     "Html":{
         "Main" : "80%",
         "Pugjs" : "80%",
     },  
     "Css": {
         "Main" : "60%",
         "Sass" : "70%"
     }
 }     

for main_key, main_value in myUltimateSkills.items():

    print(f"{main_key} Progress Is: ")

    for child_Key, child_progress in main_value.items():

        print(f"-{child_Key} => {child_progress}")

