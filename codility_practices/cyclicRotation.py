def solution(A, K):
    if len(A) == 0:
        return []
    else:
        if (abs(K) > len(A)):
            if K > 0:
                K = K - (K//len(A) * len(A))
            else :
                K = - (abs(K) - (abs(K)//len(A) * len(A)))
        poslist = [x for x in range(len(A))]
        newposlist = [x+K for x in range(len(A))]

        # Update positions
        for x in range(len(newposlist)):
            if newposlist[x] == len(A):
                newposlist[x] = 0
            elif newposlist[x] > len(A):
                newposlist[x] = newposlist[x] - len(A)

        # Reposition
        newList = [0] * len(A)
        for x,y in zip(A, newposlist):
            poslist[y] = x

        return poslist
