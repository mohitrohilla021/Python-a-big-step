# some additional information about python

# Truncated division "//"

# a // b = The integer part of the integer division of a by b

# Sometimes we need an interger output itself
print(55/2)         # float is the result
print(55//2)        # the result remains int only

# If any one digit is float type then the result will be float type only
print(55.0//2)      # the result is float but still Truncated...its 27,0 not 27.5

# Exponentiation symbol: " ** "
print(2**10)

# Precedence of characters in python language:
# 1.) Paranthesis " () "
# 2.) Exponential " ** "
# 3.) Multiplication and division " * / // % "
# 4.) Addition and subtraction  " + - "

# square(), sub() these are inbuild functions of python

# print(square)... gives output: <function square>... when there is no argu...

# Various ways to print a string:
# 1st way:
print("Its is string...")
# 2nd way:
print("""Its is string...""")
# 3rd way:
print('Its is string...')
# 4th way:
print('''Its is string...''')

# "Why" is these formats given...
# The most important use of the these "quotation" is when...
# when we have any kind of quatations in the statement then to avois any error, we use these...

# print("When "name" is in inverted commas")  #This causes an error
# correct statement:
print("""When "name" is in inverted commas""")

# print('When 'name' is in inverted commas')  #This causes an error
# correct statement:
print('''When 'name' is in inverted commas''')

max_marks=100
# print("The maximum marks are " + max_marks)   # Type error
print("The maximum marks are " +str(max_marks)) # String can be added to a string

# 2x=100            # 2x is not allowed here... x2 can be used
# print(2x)

x2=100
print("Maximum marks:",x2)

# After studying the expressions there is one more important term called "statements" in python
# Statement is the complete instruction that a py prog. executes...
# x=1+2-5  This is an assignment statement
# "1+2-5" is the expression
# Expressions are various types:
# 1.) Literal Expressions
#       Like, x=500, stores value 500 itself, same value or y=3.14, etc
# 2.) Complex Expressions
#       Like,, x=200+10, stores a diff value i.e. 210

# To count the number of alplabets present in any expression we have"len" fn

print(len("Hello world"))       # Total char are 11 in this

# python has simple functions for Addition and subtraction
# add(3,5)
# sub(5,3)

# x+=3 is same as x=x+3   please note this is important

# Hard coding?
# Its writing the "answer" without actually going through the computation of the answer.
x1=10
x2=20
avg=15.0
print("The average value is:",avg)   # Its actually direct writing, no computation here...
# We should never hard code our answers, thats important to make the code more and more better...

sum=10.0
# print("The value of sum is:"+sum)   # This is a type error...
print("The value of sum is:"+str(sum))
