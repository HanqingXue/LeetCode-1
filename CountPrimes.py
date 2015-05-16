"""
Help of: https://www.topcoder.com/community/data-science/data-science-tutorials/mathematics-for-topcoders/
http://rosettacode.org/wiki/Sieve_of_Eratosthenes#Python
Count the number of prime numbers less than a non-negative number, n
"""
import math
import itertools as it

def isPrime1(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        return True
"""
we only need to check divisibility for values of i less or equal to the square root of n (call this m).
If n divides a number that is greater than m then the result of that division will be some number less than m and thus n will also divide a number less or equal to m. 
Another optimization is to realize that there are no even primes greater than 2. Once we’ve checked that n is not even we can safely increment the value of i by 2. 
"""
def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = int(math.sqrt(n));
    for i in range(3, m+1, 2):
        if n%i==0:
            return False
    return True

#print(isPrime(5))

"""
Now we want to find all primes from 1 to 1000)00, 
we would have to call the above method 100000 times. 
This would be very inefficient since we would be repeating the same calculations over and over again. 
In this situation it is best to use a Sieve of Eratosthenes. 
Thhis will generate all the primes from 2 to n. 
It begins by assuming that all numbers are prime. 
then takes the first prime number and removes all of its multiples. It thenapplies the same method to the next prime number. This is continued until all numbers have been processed."""

"""Using set lookup"""
"""
Using set lookup
Uses a set to store the multiples. set are faster (usually O(log n)) than lists (O(n)) for checking if a given object is in. Using the set.update method avoids explicit iteration in the interpreter, making it even faster
""" 

def sieve(n):
    "Return all primes <= n."
    #np1 = n + 1
    s = [True] * n
    s[0] = s[1] = False
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): 
        if s[i]:
            print(s[i*i: n:i])
            print(s)
            s[i*i: n: i] =  [False] * len(range(i*i, n, i))
    return s.count(True)
#OMG I AM ESTATIC! I USING A BOOLEAN ARRAY IS HEAPS BETTER CUZ 1 BYTE(LIKE IN C)
print(sieve(10))
#print(list(sieve(50)))
