'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(n):
	stg = str(n)
	half = len(stg) / 2
	for i in range(half):
		otherside = (i * -1) - 1
		if stg[i] != stg[otherside]: return False
	return True

def findLargest(largest=10000):
	for i in range(100,1000):
		for j in range(100,1000):
			test = i * j
			if isPalindrome(test) and test > largest:
				largest = test
	return largest
	
# CURRENT PROBLEM:  only testing factors which are 1 apart
