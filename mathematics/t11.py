def power(x, n):

	# If x^0 return 1
	if (n == 0):
		return 1

	# If we need to find of 0^y
	if (x == 0):
		return 0

	# For all other cases
	return x * power(x, n - 1)


# Function to calculate x raised to the power y in O(logn)
def power(x,n):
	if (n==0):
		return 1
	temp = pow(x,n//2)
	if n%2==0:
		return temp* temp
	else:
		return x * temp *temp

    

# Driver Code
if __name__ == "__main__":
	x = 2
	n = 3

	# Function call
	print(power(x, n))
