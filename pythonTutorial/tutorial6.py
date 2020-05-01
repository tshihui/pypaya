if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        sys.exit('Please enter True or False')
    if sys.argv[1]:

        import func6

        print('function from func6 imported')
        print('function to find odd numbers:', func6.findOdd(10))

        print('assign function to a new object name, oddy')
        oddy = func6.findOdd
        print('calling oddy', oddy(3))
        print('module.__name__ ', func6.__name__)

        varInFunc6 = 'oh'
        print('Set varInFunc6 = "oh"', varInFunc6)
        from func6 import varInFunc6
        print('Variable directly imported from func6 becomes the global var here', varInFunc6)
        print('varInFunc6 becomes', varInFunc6)

        from func6 import findOdd as oddy
        print('import findOdd function directly as oddy')
        print('call oddy directly', oddy(489))

        print('If module is updated, we can restart interpreter or use "importlib.reload()"')
        print('first, import importlib')
        import importlib
        print('Reload func6', importlib.reload(func6))
        
        import func6
        if len(sys.argv) >= 3:
            print(func6.findOdd(int(sys.argv[2])))

        print('sys.path contains the list of strings which are the search paths for modules')
        print(sys.path)
        print('you can add on additional search paths by using sys.path.append("loc")')

        print('using dir() to find out names in modules')
        print(dir(func6))
        import builtins
        print("dir(builtins) returns all the builtin functions and variables")
        print(dir(builtins))

        print('Creating packages')
        print('Every level of folder has to contain __init__.py')
        print('submodules can be loaded such as import func6sub.func6sub')
        import func6sub.func6sub
        if len(sys.argv) > 3:
            print(func6sub.func6sub.findEven(int(sys.argv[3])))
        print('We can also use from xx.xx import func')
        from func6sub.func6sub import findEven
        print('and call function directly')
        if len(sys.argv) > 3:
            findEven(int(sys.argv[3]))
