def solution(X,Y,D):
    if (Y-X)%D == 0:
        step = (Y-X)//D
    else:
        step = (Y-X)//D + 1
    return step
