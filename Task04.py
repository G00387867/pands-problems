# Program that asks the user to input any positive integer and
#  outputs the successive value of the following calculation.
# It should at each step calculate the next value by taking the current value
# if the it is even, divide it by two, if it is odd, multiply
# it by three and add one
# the program ends if the current value is one.


# first number and then check if it has a positive value

n = int(input("please enter a number: " ))
    
while n != 1:
    # eliminating 0 and negative numbers
    if n <= 0:
        print("Please enter a positive number.")
        break

    # for even numbers:
    elif n % 2== 0:
        n=int(n/2)
        print(n)

    # for other integers (odd numbers)
    else:
        n=int(n*3+1)
        print(n)
