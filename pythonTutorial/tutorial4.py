if __name__ == '__main__':
    print('--- If statements:')
    x = 14
    if x < 10:
        print('Less than 10')
    elif x < 20:
        print('Less than 20 greater than 10')
    else:
        print('Larger than 20')

    print('\n--- For statements:')
    menu = {'ham': 14, 'sausages': 20, 'tea': 15}
    for item, price in menu.items():
        print(f'{item:10} costs {price:4d}')

    print('\n--- Range function:')
    print('range(3, 10) values 3-9')
    for i in range(3, 10):
        print(i)
    print('Sum of a range can be easily obtained sum(range(val))', sum(range(3,10)))
    print('Converting range into list: list(range(val))', list(range(3,6)))

    print('\n--- Break, continue, else:')
    for n in range(20):
        if n % 2 == 0:
            print('Even')
            continue # This will return loop to the top and not execute the remaining
        print(f'The odd number is {n:3d}.')

    for n in range(20):
        if n % 2 == 0 and n > 13:
            print(f'{n} is even and greater than 13')
            break # This will exit loop once we entered this if clause
        print(f'Current number is {n}')

    for n in range(2, 20):
        for x in range(2, n):
            if n % x == 0:
                break # This breaks out of the second for loop
        else: # this else corresponds to the 2nd for loop
            print(f'{n} is a prime number')

    print('\n--- Pass statements:')
    print('Essentially does nothing.')
    def newFunction(*args):
        pass
    print('pass can be placed in functions that are incomplete', newFunction(29))

    print('--- Defining functions')
    def fib(n):
        """Print a fibbonaci series up to n"""
        a, b = 0, 1
        while a < n:
            print(a, end= ' ')
            a, b = b, a+b
        # print()

    print('A function creates a new symbol table for local variables\n'
          'When a function is executed, it first searches in the local symbol table\n'
          'before going to search in the global symbol table and finally the table\n'
          'of built-in names.')
    fib(10)




