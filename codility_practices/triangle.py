#######################
## Codility Lesson 6 ##
#######################

def checkTrio(Atrio):
    """ To check if 3 numbers satisfy triangle property """
    if (Atrio[0] + Atrio[1] > Atrio[2] and Atrio[0] + Atrio[2] > Atrio[1] and Atrio[1] + Atrio[2] > Atrio[0]):
        return(True)
    else:
        return(False)


def solution(A):
    """ Return 1 if 3 integers can form a triangle """
    Asort = sorted(A)[::-1]

    for i in range(len(A)-2):
        if checkTrio(Asort[i:i+3]):
            return(1)

    return(0)


if __name__ == '__main__':
    print('Test for [100, 40, 25, 1, 5, 14, 50]')
    print(solution([100, 40, 25, 1, 5, 14, 50]))


