#We have studied 3 packages in this to run our code
#A package is a namespace...
#that organizes a set of related classes and interfaces. ...
#1.platformIO   IDE Termianl:
#Goto: ctrl+shift+P.... then search platformio
#This opens the windows Windows PowerShell...
#This window is capable to rum the progams like command promt...

x=1
y=2
z=3
print(x,sep='*',end='\n\n\n')
print(y,sep='*',end='\n\n\n')
print(z,sep='*',end='\n\n\n')

p=input("Please give me a score on 10:")
print('Ahh',p,' is a good score, thanks...')

#2. Script:
#This is also used to run the py code
#The shortcut key is: ctrl+shift+b... It directly opens the terminal and shows the result
#The other way to open this is  Goto: ctrl+shift+P.... then search Script

#3. Python Debugger:
#This actually is used to set "breakpoints and single stepping at the source line level"...
#Then goto any line and right click at that line no. and select...
#Toggle python debugger or press alt+r


# Few basics of python...
# these are the "different things" that actually not common so, be cautious here...

# Simple loop using...
print("This is the 1st simple case...")
for i in range(5):
    print(i)

# We can even give starting and ending points in the loop...
print("This is the 2st simple case...")
for i in range(1,5):
    print(i)

# We can add steps to the "for loop"...
print("This is the 1st attempt using step...")
for i in range(1,5,2):           # While execution this takes the values with step 2
    print(i)

# By default, the end of the print statement have "New line"...
# that's why the above two lines gets printed in 2 diff lines...
print("I love programming...")
print("Because, I am taught by programmer that too love programming.")

# By using "end" we can combines these kind of lines...
print("I love programming...",end="")
print("Because, I am taught by programmer that too love programming.")
# This is generally usefull in the case where, matrices need to be printed using, nested condition.

#for x in  25:  # This is Type error...
#    print(x)

# to resolve this we need a list:
for x in [25]:
    print(x)
