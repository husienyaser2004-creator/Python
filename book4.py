age= int(input("how old are you ?"))
nationality = input("what's your nationality: ")
if age>= 18 and nationality== " egyptian" :
    print("yuo are eligible to register ")
else :
    print("not eligible to reglister")
#____________________________________________________________
age= int(input("how old are you ?").strip())
nationality = input("what's your nationality: ").strip()
if age>= 18 and nationality== " egyptian" :
    print("yuo are eligible to register ")
else :
    print("not eligible to reglister")
#_____________________________________________________________
                  ###Loop###
                  
                  #while Loop#
i = 1 
while i<=10 :
    print(i)
    i = i+1     ##i+=1
#______________________________________________________________
i = 1
while i<=5 : 
    print("the number is", i)
    i+=1
#______________________________________________________________
i = 1
while i<=10 : 
   i =i=1         ## i+1 
   print(i)
#______________________________________________________________ 
i = 1
while i <=10 :
    print(i)
    i+=1 
else:
    print("the condition is not true")
#_______________________________________________________________
i = 1 
while i<=10 :
    i = i=1          ## i+=1
    if i == 8: 
        continue
    print(i)
#________________________________________________________________
i = 1 
while i<=10 :
    i = i=1          ## i+=1
    if i == 8: 
        break
    print(i)                        
#_________________________________________________________________
###تكتب برنامج بيسأل المستخدم سؤال دة لو جاوب عليه صح يبقي هو كسب 
# ولو مجاوبش صح يبقي مكسبش تعيد السؤال لحد ما يجاوب عليه
secret_answer = "cairo"
answer = " "
while secret_answer != answer :
    answer = input(" what's the capital of Egypt?")
print("you win")
#__________________________________________________________________
secret_answer = "cairo"
answer = " "
count = 0
limit = 3
lose = False          ###lose = 15
while secret_answer != answer and not lose :       ###lose==15:
    if count < limit :
       answer = input("what's the capital of Egypt?")
       count +=1
    else :
        lose = True             ###lose=14

if lose:
    print("you lose") 
else:
     print("you win")
#__________________________________________________________________     
                              #For Loop#
for name in "ali" :
    print(name)
#---------------------------------------------
x ="ali"
for name in x :
    print(name)
#---------------------------------------------
x =["ali , hazem , rahma"]
for name in x :
    print(name)
#---------------------------------------------
for i in range(5):
     print("welcome number", i)
#---------------------------------------------
for x in range(5,12) :
    print(x)
#---------------------------------------------     
for i in range(1, 6):
    if i == 3:
     continue
    print("the number", i )
#---------------------------------------------    
name ="ahmed"
print(len(name))
#---------------------------------------------
print(len("programming"))
#---------------------------------------------
name = "ahmed"
for x in range(len(name)) :       #for x in range(5)
    print(x) 
#---------------------------------------------
    