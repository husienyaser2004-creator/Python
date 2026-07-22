#---------------------------------
#----Loop For and Else------------
#---------------------------------
# item Is A Vairable You Create And Call Whenenver You Want 
# item refer to the current position and will run and visit all visit item to the end
# iterable_object => sequence [ list, tuples, set, dict, string of charcaters, etc...]

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers:
    
    # print(number * 17)

    if number % 2 == 0:  # Even

        print(f"The Number {number} Is Even.")

    else:

        print(f"The Number {number} Is Odd.")     


else: 

    print("The Loop Is Finished")



myname = "Hussien"

for letter in myname:

    print(f"[ {letter.upper()} ]")