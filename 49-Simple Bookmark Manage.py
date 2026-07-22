#------------------------------------------
#--Loop => While Training -----------------
#--- Simple Bookmark Manage ---------------
#------------------------------------------

# Empty List To Fill Later
MyFavouritewebs = []

# Maxium Allowed Websites
maximumwebs = 5

while maximumwebs > 0 :

    # Input The New Website
    web = input("Website Name Without https://")

    # Add The New  website To The List 
    MyFavouritewebs.append(f"https://{web.strip().lower()}")

    # Decrease One Number From Allowed Websites 
    maximumwebs-= 1 # maximumwebs = maximumwebs - 1

    # print The Add Message 
    print(f"website Added, {maximumwebs} places Left")

    # Print The List 
    print(MyFavouritewebs)

else:

    print("Bookmark Is Full, You Cant Add More")

    # Check If List Not Empty 
    if len(MyFavouritewebs) > 0 :

    # Sort The List 
        MyFavouritewebs.sort() 

    index = 0 

    print("printing The List Of Websites in Your Bookmark")

    while index < len(MyFavouritewebs) : 

        print(MyFavouritewebs[index])

        index += 1 # index = index + 1