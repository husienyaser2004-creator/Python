#----------------------------------------------
#--Modules Part 1 - Intro And Built In Modules
#----------------------------------------------
# [1] Module is A File Contain A Sat Of Functions
# [2] You Can Import Module In Your App To Help You
# [3] YOu Can Import Multiple Modules
# [4] You Can Create YOur Own Modules
# [5] MOdules Saves Your Time
#----------------------------------------------

# Import Main Moudule
# Impoet random
# print(randow)
#print(f"print Random Float Number {random.random}")


# Show All Function Inside Module
# import random
# print(dir(random))

# Import One Or Two Functions From Module
from random import randint,random
print(f"print Random Float {random()}")
print(f"print Random Integer {randint(100,900)}")
