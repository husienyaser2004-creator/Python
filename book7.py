                                ### Functions ###
z="hello"
print(z.lower())
#_________________________________________________________
z="HELLO"
print(z.lower())
#_________________________________________________________
z="hello world python"
print(z.title())
#_________________________________________________________
z="hello world python"
print(z.capitalize())
#__________________________________________________________
print(pow(3,3))
#__________________________________________________________
def firstfunction():
    print("hello world")
print("hello world")
firstfunction()
#__________________________________________________________
def say_hello():
    print("welcome in programming")
say_hello()
#__________________________________________________________
def say_Hi():
    print("hello user")
print("frist")
say_Hi()
print("second")
#__________________________________________________________
def firstfunction(name):
    print("my name is: " + name)
firstfunction("ahmed")
#__________________________________________________________
def firstfunction(name,age):
    print("my name is: " + name+", your age is: "+ age)
firstfunction("ahmed","25")
#___________________________________________________________
def firstfunction(name,age):
    print("my name is: " + name+"your age is: "+ str(age))
firstfunction("ahmed",25)
#___________________________________________________________
def cube(num) :      ### 
    num*num*num      ###
cube(3)              ###
#___________________________________________________________
def cube(num) :      ##
    num*num*num      ##
print(cube(3))       ##
#___________________________________________________________ 
def cube(num) :         ##
   return num*num*num   ##
resuit = cube(4)        ##
print(cube(3))          ## 
#___________________________________________________________
def cube(num) :         ##
   return num*num*num   ##
resuit = cube(4)        ##
print(resuit)
#___________________________________________________________
def cals(num1,num2) :
    return num1+num2
print(cals(5,9))
#___________________________________________________________
def cals(num1,num2):
    return num1+num2
print("aaaaaaaaa")
print(cals(5,9))
#_____________________________________________________________
def calcdays(age):
    return "your age is : "+ str(age +365)+"days"
print(calcdays(20))
#____________________________________________________________
def calchours(age):
    return "your age is : "+ str(age*365*24)+"hours"
print(calchours(20))
#____________________________________________________________
def calcdays(age):
    return "your age is : "+ str(age*365)+"days"
print(calcdays(input("enter your age: ")))
#____________________________________________________________
def calcdays(age):
    return "your age is : "+ str(age*365)+"days"
print(calcdays(int(input("enter your age: "))))
#____________________________________________________________
              ####Dictionary###
info = {
"name"         : "ahmed",
"age" #/111#   : 25,
"country"  : "egypt", 
}
print(info)

print(info["name"])
print(info.get("name"))
print(info.get("id"))
print(info.get("fffff","not found"))       
