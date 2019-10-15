##########################################
## Codility Lesson 4: Counting Elements
##########################################

def solution(A):
    Ad = {x:0 for x in range(1, len(A)+1)}
    
    for x in A:
        Ad[x] = 1
        
    if 0 in Ad.values():
        return(0)
    else:
        return(1)
