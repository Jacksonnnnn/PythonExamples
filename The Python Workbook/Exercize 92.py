num = int(raw_input("Enter a number to see if it is prime.  "))

def prime(a):
	if a % 2 == 0:
		print "%s is not a prime number." % a
		return False
	if a % 3 == 0:
		print "%s is not a prime number." % a
		return False
	if a % 4 == 0:
		print "%s is not a prime number." % a
		return False
	if a % 5 == 0:
		print "%s is not a prime number." % a
		return False
	if a % 6 == 0:
		print "%s is not a prime number." % a
		return False
	if a % 7 == 0:
		print "%s is not a prime number." % a
		return False
	if a % 8 == 0:
		print "%s is not a prime number." % a
		return False
	if a % 9 == 0:
		print "%s is not a prime number." % a
		return False
	if a % 10 == 0:
		print "%s is not a prime number." % a
		return False
	else:
		print "%s is a prime number." % a
		return True
prime(num)