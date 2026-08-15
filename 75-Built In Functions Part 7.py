#-----------------------------------
#---Built In Functions Part 7-------
#-----------------------------------

# enumerate(iterable, start=0) -> enumerate object

mySkills = ["Python", "PHP", "CSS", "Js"]

mySkillwithCounter = enumerate(mySkills, 20)

print(type(mySkillwithCounter))

for counter , skill in mySkillwithCounter:
    print(f"{counter} - {skill}")


print("#" * 50)

# help()

# print(help(print))


print("#" * 50)


# reversed(iterable) -> reverse iterator

myString = "Hussien"

print(reversed(myString))

for letter in reversed(myString):
    
    print(letter)   
    