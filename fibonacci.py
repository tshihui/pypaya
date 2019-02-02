###############
## Fibonacci ##
## 2/2/2019  ##
###############
def fib(n):
    """ Fibonacci sequence """
    if n <= 0:
        return('Please input positive integer.')
    else:
        seq = []
        for k in range(n):
            if k <= 1:
                seq.append(k)
            else:
                seq.append(sum(seq[k-2:k]))
        print('The first ', n, ' numbers of the Fibonacci sequence is :', seq)

#######################
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please state n to compute fibonacci sequence.")
    else:
        n = int(sys.argv[1])
        fib(n)
