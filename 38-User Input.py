#------------------------------
#------User Input -------------
#------------------------------

fName = input('What\'s Is Your First Name?')
mName = input('What\'s Is Your Middel Name?')
IName = input('What\'s Is Your Last Name?')

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
IName = IName.strip().capitalize()

print(f"Hello {fName} {mName:.1s} {IName} Happy To See You. ")



