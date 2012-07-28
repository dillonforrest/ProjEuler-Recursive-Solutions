'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# Primes below 20: 2, 3, 5, 7, 11, 13, 17, 19.  Product = 9699690

def findSmallest(n=9699690):
	for i in range(1,21):
		if n % i != 0: return findSmallest(n + 9699690)
		else: pass
	return n
