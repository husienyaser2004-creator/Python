#---------------------------------------------
#--Calculate Age Advanced Version ------------
#---------------------------------------------

# Wite Note
print("#" * 80)
print("You Can Write The First Letter Or Full Name Of The Time Unit ".center(80, '#'))
print("#" * 80)

# Collect Age Data 
age = input ("Please Enter Your Age ") . strip()

# Collect Time Unit Data 
Unit = input ("Please Enter Your Time Unit (Year, Month, Day) ") . strip().lower()

# Get Time Units 
months = int (age) * 12
Weeks = months * 4
Days = int(age) * 365

if Unit == 'months' or Unit == 'm':

    print("You Choosed The Unit Months")
    print(f"Your  live For {months:,} months.")


elif Unit == 'weeks' or Unit == 'w':

    print("You Choosed The Unit Weeks")
    print(f"Your  live For {Weeks:,} Weeks.")    


elif Unit == 'days' or Unit == 'd':

    print("You Choosed The Unit Days")
    print(f"Your  live For {Days:,} Days.")