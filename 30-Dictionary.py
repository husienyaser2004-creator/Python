#-------------------------------
#-----Dictionary-----
#-------------------------------

# [1] Dict Itmes Are Enclosed In Curly Braces {}
# [2] Dict Items Are Key : Value
# [3] Dict Key need to be Immutable (String, Number, Tuple) list Not Allowed 
# [4] Dict Value Can Have Any Data Type (String, Number, List, Tuple, Dict)
# [5] Dict Itmes Need To Be Unique (No Duplicate Keys Allowed)
# [6] Dict Is Not Ordered You Access Its Elements With Key 

# Dictionary 

user = {
    "name": "Hussien",
    "age":36,
    "country": "Egypt",
    "Skills": ["Python", "JavaScript", "C++"],
    "rating": 10.5,
    "name": "Soudy"
}

print(user)
print(user['country'])
print(user.get("country"))

print(user.keys())
print(user.values())


# Two-Dimensional Dictionary

languages = {
    "One": {
        "name": "Python",
        "progress": "80%"
    },
    "Two": {
        "name": "JavaScript",
        "progress": "70%"
    },
    "Three": {
        "name": "C++",
        "progress": "60%"
    }
}

print(languages)
print(languages["One"])
print(languages["Two"]["name"])

# Dictionary Length
print(len(languages))
print(len(languages["Two"]))

# create Dictionary From Variabls

frameworkOne = {
    "name": "Django",
    "progress": "80%"
}

frameworkTwo = {
    "name": "ReactJs",
    "progress": "80%"
}

frameworkThree = {
    "name": "ReactJs",
    "progress": "80%"
}

all_frameworks = {
    "One": frameworkOne,
    "Two": frameworkTwo,
    "Three": frameworkThree
}

print(all_frameworks)