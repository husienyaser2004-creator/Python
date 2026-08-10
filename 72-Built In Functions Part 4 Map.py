#-------------------------------------
#--Built In Functions => Map ---------
#-------------------------------------
# [1] Map Take A Finction + Iterator 
# [2] Map Called Map Because It Map the Function On Every Element
# [3] The Function Can Be Pre Defined Function Or Lambda Function
#---------------------------------------------------------------------

# Use Map With Pre predefined Function

from email.mime import text


def formatText(text):
    return f"-{text.strip().capitalize()} -"

myText = ["  hussien " , "mohamed" , " ali "]

#myformatText = map(formatText , myText)
#print(myformatText)

#for name in list(map(formatText , myText)):

#    print(name)


print("#" * 50)


# Use Map With Lambda Function

# def formatText(text):
#    return f"-{text.strip().capitalize()} -"

myText = ["  hussien " , "mohamed" , " ali "]

for name in list(map(lambda text: f"-{text.strip().capitalize()} -", myText)):


    print(name)
