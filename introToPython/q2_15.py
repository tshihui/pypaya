# 2.15
num1 = float(input('Please input first number: '))
num2 = float(input('Please input second number: '))
num3 = float(input('Please input third number: '))

min = num1
min2 = num2
min3 = num3

if (min < min2) & (min2 > min3):
    min2 = num3
    min3 = num2

if (min > min2) & (min > min3):
    min3 = min
    if (min2 < min3):
        min = min2
        min2 = num3
    else:
        min = min3

if (min > min2) & (min < min3):
    min = min2
    min2 = num1

print(min, min2, min3)

