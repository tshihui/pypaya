if __name__ == '__main__':
    # global namespace is present
    print('Classes')
    print('\nPython scopes & namespaces')
    print('References to names in a module are attribute references\n'
          'modname.funcname')
    print('Module attributes maybe read-only or writable')
    print('In writable cases: modname.attriname = 40 can be done')
    print('Deletion can be performed by del module.attriname')
    print('In a function, local namespace is created, and forgotten once\n'
          'function returns or raises an exception that was not handled.')

    print('Scope: textual region of a python program, where namespace is directly accessible.')
    print('i.e. a reference to a name attempting to find the name in the namespace')
    print("At every execution, at least 3 nested scopes' namespaces are directly accessible")
    print('    innerscope: searched first, containing local names')
    print('    scopes of any enclosing functions: searched from the nearest -> non-local/non-global')
    print("    next-to-last scope: current module's global names")
    print('    outermost scope: searched last, namespace with builtin names')

    print('Scopes & Namespaces EG:')
    def scope_test():
        def do_local():
            # if print(spam) is done here,
            # spam defined in scope_test will be printed
            spam = 'local spam'
            # this only assigns spam locally
            # when spam is referenced outside this function,
            # spam value here will not be reflected

        def do_nonlocal():
            # declaration needs to be done before assignment within function
            # reference to spam cannot be done prior to nonlocal spam statement
            # spam defined in scope_test here is only in the local namespace of scope_test
            nonlocal spam
            # nonlocal indicates that spam lives in an enclosing scope
            spam = 'nonlocal spam'
            # modifies spam in scope_test

        def do_global():
            # global indicates that spam lives in global scope
            global spam
            spam = 'global spam'
            # this is going to modify spam in the global namespace

        # do_local()
        # print(spam)
        # If we try print(spam) here, we will get an error.
        # do_local wouldn't have returned spam.
        # hence spam is not in scope_test & also not in global namespace
        # Similarly, if we set spam the following way:
        spam = 'test spam'
        do_local()
        # and execute do_local()
        print('after local assignment:', spam)
        # expects: test spam
        # do not show spam as the value define in do_local()

        # in do_nonlocal()
        # spam value will be updated with the value in do_nonlocal()
        # as spam is declared nonlocal
        do_nonlocal()
        print('after nonlocal assignment:', spam)
        # expects: nonlocal spam
        do_global()
        print('after global assignment:', spam)
        # expect: nonlocal spam as it would have identified spam within here
        # out of this function, we will expect spam = 'global spam'
        # if do_nonlocal was not run before do_global,
        # we would expect: test spam

    scope_test()
    print('In the global scope:', spam)

    print('\nClasses')
    print('1. Class Definition Syntax')
    print('class ClassName:\n'
          '...')
    print('new namespace for the local scope is created when class definition is entered')

    print('\n2. Class Objects')
    print('an example:\n'
          'class MyClass:\n'
          '    """ A simple eg class"""\n'
          '    i = 12345\n'
          '\n'
          '    def f(self):\n'
          '        return "hello world"')
    class MyClass:
        """ A simple class"""
        i = 12345

        def f(self):
            return 'hello world!'

    print('\nMyClass.i will return :', MyClass.i)
    MyClass.i = 341
    print('MyClass.i value can be changed by assigment:', MyClass.i)
    print('MyClass.f(xxx) will return :', MyClass.f(1245))
    print('MyClass.__doc__ will return: ', MyClass.__doc__)
    print('MyClass.i and MyClass.f are attribute references')

    print('Class instantiation: x = MyClass()')
    print('creates an empty object. This can be changed by defining initial state\n'
          'method in the class. For eg:\n'
          'def __init__(self):\n'
          '    self.data = []\n'
          '--- or ---\n'
          'def __init__(self, x):\n'
          '    self.oh = x + 10')
    class MyClass:
        """ A simple class"""
        i = 12345

        def __init__(self, x):
            self.oh = x + 10

        def f(self):
            return 'hello world!'

        def pit(self):
            return self.oh ** 2

    x = MyClass(100) # x is an instance
    print('Assigning x = MyClass(100), x.oh will return:', x.oh)
    print('If a function such as:\n'
          '    def pit(self):\n'
          '        return self.oh ** 2\n'
          'is defined in the class, then\n'
          'x.pit() will return,', x.pit())

    print('\n! An instance = an object. Creating an instance = instantiation.')
    print('\nClass is like a blueprint.')
    print('An object created from this blueprint is a class instance.\n'
          'Member variables specific to this object = instance variables\n'
          '(compared to class variables shared across the class.')
    print('\n3. Instance Objects')
    print('Instance objects only understand attribute references: instanceName.funcName')
    print('There are 2 types of attribute names: 1) data attributes, 2) methods')
    print('MyClass.f is a function object while\n'
          'x.f (where x = MyClass()), is a method object.')

    print('\n4. Method Objects')
    print('instanceName = ClassName()')
    print('methodObj = instanceName.func !! note: without ()')
    print('methodObj can be executed by calling methodObj() ')
    print('methodObj() can be called without passing any arguments because\n'
          'it is actually executing ClassName.method(instanceObj) ')
    x = MyClass(10)
    xp = x.pit
    print('For eg:\n'
          'x = MyClass(10)\n'
          'xp = x.pit\n'
          'xp() = x.pit() =', xp(), '\n is the same as\n'
                        'MyClass.pit(x)\n', MyClass.pit(x),
                        '')
    print('All the things within a class are the attributes (data or methods)')
    print('when an attribute is referenced, the class of the instance is searched.\n'
          'if a function object is identified, a method object is created by\n'
          'packing the instance object and the function object together.\n'
          'when a method object is called with an argument list,\n'
          'a new argument list is created from the instance object + the argument list\n'
          'and passed into the function object.')
    print('In other words....\n'
          '1) create instance object from a class [insObj = MyClass()]\n'
          '2a) with instance object, reference data attributes [insObj.counter]\n'
          '2b) with instance object, reference non data attribute (function) [methObj = insObj.func] \n'
          '3) when the attribute referenced is identified as a function,\n'
          'the instance object and function are packed together and regarded as an method object.\n'
          'when a list of arguments are given to the method object,[methObj(args)] \n'
          'a new list of arguments is created from instance object + given arg list [insObj, args] \n'
          'and given to the in the function object in this method. [MyClass.func(insObj, args)]')
    print("For eg:\n"
          "    class MyClass:\n"
          "        def __init__(self, ah):\n"
          "            self.oh = ah+10\n"
          "        def pit(self):\n"
          "            return self.oh ** 2\n"
          "        def pit2(self, x):\n"
          "           return self.oh + x ** 2")

    class MyClass:
        def __init__(self, ah):
            self.oh = ah + 10
        def pit(self):
            return self.oh ** 2

        def pit2(self, x):
            return self.oh + x ** 2

    x = MyClass(10) # ah = 10. oh is evaluated as 20
    print('x = MyClass(10)')
    xp2 = x.pit2 # instance object and function object packed together as method object
    print('xp2 = x.pit2')
    # self.oh = 20 unique to instanceObject x, and x = 5 (the new arg value) returns 45.
    print('xp2(5) =', xp2(5))
    print('MyClass.pit2(x, 5) =', MyClass.pit2(x, 5))
    print('MyClass(10).pit(5) = ', MyClass(10).pit2(5))
    print('xp2 = MyClass.pit2(x, 5) = MyClass(10).pit(5)')

    print('\n5. Class & Instance Variables')
    print('instance vars: special cases unique to each instance\n'
          '(same toyota car with different parts depending on customer requirements)')
    print('class vars: for all attributes and methods which are used by all instances of the class.')

    class Dog:
        kind = 'beagle'

        def __init__(self, name):
            self.name = name

    pat1 = Dog('judy')
    pat2 = Dog('brown')
    print('Class variables will be shared by all instances: \n'
          '    pat1.kind =', pat1.kind,
          '    pat2.kind =', pat2.kind)
    print('Instance variables will be unique to each instance: \n'
          '    pat1.name =', pat1.name,
          '    pat2.name =', pat2.name)


    class Dog:
        owner = 'linda'
        def __init__(self, name):
            self.name = name
            self.tricks = []
            # init will always take name, and initialize an empty list to store tricks for an instance obj

        def add_tricks(self, trick):
            self.tricks.append(trick)
            # if add_tricks are called to pass a trick, tricks for an instance var will be updated.

        def return_tricks(self):
            return self.tricks

    dog2 = Dog('john')
    dog2.add_tricks('roll over')
    print(dog2.return_tricks())
    dog2.add_tricks('play dead')
    print(dog2.return_tricks())
    dog3 = Dog('wow')
    dog3.add_tricks('cotton candy')
    print(Dog.return_tricks(dog3))

    print('\nRemarks')
    print('If the same attribute name occurs in both instance & class, lookup'
          'prioritizes the instance (search in instance first).')
    print('For eg:'
          '\nclass Animal():'
          '\n    animal = "pig"\n'
          'a = Animal()\n'
          'a.animal will return pig\n'
          'a.animal = "cow", will return "cow" instead of "pig"')
    print('In python, it is a convention to have self as the first argument of a method in class.')
    print('In other words, self is just an argument name. It can be called anything.')

    print('\nInheritance')
    print('base class must be defined in the same scope as derived class')
    print('otherwise, class derivedClass(modname.baseClass) will work too')
    print('if an attribute reference is not found in a derived class, it will be searched in base class')
    print('To check if an instance is a class of ClassName, we can use isinstance(obj, className)')
    print('TRUE will be return if baseclass is parsed for an instance of the derived class.')
    print('One can check if A is a subclass of B by using issubclass(A, B)')

    print('\nMultiple inheritance')
    print('\nMultiple inheritance can also occur class derivedClass(base1, base2)')
    print('attributes will be searched in depth first, left to right order')
    print('*** here is in fact other paths to access the parent class')
    print('--- will need to learn more on method resolution order to understand this ----')

    print('\nPrivate Variables')
    print('private variables are prefixed with __')
    class Mapping:
        def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)

        def update(self, iterable):
            for item in iterable:
                self.items_list.append(item)

        __update = update  # private copy of original update() method

    class MappingSubclass(Mapping):

        def update(self, keys, values):
            # provides new signature for update()
            # but does not break __init__()
            for item in zip(keys, values):
                self.items_list.append(item)

    print('\nIterators')
    print('for calls iter() on a container object (list/dict etc).')
    print('iter() returns an iterator object defining the method __next__,\n'
          'which accesses the elements in the container one at a time.\n'
          'when __next__ reaches the end, it raises StopIteration and tells the for loop to terminate.\n'
          '__next__ can be called using next()')
    print('for eg: p = iter([1,2,3])\n'
          '        next(p)')
    print('after next(p) prints the last element, calling next(p) again will raise StopIteration')
    print('for --> gives object to iter() --> gives to __next__ --> read each element and return until the end')

    print('\nGenerators')
    print('generators act like functions with "yield" statement instead of "return"')
    print('For eg:\n'
          'def reverse(data):\n'
          '    for index in range(len(data)-1, -1, -1):\n'
          '        yield data[index]\n'
          'reverse([1,2,3,4]) will return a generator object\n'
          'for x in reverse([1,2,3,4]) will return what was defined in the generator function.')
    print('generator remembers all the data values & which statement was last executed\n'
          'hence is able to continue where it left off.')






