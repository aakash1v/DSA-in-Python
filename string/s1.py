def issubseq(s1,s2):
    i,j=0,0
    while(i<len(s1) and j<len(s2)):
        if s1[i] == s2[j]:
            j = j+1
        i = i +1
    
    if j ==len(s2):
        return False
    else:
        return True
    
s1 = "ABCDEF"
s2 = "ADE"

print(issubseq(s1,s2))
