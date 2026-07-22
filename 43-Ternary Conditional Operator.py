#---------------------------------
#---Ternary Conditional Operator---
#---------------------------------

from ast import If


Country = "a"

if Country =="Egypt":

   print(f"The Weather in {Country} is 15")

elif Country =="KSA":

   print(f"The Weather in {Country} is 30")

else :

   print("Country is not in the list")

   
# Short If

movieRate = 18
age = 20

if age < movieRate:

    print("Movie is Not Good 4U") # Conditional If True 

else : 
   
    print("Movie is Good 4U And Happy Watching") # Conditional If False

    print("Movie is Not Good 4U"if age < movieRate else "Movie is Good 4U And Happy Watching") # Short If Else

    # Conditional If True | If Condition | Else | Conditional If False