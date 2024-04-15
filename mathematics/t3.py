'''Palindrome Number
'''
def Palindrome(N):
    old= N
    rev =0
    while(N>0):
        r = N%10
        rev = rev*10 + r
        N = N//10

    if old ==rev:
        return True
    else:
        return False
    


#Driver code
print(Palindrome(13431))