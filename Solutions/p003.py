'''
The largest prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from math import floor

def isPrime(n):
	top_limit = int( floor(n ** 0.5) )
	for i in range(2,top_limit):
		if n % i == 0: return False
	return True

def findFactors(n=600851475143):
	sqrt = int( floor(n ** 0.5) )
	factors = [i for i in range(2,sqrt) if n % i == 0]
	for factor in reversed(factors):
		if isPrime(factor): return factor
		else: pass
	
