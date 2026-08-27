#------------------------------------------
#----Decorators - Function With Parameters-
#------------------------------------------

def myDecorator(func): # Decorator

    #def myDecoratorTwo(func): # Decorator

        def nestedFunc(num1, num2): # Any Name Its Just For Decoration 

            if num1 < 0 or num2 < 0:

                print("Beware One Of The Number Is Less Than Zero")

            print("Coming From Decorator Two")

        #print("Before") # Message From Decorator 

            func(num1, num2) # Execute Function 

        return nestedFunc # Return All Data 

@myDecorator
#@myDecoratorTwo
def calculate(n1,n2):

    print(n1+n2)

calculate(-5, 90)

