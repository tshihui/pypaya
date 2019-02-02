###############
## Fibonacci ##
## 2/2/2019  ##
###############
def fib(n):
    """ Fibonacci sequence """
    if n <= 0:
        return('Please input positive integer.')
    else:
        i_1 = 0
        i = 1
        seq = [i_1,i]
        while len(seq) <= n:
             i_2 = i_1
             i_1 = i
             i = i_2 + i_1
             seq.append(i)
        print('Fibnoacci sequence with n =', n, 'is :', seq)

#######################
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please state n to compute fibonacci sequence.")
    else:
        n = int(sys.argv[1])
        fib(n)
