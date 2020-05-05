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
        print()

    print('A function creates a new symbol table for local variables\n'
          'When a function is executed, it first searches in the local symbol table\n'
          'before going to search in the global symbol table and finally the table\n'
          'of built-in names.')
    fib(10)

    def fib2(n):
        """Fib function that returns instead of print"""
        result = []
        a, b = 0,1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result

    print(fib2(10))

    print('\n1) Defining functions with default values for arguments')
    def ask_ok(prompt, retries=4, reminder='Please try again!'):
        while True:
            ok = input(prompt)
            if ok in ('y', 'yes', 'Y'):
                return True
            elif ok in ('n', 'no', 'N'):
                return False
            else:
                retries = retries - 1
                if retries < 0:
                    raise valueError('invalid user response')
                print(reminder)

    print('\nNote that if default values were a prespecified value, this value will be used')
    x = 4
    def printNo(no = x):
        return(no)
    print('x = 4 prior to defining function. printNo() returns:', printNo())
    x = 5
    print('x set to 5, now printNo() returns:', printNo())

    print('\n2) Keyword Arguments- kwarg = value')
    print("in def parrot(voltage, state='a diff', action='voomo', type='blue') :\n")
    print('voltage is a required argument, while the rest are optional')

    def parrot(voltage, state='a diff', action='voomo', type='blue'):
        print('-- this parrot wouldnt', action, end=' ')
        print('if you put', voltage, 'volts through it.')
        print('--- lovely! the', type)
        print('--- it is', state, '!')

    print(parrot(19), '<-- executing parrot(19)')

    def cheeseshop(kind, *arguments, **keywords):
        print('Do you have any', kind, '?')
        print('We are out of', kind, '.')
        # anything after positional argument for 'kind' that has no keywords
        # will be parsed to the following:
        for arg in arguments:
            print(arg)
        print('-' * 30)
        # only if keywords are present, the following will be executed
        for kw in keywords:
            print(kw, ':', keywords[kw])

    cheeseshop('mozerella', 'this is crazy', 'how can that be')
    cheeseshop('mozerella', 'this is crazy', 'how can that be',
               shop = 'cheeseshop', shopkeeper = 'lion')

    print('\nFormat of functions:\n'
          'f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2')
    print('pos: positional args')
    print('kwd: keyword args')
    print('/ : whatever before is positional ONLY')
    print('* : whatever before is keyword ONLY')
    print('without / or *, it can be positional or keyword')

    def weightliftRecords(squat, deadlift, *args):
        print('Squatted', squat, sep=':')
        print('Deadlifted', deadlift, sep=':')
        for a in args:
            print(a)

    weightliftRecords(30, 40, 'bench = 30')
    # weightliftRecords(squat=30, deadlift=40, 'bench = 30') won't work
    # as 'bench=30' becomes positional
    print('POSITIONAL ARG HAS TO GO FIRST.')
    # weightliftRecords(squat=30, deadlift=40) this is fine.

    print('--- Function with keyword args only:')
    print('------ def menu(*, kwargs)')
    def menu(*, kwargs):
        """this function only takes keyword arguments"""
        for food in kwargs:
            print(food, 'costs', kwargs[food])
    print("menu(kwargs={'ham': 40, 'eggs': 20, 'tea':10}):")
    menu(kwargs={'ham': 40, 'eggs': 20, 'tea':10})

    print('\n-- Another way of defining keyword args: **kwargs')
    print('------ def menu2(**kwargs)')
    def menu2(**kwargs):
        """this function only takes keyword arguments"""
        for food in kwargs:
            print(food, 'costs', kwargs[food])
    print("menu2(**{'ham': 40, 'eggs': 20, 'tea': 10})")
    menu2(**{'ham': 40, 'eggs': 20, 'tea': 10})

    def unpackingArgs(name, friend):
        """this function only takes keyword arguments"""
        print('this is', name, 'nice to meet', friend, '.')
    unpackingArgs('sh', 'nish')
    unpackingArgs('sh', friend='nish')
    unpackingArgs(name='sh', friend='nish')
    unpackingArgs(**{'name':'sh', 'friend':'nish'})

    print("menu2(**{'ham': 40, 'eggs': 20, 'tea': 10})")
    menu2(**{'ham': 40, 'eggs': 20, 'tea': 10})

    print('\n-- Arbituary number arguments: *args') # Least used. "Variadic arguments."
    print('Scoops up whatever is in the arguments that were not taken as positional/keywords')
    print('------ def menu3(*args)')
    def menu3(*args):
        """this function only takes keyword arguments"""
        for food,cost in args:
            print(food, 'costs', cost)
    print("menu3(('ham', 40), ('tea', 20))")
    menu3(('ham', 40), ('tea', 20))

    def concatSent(*args):
        print('_'.join(args))
    concatSent('oh', 'this', 'is', 'nonsense')


    print('\nSmart way of using /')
    def check(name, **kwds):
        """We want function to return True if name is in kwds dict"""
        return 'name' in kwds #This will not work though
    print('Defining function this way:')
    print('--- def check(name, **kwds):')
    print("will not work: check('oh', **{'oh':3})")
    print(' '*10, check('oh', **{'oh':3}))

    def check2(name, /, **kwargs):
        return name in kwargs

    print('Defining function this way:')
    print('--- def check2(name, /, **kwargs):')
    print("will not work: check('oh', **{'oh':3})")
    print(' '*10, check2('oh', **{'oh': 3}))
    print('Works as function understood that the first arg is positional, whatever after is keyword')

    print('\nLambda Expressions')
    print('!!! lambda arguments: function')
    def make_increment(n):
        return lambda x: n+x

    mk10 = make_increment(10)
    print('mk10(4):', mk10(4))
    print('make_increment(10)(5):', make_increment(10)(5))

    add1 = lambda x: x + 1
    print('\nadd1 = lambda x: x+1')
    print('add1(20)', add1(20))

    pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
    pairs.sort(key=lambda pair: pair[1]) # sorting by 2nd element in each tuple
    print(pairs)

    def make_increment2(n, n2):
        """Testing lambda within function"""
        sumN = lambda x: n+x
        return sumN(n2)**2

    print(make_increment2(10, 15))

    print('\nDocument string')
    print('Doc string of a function can be obtained via: function.__doc__')
    print('Doc string of make_increment2:', make_increment2.__doc__)