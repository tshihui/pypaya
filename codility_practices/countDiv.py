def solution(A, B, K):
    if B-A == 0 and A == 0:
        return(1)
    if B < K:
        return(0)
    if A % K == 0:
        addV = 1
    else:
        addV = 0
    return(((B//K)-(A//K)) + addV)

if __name__ == '__main__':
   print(solution(11, 345, 17))
