def solution(A):
    Td = {}
    for x in A:
        try:
            Td[x] += 1
        except:
            Td[x] = 1
    for k in Td.keys():
        if Td[k] % 2 == 1:
            return k
        else:
            pass

