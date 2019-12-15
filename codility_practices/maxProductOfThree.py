#######################
## Codility Lesson 6 ##
#######################

def solution(A):
    sortA = sorted(A)
    pdt1 = sortA[0] * sortA[1] * sortA[-1]
    pdt2 = sortA[-1] * sortA[-2] * sortA[-3]
    if pdt1 > pdt2:
        return(pdt1)
    else:
        return(pdt2)



if __name__ == '__main__':
    print('Test for [-5,5,-5,4]')
    print(solution([-5,5,-5,4]))
