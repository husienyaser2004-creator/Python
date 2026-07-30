#----------------------------------------
#-----Loop => While Training ------------
#----- Simple Password Guess ------------

tries = 4
mainpassword = "hussien@123"

inputpassword = input("write Your Password: ")

while inputpassword != mainpassword: # True

    tries -= 1 # tries = tries - 1

    print(f"wrong password, {'Last'if tries == 0 else tries} chance Left")

    inputpassword = input("write Your Password: ")

    if tries == 0:

        print("All Tries Is Finished.")

        break
        
        print("Will Not print")


    else:

        print("Correct Password")