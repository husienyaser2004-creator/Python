#-----------------------------------
#--Function Parameters + Arguments--
#-----------------------------------

a, b, c = "Hussien" , "Ahmed" , "Sayed"

print(f"Hello {a}")
print(f"Hello {b}")
print(f"Hello {c}")

# def                            => Function Keyword(Define Function)
# say_hello                      => Function Name
# name                           => Function Parameter
# print(f"Hello {name}")         => task of the function
# say_hello("Hussien")            => Hussien is The Argument    

def say_hello(n):
    print(f"Hello {n}")

say_hello("Hussien") # Hussien is The Argument  

say_hello('a')
say_hello('b')
say_hello('c')

def addition(n1, n2):
    print(n1 + n2)

addition(100, 300)
addition(-50, 100)

def addition(n1, n2):
    if type(n1) != int or type(n2) != int:
       print("only integers allowed")

    else:
        print(n1 + n2)

addition(100, 500)        


def full_name(frist, middle, last):

    print(f"Hello {frist.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

full_name("Hussien","mohamed","yasser")    