#---------------------
#--Escape Sequences Character-----
#\b => Back Space
#\newline => Escape new line + \
#\\ => Escape Back Slash
# \' =>  Escape Single Quotes
# \" =>  Escape Double Quotes
# \n => Line Feed 
# \r => Carriage Return
# \t => Horizontal
# \ xhh => Character Hex Value 


# Back Space
print("hello\bworld")  #will Remove o


# Escape New line + \ Back Slash
print("hello \
I love \
phthon")

# Escape Back Slash
print("I love  back Slash \\")

# Escape single Quote
print('I love Single Quto\'Test\' ')

#Escape Double Quotes
print("'I love Single Quto\"Test\" ")

# line feed
print(" Hello World\nSecond Line")

# \r => Carriage Return
print("123456\rAbcd")

 # \t => Horizontal
print("Hello\tpython")

# Character Hex Value
print("\x4f\x73")