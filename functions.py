# Adam Shaat
# a function to sqaure numbers
import math

def power(x, y):
  ans = x
  y = y - 1
  while y > 0:
    ans = ans * x
    y = y - 1  
  return ans
  
def f(x):
  ans = (100 * power(x, 2) + 10 * power(x, 3)) // 100 
  ans = ans - (power(x, 3) // 10)
  return ans

def isprime(i):

  # loop through all values from 2 up to
  # but not including i.
  for j in range(2, math.floor(math.sqrt(i))):
    if i % j == 0:
      # if it does, i isn't a prime so exit
      # the loop and indicate it's not prime.  
      return False
  return True

