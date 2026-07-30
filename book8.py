                      ### Error ###
#خطا نحوي |syntax Error|print("welcome")|نسيان إغلاق القوس             
#خطا منطقي | Logic Error | x = 2*2 ثم الطباعه x = 5 |نتيجه غير صحيحه
# خطا وقت التشغيل | Run time Error | 10\0 |عمليه غير ممكنه اثناء التنفيذ
# خطا نوع البيانات | Type Error | "5" + 5 |محاوله جمع نص مع الرقم
 
num = int(input("enter nuber: "))
print(num)
print("test")
#______________________________________________________
try:
    num = int(input("enter number: "))
    print(num)
except:
    print("invalid value")
print("test")
#_______________________________________________________    
# x = 10\0
#_______________________________________________________
try:
    x = 10/0
    num = int(input("enter number: "))
    print(num)
except:
    print("invalid value")
print("test")
#_________________________________________________________
try:
    x = 10/0
    num = int(input("enter number: "))
    print(num)
except ZeroDivisionError:
    print("division error")
except ValueError:
    print("invalid value")
print("test")    
#___________________________________________________________
try:
    num = int(input("enter number: "))
    print(num)
    x = 10/0
except ZeroDivisionError:
    print("division error")
except ValueError:
    print("invalid value")
print("test")
#___________________________________________________________
try:
    num = int(input("enter number: "))
    print(num)
    x = 10/0
except ZeroDivisionError as error:
    print(error)
except ValueError as error :
    print(error)
print("test")
#_____________________________________________________________
try:
    Value = int(input("enter a number: "))
    print(Value)
except:
    print("invalid input")
print("success")      
#________________________________________________________________  
try:
    result = 10/0
    Value = int(input("enter a  number: "))
    print(Value)
except ZeroDivisionError as err :
    print(err)
except ValueError as err1 :
    print(err1)
    print("success")    
#_________________________________________________________________  
file = open("demo.text","r")                               #قراءه فقط و (لازم يكون الملف موجود) 
file = open("demo.text","r+")                              #قراءه و كتابه
file = open("demo.text","w")                               #كتابه(بيمسح كل اللي في الملف الاول)
file = open("demo.text","w+")                              # (قراءه و كتابه (و بيسمح المحتوي 
file = open("demo.text","a")                               #إضافه اخر الملف 
file = open("demo.text","a+")                              # قراءه +اضافه
#__________________________________________________________________
file = open("demo.text","r")  
print(file.readable())                         #هل الملف قابل للقراءه
file.close()
#__________________________________________________________________
file = open("demo.text","r")
print(file.read())                         #قراءه الملف كامل
file.close()
#___________________________________________________________________
file = open("demo.text","r")
print(file.readline())             #قراءه سطر سطر
print(file.readline())
print(file.readline())
file.close()
#_____________________________________________________________________
file = open("demo.text","r")
print(file.readlines())            #قراءه كل سطر في ليست
file.close()
#_____________________________________________________________________
file = open("demo.text", "r")
for lista in file.readlines():
    print(lista)
file.close()    
#_____________________________________________________________________
file = open("demo.text","r+")                     #بيكتب من اول الملف (و بيمسح جزء من المحتوي)
print(file.write("omar"))
file.close()    
#_____________________________________________________________________
file = open("demo.text","w")                               #كتابه(بيمسح كل اللي في الملف الاول)
print(file.write("omar"))
file.close()    
#_____________________________________________________________________
file = open("demo.text","a")                               #إضافه اخر الملف بدون مسح القديم 
print(file.write("\nhamza"))
file.close()    
#_____________________________________________________________________
file = open("mano.text", "a")
print(file.write("\nhamza"))
file.close()    
#____________________________________________________________________
programming = ["python", "c++","c#","c++"]
for lista in range(len(programming)):
    print(lista)
    print(programming[lista])
#_____________________________________________________________________    
programming = ["python", "c++","c#","c++"]
for lista in range(len(programming)):
    
    print(programming[lista])
#____________________________________________________________________
                             ### Set ###
myset ={"ali" , "mohamed" , "hamza"}
print(myset)
#____________________________________________________________________   
myset ={"ali" , "mohamed" , "hamza"}
print(myset[0])    ###
#____________________________________________________________________
myset ={"ali" , "mohamed" , "hamza" , [1,2,3]} ###
print(myset)    
#____________________________________________________________________
myset ={"ali" , "mohamed" , "hamza" , {"name" : "ahmed" ,}} ###
print(myset)
#___________________________________________________________________
myset ={"ali" , "mohamed" , "hamza" , (1,2,3)} 
print(myset)    
#___________________________________________________________________
                   ### Set methods ###
### Union()   ,    add()      ,    remove()   ,   discard()  ,  clear()   ###              
a = {1,2,3}
b = {4,5,6, "ahmed"}
print(a.union(b))      ##print(a|b)
a.add(10)
a.add(15)
print(a)
b.remove(5)
b.remove("ahmed")
b.remove(20)
b.discard(5)
b.discard("ahmed")
#b.discard(20)
print(b)
a.clear()
print(a)

                          