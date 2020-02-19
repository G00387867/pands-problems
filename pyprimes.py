# Adam Shaat
# computing the primes.

# My list of primes - TBD
p=[]

# loop through all the numbers we're 
# checking for primality.

for i in range(2, 100):
    # Assume i is a prime
    isprime = True
    # loop through all values from 2 up to
    # but not including i.
    for j in range(2, i):
      if i % j == 0:
        # if it does, i isn't a prime so exit
        # the loop and indicate it's not prime.  
        isprime = False
        break
    # if i is prime, then append to P. 
    if isprime:
     p.append(i)

print(p)