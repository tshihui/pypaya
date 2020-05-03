if __name__ == '__main__':
    print('syntax error vs other exception')
    print('Handling exceptions using try-except')
    print('First, statements under try will be executed.\nIf an exception occurs & exception is the same type\n'
          'specified after the except clause, statements under except will\n'
          'be executed then return to the try statement again.\n'
          'Else, execution will stop after executing the statements under except.')
    print('Except clause can take the form:\n'
          '     except (RuntimeError, ValueError, TypeError)')
