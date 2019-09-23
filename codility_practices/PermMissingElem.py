def solution(A):
    diffEle = set(range(1, len(A)+2)) - set(A)
    return list(diffEle)[0]
