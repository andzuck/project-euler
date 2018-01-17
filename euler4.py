
# Project Euler Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.


# 100 * 100 is lower bound
# 999 * 999 is upper bound


def reverse(s):
    return s[::-1]

largest_palindrome = 0

for i in range(100, 1000):
	for j in range(100, 1000):
		n = i * j
		if str(n) == reverse(str(n)):
			largest_palindrome = n if n > largest_palindrome else largest_palindrome

print(largest_palindrome)

