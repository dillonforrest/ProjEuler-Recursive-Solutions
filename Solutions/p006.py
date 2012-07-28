'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
def findSumOfSquares(n=1, max=100):
	if n < max: return n ** 2 + findSumOfSquares(n+1, max)
	else: return n ** 2

def findSquareOfSum(n=1, sum_=0, max=100):
	print n
	if n < max:	return findSquareOfSum(n+1, sum_+n, max)
	else:	return (sum_ + n) ** 2

def findDiff():
	sumofsqs = findSumOfSquares(max=100)
	sqofsum  = findSquareOfSum(max=100)
	return sumofsqs - sqofsum
