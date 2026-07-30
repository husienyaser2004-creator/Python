#-------------------------------------------
#----- Nested If ---------------------------
#-------------------------------------------

uName = "Hussien"
isStudent = "Yes"
uCountry = "Egypt"
cName = "python Course"
cprice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

    if isStudent == "Yes":


     print(f"Hi {uName}, Because you are from {uCountry} And Student")
     print(f"The Course \"{cName}\" price Is: ${cprice - 90}")


elif uCountry == "Kuwait" or uCountry == "Bahrain" :
    print(f"Hi {uName}, Because you are from {uCountry}")
    print (f"The Course \"{cName}\" price Is: ${cprice - 70}")


else : 
    print(f"Hi {uName}, Because you are from {uCountry}")
    print(f"The Course \"{cName}\" price Is: ${cprice - 30}")