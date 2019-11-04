#######################
## Codility Lesson 5 ##
#######################

def findIF(subSeq):
    """ Return impact factor in subsequence """
    if 'A' in subSeq:
        return(1)
    elif 'C' in subSeq:
        return(2)
    elif 'G' in subSeq:
        return(3)
    else:
        return(4)
    
def solution(S, P, Q):
    """ Identify impact factor per query in P & Q """
    M = [0] * len(P)
    for m in range(len(P)):
        subS = S[P[m]:Q[m]+1]
        M[m] = findIF(subS)
    return(M)
