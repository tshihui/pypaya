#-------------------
# Codility Lesson 4
# MissingInteger.py
#-------------------

def solution(A):
    mA = max(A)
    L = [0] * mA
    negNum = 0
    for a in A:
        if a > 0:
            L[a-1] = 1
        else:
            negNum += 1
    if sum(L) > 0:
        try:
            return(L.index(0) + 1)
        except:
            return(mA + 1)
    elif negNum == len(A):
        return(1)
