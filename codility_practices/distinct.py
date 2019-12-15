#######################
## Codility Lesson 6 ##
####################### 


from collections import defaultdict

def solution(A):
    """ Return number of distinct values in the array """
    if len(A) == 0:
        return(0)

    uniDict = defaultdict(int)

    for i in A:
        uniDict[i] =+ 1

    return(len(uniDict.keys()))



if __name__ == '__main__':
    print('Test with empty list')
    print(solution([]))
    print('Test with [4,5,6,1,1,1,1,5,3]')
    print(solution([4,5,6,1,1,1,1,5,3]))

