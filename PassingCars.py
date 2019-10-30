#######################
## Codility Lesson 5 ##
#######################

from collections import defaultdict

def solution(A):
    if (0 in A):
        firstZero = A.index(0)
        A = A[firstZero:]
        L = [0] * (len(A)+1)
        zeroPos = defaultdict(int)
        for a in range(len(A)):
            L[a+1] = L[a] + A[a]
            if A[a] == 0:
                zeroPos[a] = 1
    
        L.pop(0)
        sumAll = 0
        for zeroP in zeroPos.keys():
            sumAll += (L[len(A)-1] - L[zeroP])
            if sumAll > 1000000000:
                return(-1)
    
        return(sumAll)
    else:
        return(0)
