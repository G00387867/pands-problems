# Adam Shaat
# computing the primes.
import math

def isprime(i):

  # loop through all values from 2 up to
  # but not including i.
  for j in range(2, math.floor(math.sqrt(i))):
    if i % j == 0:
      # if it does, i isn't a prime so exit
      # the loop and indicate it's not prime.  
      return False
  return True

# My list of primes - TBD
p=[]

# loop through all the numbers we're 
# checking for primality.


for i in range(2, 100000):

    # if i is prime, then append to P. 
    if isprime(i):
     p.append(i)
     
# print out our list
print(p)