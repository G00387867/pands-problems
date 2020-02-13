# Adam Shaat
# Check if a number is prime
# The primes are 2, 3, 5, 7, 11, 13, ..

p = 347
m = 2
isprime = True

while m < p:
  if p % m == 0:
    isprime = False
    break
  m = m + 1

if isprime:
  print(p, "is a prime number.")
else:
  print(p, "is not prime.")


p = 347
isprime = True

for m in range(2, p):
  if p % m == 0:
    isprime = False
    break

if isprime:
  print(p, "is a prime number.")
else:
  print(p, "is not prime.")


