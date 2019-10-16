from collections import defaultdict

def solution(X, A):
    lenA = len(A)
    if (lenA < X+1) and (lenA != 1 and X != 1 and A[0] != 1):
        return(-1)
    else:
        mapdic = defaultdict(int)
        for k in range(lenA):
            mapdic[A[k]] += 1
            if len(mapdic.keys()) == X:
                return(k)
            else:
                next
        return(-1)
