'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def isPythagoreanTriplet(a, b, c):
	if a**2 + b**2 == c**2:	return True
	else: return False

def testLegs(a=None, b=None, c=None):
	if not a and not b:
		a = c - 1
		b = 1000 - a - c
	if isPythagoreanTriplet(a, b, c): return True, a, b
	elif b >= a: return False, None, None
	else: return testLegs(a=a-1, b=b+1, c=c)

def testHypotenuse(c=334):
	isTriple, a, b = testLegs(c=c)
	if isTriple: return a * b * c
	else: return testHypotenuse(c=c+1)
