def solution(A):
    for x in range(1, len(A)):
        A[x] += A[x-1]
    return min([abs((2*y) - A[len(A)-1]) for y in A[:len(A)-1]])
