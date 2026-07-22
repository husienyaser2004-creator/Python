#----------------------------------------
#---Membership Operators-----------------
#----------------------------------------
# iN 
# Not in
#----------------------------------------

# String

name = "Hussien"
print("H" in name) # True
print("a" in name) # False
print("s" in name) # True
print("e" in name) # True

print("#" * 50)

# List

Friends = ["Hussien", "Ali", "Mohamed"]

print("Hussien" in Friends) # True
print("Ali" in Friends) # True
print("Mohamed" not in Friends) # False

print("#" * 50)

# Using In And Not In With Condition

Countriesone = ["Egypt", "KSA", "Kuwait", "Bahrain"]
CountriesoneDiscount = 80


Countriestwo = ["USA", "Canada", "Germany", "France"]
CountriestwoDiscount = 50


myCountry = "Egypt"

if myCountry in Countriesone:
    print(f"Hello You Have A Discount Equal To {CountriesoneDiscount}")


elif myCountry in Countriestwo:
    print(f"Hello You Have A Discount Equal To {CountriestwoDiscount}")


else :
    print("You Have No Discount")