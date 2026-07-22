#---------------------------
#---If, Elif, Else----------
#---------------------------

uName = "Hussien"
uCountry = "Kuwait"
cName = "python Course"
cprice = 100

if uCountry == "Egypt":
    print(f"Hello {uName}, Because you are from {uCountry}")
    print (f"The Course \"{cName}\" price Is: ${cprice - 80}")


elif uCountry == "KSA":
    print(f"Hello {uName}, Because you are from {uCountry}")
    print (f"The Course \"{cName}\" price Is: ${cprice - 70}")


else : 
    print(f"Hello {uName}, Because you are from {uCountry}")
    print(f"The Course \"{cName}\" price Is: ${cprice - 30}")