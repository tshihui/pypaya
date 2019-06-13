def lcm(num1, num2):
    if num1 >= num2:
        rangenum = num1
    else:
        rangenum = num2
    lcm = 1
    x = 2
    while (x <= rangenum):
        if num1%x == 0 and num2%x == 0:
            num1 = num1/x
            num2 = num2/x
            lcm = lcm*x
        if num1%x == 0 and num2%x != 0:
            num1 = num1/x
            lcm = lcm*x
        if num1%x != 0 and num2%x == 0:
            num2 = num2/x
            lcm = lcm*x
        if num1%x !=0  and num2%x != 0:
            x = x+1
        if num1 == 1 and num2 == 1:
            return lcm
        

x = 311
y = 124
print("LCM of " + str(x) + " and " + str(y) + " : " + str(lcm(x,y)))

