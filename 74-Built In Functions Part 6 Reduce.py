#---------------------------------------
#--built-in functions part 6 reduce-----
#---------------------------------------
# [1] Reduce Take A Function + Iterable
# [2] Reduce Run A Function On Frist And Second Element And Give Result 
# [3] Then Run The Function On Result And Third Element 
# [4] Then Run Function On Resuit And Fourth Element And So On 
# [5] Till One Element Left and This is The Result Of  The Reduce 
# [6] The Function Can Be Pre-Defined Function Or Lambda Function
#-------------------------------------------------------------------------

from functools import reduce
import numbers


def sumAll(num1, num2): 

    return num1 + num2

number = [1, 8, 2, 9, 100]

result = reduce(lambda num1, num2: num1 + num2, number)

#result = reduce(sumAll, numbers)

print(result)

# ((1 + 8) + 2) + 9) + 100 = 120