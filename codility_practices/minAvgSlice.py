def getMean(l):
    return(sum(l)/len(l))

from collections import defaultdict

def solution(A):
    avgDict = defaultdict(int)
    for startPos in range(len(A)-1):
        if len(A) > 3 and startPos != len(A)-2:
            if A[startPos+2] <= A[startPos] and A[startPos+2] <= A[startPos+1]:
                avgDict[startPos] = getMean(A[startPos:startPos+3])
            else:
                avgDict[startPos] = getMean(A[startPos:startPos+2])
        else:
            avgDict[startPos] = getMean(A[startPos:startPos+2])
                        
    return(list(avgDict.values()).index(min(avgDict.values())))

if __name__ == '__main__':
    print(solution([10, 10, -1, 2, 4, -1, 2, -1]))
