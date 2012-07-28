'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def isPrime(n):
	sqrt = int(n ** 0.5) + 1
	for i in range(2, sqrt):
		if n % i == 0: return False
	return True

def findPrime(count=6, n=13, goal=10001):
	while True:
		n += 1
		if isPrime(n): 
			count += 1
			if count < goal: return findPrime(count, n, goal)
			if count == goal: return n	
