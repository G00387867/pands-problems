
# Adam Shaat
# A program that takes a positive floating point  number as input
# output is an approximation of its squareroot

import math
n = float(input("Please enter a positive number: "))

if n>=0:
    n = math.sqrt(n)
    print(n)
# handling exception with  negative numbers    
else:
    print("Please enter a positive number!")

# trying to code the Newton's method for square roots
# I have referred to the following website: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# then I complteted the suntax using the 
# first method as importing from library

n = float(input("Please enter a positive number: "))


def sqrt(n):

    r = n
    precision = 10 ** (-10)
    
    while abs(n - r * r) > precision:
        r = (r + n / r) / 2
        
    return r

if n>=0:
    print (sqrt(n))
    
# handling exception with  negative numbers    
else:
    print("Please enter a positive number!")

