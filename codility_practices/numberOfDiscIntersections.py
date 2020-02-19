from collections import defaultdict 

def solution(A):
    if len(A) <= 1 or sum(A) == 0:
        return(0)
    
    totalPossibleInter = (len(A) * (len(A) - 1)) / 2
    Alower = []
    Aupper = []
    for i in range(len(A)):
        Alower.append((A[i] - i) * -1)
        Aupper.append(i + A[i])
        
    AlowerSort = sorted(Alower)
    AupperSort = sorted(Aupper)
    AlowerSortRev = AlowerSort[::-1]
    
    if AlowerSort[-1] < AupperSort[0]:
        return(int(totalPossibleInter))
    
    upperDict = defaultdict(int)
    for i in sorted(AlowerSort + AupperSort):
        upperDict[i] = 0
    for i in range(len(A)):
        upperDict[AupperSort[i]] += 1
    for i in range(len(upperDict)):
        upperDict[i] = upperDict[i] + upperDict[i-1]
    
    sumCount = 0
    for k in range(len(A)):
        sumCount += upperDict[AlowerSortRev[k]-1]

    numInter = totalPossibleInter - sumCount
    if numInter > 10000000:
        return(int(-1))
    else:
        return(int(numInter))
