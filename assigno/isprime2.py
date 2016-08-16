
def prime(x):
	if x<2:
		return False
	if x == 2:
		return True
	if x%2 == 0:
		return False
	if not x & 1:
		return False

	for n in range(3, int(x**0.5)+1, 2):
		if x%n == 0:
			return False
	return True
print prime(95)


