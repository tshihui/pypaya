if __name__ == '__main__':
    print('syntax error vs other exception')
    print('Handling exceptions using try-except')
    print('First, statements under try will be executed.\nIf an exception occurs & exception is the same type\n'
          'specified after the except clause, statements under except will\n'
          'be executed then return to the try statement again.\n'
          'Else, execution will stop after executing the statements under except.')
    print('Except clause can take the form:\n'
          '     except (RuntimeError, ValueError, TypeError)')

    print('\nIn except clauses, the first matching except clause will be triggered.')
    print('For eg:')
    class B(Exception):
        pass

    class C(B):
        pass

    class D(C):
        pass

    print('In the order of except D-C-B')
    print('This function:\n')
    print("    for cls in [B, C, D]:\n"
          "try:\n"
          "    raise cls\n"
          "except D:\n"
          "    print('D')\n"
          "except C:\n"
          "    print('C')\n"
          "except B:\n"
          "    print('B')")
    print('--- Returns:')
    for cls in [B, C, D]:
        try:
            raise cls
        except D:
            print('D')
        except C:
            print('C')
        except B:
            print('B')

    print('\nWhile this:')
    print("    for cls in [B, C, D]:\n"
          "try:\n"
          "    raise cls\n"
          "except B:\n"
          "    print('B')\n"
          "except C:\n"
          "    print('C')\n"
          "except D:\n"
          "    print('D')")
    print('--- Returns:')
    for cls in [B, C, D]:
        try:
            raise cls
        except B:
            print('B')
        except C:
            print('C')
        except D:
            print('D')

    print('This is so as when classes were defined, B(Exception), C(B) and D(C).')

    print('\nWe can also not specify exception names by doing: except: ')
    print('and insert another raise clause within this except clause to raise exception again.')
    print('For eg:\n'
          'try:\n'
          '    print(z) #when z is not defined\n'
          'except:\n'
          '    print("Number not defined!")\n'
          '    raise')
    print('Will raise and error at the end')
    print('while...')
    print('For eg:\n'
          'try:\n'
          '    print(z) #when z is not defined\n'
          'except:\n'
          '    print("Number not defined!")\n'
          '    z = 10')
    try:
        print(z)
    except:
        print("Number not defined!")
        z = 10
    print('Helps to set z=', z)

    print('\nTry-except can also take an else clause which comes last:')
    print("try:"
          "    print(o)"
          "except ValueError:"
          "    print('no such number')"
          "else:"
          "    print('ok set to 100')"
          "    o += 100")
    print('This when o is present, will skip the except clause and perform else (Only if try statement is legit\n'
          'then do what is in the else.')
    o = 10
    print(f'o set to {o}')
    try:
        print(o)
    except ValueError:
        print('no such number')
    else:
        print('ok o + 100')
        o += 100
        print(f'Final o: {o}')

    print('Whenever necessary, a variable can be defined in the except clause')
    print('For eg:')
    print("try:\n"
          "    print(p)\n"
          "except Exception as inst:"
          "    print(type(inst))\n"
          "    print(inst.args)\n"
          "    print(inst)\n"
          "    print('ok set to 100')\n"
          "    p += 100\n")
    try:
        print(p)
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst)
        print('ok set to 100')
        p = 100

    print('\nTo note: exception handlers also handle exceptions raised in try clause through a function')

    print('\n Raising Exceptions:')
    print('raise statements forces an exception to occur.')
    print('raise xxxxx, xxxx represents the exception instance/exception class')
    print('When raised in the format: raise exceptName(arg), arg will be printed after the exceptName in the exception raised.')
    print('Exceptions can be looked at but not handled in the following manner:')
    print("    try:\n"
          "        print(q)\n"
          "    except Exception as er:\n"
          "        print(er)\n"
          "        raise")
    print('This will print the error and then raise the exception again')

    print('\nUser Defined Exceptions:')
    print('When a module consists of multiple exception classes, it is common to defined a base class for exception:')
    print('class Error(Exception)\n'
          '    pass')
    print('class InputError(Error):\n'
          '    ....')
    print('class PrintError(Error):\n'
          '    ...')

    print('\nDefine cleaning up actions:')
    print('try-finally')
    print('finally clause will be executed a) before any exception is raised in try b) before exiting try\n'
          'In other words, finally will be executed in any event.')
    print('try-finally-except (if there is an exception)')
    try:
        print(pp)
    except:
        print('!!! there was an EXCEPTION but we gonna ignore it')
        pass
    finally:
        print('prints this regardless of whether there is pp')
    pp = 50
    try:
        print(pp)
    finally:
        print('prints this regardless of whether there is pp')
    print('\nIn a function, if try and finally both have return statements and there were no exceptions,\n'
          'return in finally will be used')

    print('\nPredefined cleanup actions:')
    print('For eg, with statements in: with open("file.text") as f: ..., cleans up after the file is read.')
    print('This avoids unnecessary problems when running scripts.')