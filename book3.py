###الطرق الخمسه المختلفه لجمع رقمين
a=10
b=3
z=a+b
print(a+b)
print(3+10)
print(z)
print("the sum is: "+str(a+b))
print("the sum is: ",a+b)
#__________________________________________
a=10
b=3
print("the sum is: ", a+b)
print("the difference is: ", a-b)
print("the multiplication: ", a*b)
print("the division: ", a/b)
print("the modulus: ", a%b)
#___________________________________________
         ##Logical Operations###    (True/fales)
         #(==)  (!=)  (>)  (<)  (>=)  (<=)
#-------5==5,,5!6,,10>3,,5>9,,5>=5,,3<=5
x=5
z=10
y=5
b=5
print(x==y)      #true 
print(z>b)       #true
print(x<b)       #fales
print(z!=y)      #true
print(x!=y)      #fales
print(y>z)       #fales
print(z>=b)      #true
print(x<=y)      #true
#___________________________________________
x=7
print(x>3)
#___________________________________________
x=10
y=3
print(x!=y)
#___________________________________________
x=10
y=5
print("is greater than y",x>y)
print("is x equal y", x==y)
#___________________________________________
   ###برنامج يدخل رقمين و يحسب محموع رقمين و يتحقق هل المجموع الرقمين اكبر من 100
a= int(input("enter the first num: "))
b=int(input("enter the second num "))
total=a+b
print("the sum is: ", total)
print("is the sum greater than 100", total>100)
#____________________________________________
            ### Logical operations ###   (true/fales)
            ###    ( and , or , not )
a=5
y=10
print( x<9 and y>8 )                    #and لما يكون الناتجين ترو لما بتيجي تطبع غير مره واحدة
print( x<9 or y==8 )                    # or يكون الناتجين فولس لما تيجي تطبع مش بتطبع غير مره واحدة
print( not(x==5))                       # not الناتج اللي ميطلع في القوس اعكسه
#_______________________________________________
                                   ### Functions###
print(pow(2,3))
print(abs(-12))
print(max(3,9,15))
print(min(2,5,15,20))
#_______________________________________________
from math import *
print(round(5.3))
print(floor(5.9))
print(floor(-2.1))
print(ceil(5.1))
#________________________________________________
                   ### IF / Else 
#الشرط 
#if: 
#   تنفيذ اذا تحقق الشرط 
#Else:
#  تنفيذ اذا لم يتطبق الشرط 
#________________________________________________
egyptian = True 
if egyptian == True:
     print("Iam egyptian")
#_________________________________________________     
egyptian = True
if egyptian  :
    print("Iam egyptian")
#_________________________________________________    
egyptian = False
if  not egyptian  :
   print("Iam French")  
#__________________________________________________
egyptian = True
if egyptian  : 
   print("Iam egyption")
else :
    print("Iam french")
#__________________________________________________
age=int(input("how old are you ?"))
if age>=18:
    print("welcome to the site")
else : 
    print("sorry, you must be >= 18")
#___________________________________________________
#IF شرط :
#                           تنفيذ 1
#elif شرط2
#                           2 تنفيذ 
#else:
#                            3 تنفيذ 
#____________________________________________________
email = "x@gmail.com"
password = 1234
if email == "x@gmail.com" and password == 1234 :  
    print("welcome")
elif email == "x@gmail.com" and password != 1234 :
    print("invalid password")
elif email != "x@gmail.com" and password == 1234 :
    print("invalid emali")
else :
    print("invalid email and password")
#______________________________________________________
temp = int(input("enter the temperature: "))
if temp >30 :
    print("it's very hot")
elif temp >= 20 :
     print("it's fline day ")
else :
     print("it's cold")
#______________________________________________________            