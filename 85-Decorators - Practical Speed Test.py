#---------------------------------------------
#---Decorators - Practical Speed Test---------
#---------------------------------------------

from time import time 

def myDecorator(func): # Decorator

    #def myDecoratorTwo(func): # Decorator

        def nestedFunc(*numbers): # Any Name Its Just For Decoration 

            for number in numbers:


                if number < 0:

                #if numbers[0] < 0 or numbers[0] < 0:

                    print("Beware One Of The Number Is Less Than Zero")

            print("Coming From Decorator Two")

        #print("Before") # Message From Decorator 

            func(*numbers) # Execute Function 

        return nestedFunc # Return All Data 

@myDecorator
#@myDecoratorTwo
def calculate(n1,n2,n3):

    print(n1+n2+n3)

calculate(-5, 90, 150)



def SpeedTest(func):

    def wrapper():

        start = time()

        func()

        end = time()

        print(f"Function Running Time Is: {end - start}")

    return wrapper


@SpeedTest
def bigloop():

    for number in range (1, 20000) :

        print(number) 

bigloop()        





