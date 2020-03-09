# Adam Shaat
# computing the primes.
from functions import isprime

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