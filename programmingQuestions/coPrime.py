# Are 2 numbers co-prime?

def findFactors(number):
    factors = []    
    for fact in range(2,10):
        if (number % fact == 0):
           factors.append(fact)
           number = number / fact
    return(factors) 

def coPrime(a, b):
    