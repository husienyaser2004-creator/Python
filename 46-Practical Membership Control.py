#-------------------------------------
#--Practical Membership Control-------
#-------------------------------------

# List Contains Admins 
admins = ["Hussien" , "Ali" , "Mohamed" , "Osama", "Rahma"]

#print(admins)
#admins[admins.index("Hussien")] = "soudy"
#print(admins)


# Login 
name = input("Please Type Your Name").strip().capitalize()

# if Name In Admins List 
if name in admins:

    print(f"Hello {name} Welcomre Back")

    option = input("Delete Or Update Your Name ?").strip().capitalize()


# Update OPtion

    if option == "Update": 

        theNewName = input("Your New Name please ").strip().capitalize()

        admins[admins.index(name)] = theNewName

        print("Name Updated")

        print(admins)

# Delete Option

    elif option == "Delete":

        admins.remove(name)

        print("Name Deleted")

        print(admins)

# Wrong Option

    else:

       print("wrong Option Choosed")



else:

  status = input("Not Admin, Add You Y, N ? ").strip().capitalize()
    
if 'status' == "Yes" or 'status' == "Y": 

        print("You HAve Been Added")

        admins.append(name)

        print("Name Added")

        print(admins)
 
else:

    print("You Are Been Added")