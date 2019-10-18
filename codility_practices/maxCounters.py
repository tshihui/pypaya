#####################################
## Codility Lesson 4: MaxCounters.py
#####################################

#--- Attempt 2 ---#
from collections import defaultdict

def solution(N, A):
    L = defaultdict(int)
    maxV = 0
    for k in A:
        if k != N+1:
            L[k] += 1
        else:
            if (len(L.values()) > 0):
                maxV = max(L.values())
            L = defaultdict(lambda : maxV)

    output = []
    for x in range(1, N+1):
        output.append(L[x])
    
    return(output)


#--- Attempt 1 ---#
def solutionOld(N, A):
    L = [0] * N
    for k in A:
        print(k)
        if k != N+1:
            L[k-1] +=1
        else:
            L = [max(L)] * N
        print(L)
    return(L)

