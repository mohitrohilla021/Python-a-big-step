# You often need to import few things in the python
# Module:
#  A module is the "code file" that defines some functions that can  be used by other programs...
# There are functions which the people have already written and we just need to invoke them...

import random

# The use of "dot" notation, while involking any function...
# import school                     # Just an example
# value=school.student()            # so, we are calling "fn" named as "student" from "module" names as "school"...

prob=random.random()                # This returns a float number between 0 to 1...
print(prob)

diceThrow= random.randrange(1,7)    # randrange(1,n): It takes the values upto n, but does that include n...
print(diceThrow)

# Another way to import the module...
from random import randrange,random # This is also a way to import the Module

prob=random()                       # Now, directly we can invoke the functions without calling the "module"
print(prob)

diceThrow= randrange(1,7)
print(diceThrow)

# The "functions" are also called as "methods" and the "variables" are also called as "attributes"

import math
simple_value=math.sqrt(10)
print("The square root of 10 is:",simple_value)
