# GCD or HCF of two numbers
def gcd(a,b):
    if b ==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
	return (a / gcd(a,b))* b

    
#Driver code
print(gcd(3,9))