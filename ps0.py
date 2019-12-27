#Problem Statement:- Raising a number to a power and taking a logarithm

                 #Write a program that does the following in order:
                         #1. Asks the user to enter a number “x”
                         #2. Asks the user to enter a number “y”
                         #3. Prints out number “x”, raised to the power “y”.
                         #4. Prints out the log (base 2) of “x”.


import numpy as np                     #Package Importing

x = int(input("Enter number x"))       #Variable Declaraation and Take a input from User
y = int(input("Enter number y"))


print("x ** y = ", x ** y)             #Print Number "x" raised to the power "y"
print("log(x) = ", np.log2(x))         #Print the log(base 2) of "x"


#Test Cases :

            #Enter number x: 2
            #Enter number y: 3
            #X ** y = 8
            #log(x) = 1