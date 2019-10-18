#####################################
## Codility Lesson 4: MaxCounters.py
#####################################

#--- Attempt 1: ---#
def solution(N, A):
    L = [0] * N
    for k in A:
        print(k)
        if k != N+1:
            L[k-1] +=1
        else:
            L = [max(L)] * N
        print(L)
    return(L)

