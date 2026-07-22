#----------------------------------
#----Loop While Training's-------
#----------------------------------
# while Condition_is_True:
# code Will Run Until Condition Become False

myf = ["Hu" , "Os" , "Ga" , "Al" , "Ra" , "So" , "MM", "WW"]

# print(Len(myf)) # List Length [10]

a = 0 


while a < len(myf): # 0 < 10

    print(f"#{str(a+1).zfill(2)} {myf[a]}") # 01 Hu
    
    a += 1 # a = a + 1 


else:

    print("All Friends Printed Too Screen.") # True Become False


#print(myf[0])
#print(myf[1])
#print(myf[2])
#print(myf[3])
#print(myf[4])
#print(myf[5])
#print(myf[6])
#print(myf[7])
#print(myf[8])
#print(myf[9])
#print(myf[10])