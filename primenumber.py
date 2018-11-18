import math

def prime(num):
    nonPrimeCount = 0
    for x in range(2, int(math.floor(math.sqrt(num)))):
        if num % x == 0:
            return False
    return True

x = 33
#print(str(x) +  "is" + ("prime" if prime(x) else "not prime"))
print("{} is {}".format(x, "prime" if prime(x) else "not prime")) 
