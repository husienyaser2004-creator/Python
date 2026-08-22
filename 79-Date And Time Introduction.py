#-------------------------------------
#--- Date and Time => Introduction----
#-------------------------------------

import datetime

print(dir(datetime))
print(dir(datetime.datetime))

# print The Current Date and Time 
print(datetime.datetime.now())

print("#" * 40)

# print The Current Year 
print(datetime.datetime.now().year)

# print The Current Month 
print(datetime.datetime.now().month)

# print The Current Day 
print(datetime.datetime.now().day)

print("#" * 40)

# print Start and End Of Date 
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#" * 40)

print(dir(datetime.datetime.now()))

# print The Current Time 
print(datetime.datetime.now().time())

print("#" * 40)

# print the Current Time Hour
print(datetime.datetime.now().time().hour)

# print the Current Time Minute
print(datetime.datetime.now().time().minute)

# print the Current Time Second
print(datetime.datetime.now().time().second)

print("#" * 40)

# print Start and End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#" * 40)

# print Specific Date 
print(datetime.datetime(2004, 10 , 21))
print(datetime.datetime(2004, 10 , 21, 4 , 55, 59))

print("#" * 40)

myBirthDay = datetime.datetime(2004, 10 , 21)
dateNow = datetime.datetime.now()

print(f"my Birthay is { myBirthDay} And" , end ="")
print(f"Date Now Is {dateNow}")

print(f"I Lived For {dateNow - myBirthDay}")
print(f"I Lived For {(dateNow - myBirthDay).days}Days.")


