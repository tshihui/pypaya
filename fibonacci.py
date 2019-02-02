###############
## Fibonacci ##
## 2/2/2019  ##
###############
def fib(n):
    """ Fibonacci sequence """
    if n == 1 :
        return([0])
        print('The first ', n, ' numbers of the Fibonacci sequence is : [0]')
    elif n == 2:
        return([0,1])
        print('The first ', n, ' numbers of the Fibonacci sequence is : [0, 1]')
    elif n > 2:
        seq = [0,1] 
        for k in range(n-2):
            seq.append(sum(seq[k:k+2]))
        print('The first ', n, ' numbers of the Fibonacci sequence is :', seq)
        return(seq)

#######################
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please state n to compute fibonacci sequence.")
    else:
        n = int(sys.argv[1])
        fib(n)
