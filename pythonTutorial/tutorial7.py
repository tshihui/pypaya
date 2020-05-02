if __name__ == '__main__':
    print('formatting outputs with f or F')
    year = 1000
    event = 10
    print(f'the number of {event} in the last {year} years')

    print('another way to format output')
    yes = 248952
    no = 183095
    percent = no/yes
    print('{:-9} yes votes {:2.2%}'.format(yes, percent))

    s = 'hello world\n'
    print('Difference between str and repr: repr will print the version read by interpreter')
    print(str(s))
    print(repr(s))

    print('/n more on formatting')
    print('using the format {var:digitsBeforeDec.digitsf}')
    import math
    print(f'the value of pi is approx {math.pi:.3f}')
    tab = {'ohe' : 123, 'oeu':103, 'hwo':139}
    for tag, code in tab.items():
        print(f'{tag:10} ==> {code:10d}')

    print('{word!r} will apply repr to word')
    print('{word!s} will apply ascii to word')
    said = 'awwww'
    print(f'using !r: She said {said!r}')
    print(f'without !r, 10 letters spaces: She said {said:10}.')

    print('\nusing str.format()')
    print('We are going to be the {} awesome {}'.format('most', 'people'))
    print('insert numbers in the {} in strings determine positions of strings')
    print('We are going to be the {1} awesome {0}'.format('most', 'people'))

    print('This method works with keywords in {} too')
    print('We are going to be the {word1} awesome {word2}'.format(word1 = 'most', word2 = 'people'))
    print('Both positional and keyword arguments:')
    print("{date}'s breakfast will be {1} and {0}".format('eggs', 'spam', date = 'tomorrow'))
    menu = {'ham': 14, 'hotdogs': 5, 'tea': 2}
    print('Ham: {0[ham]:d}; Hotdogs: {0[hotdogs]:d}; Tea: {0[tea]:d}'.format(menu))
    print('Ham: {ham:d}; Hotdogs: {hotdogs:d}; Tea: {tea:d}'.format(**menu))

    for x in range(1, 11):
        print('{0:2d}, {1:3d}, {2:4d}'.format(x, x**2, x**3))

    print('manual string formatting')
    print('right padded')
    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x**2).rjust(3), repr(x**3).rjust(4), end = '\n')
    print('center')
    for x in range(1, 11):
        print(repr(x).center(2), repr(x ** 2).center(3), repr(x ** 3).center(4), end='\n')
    print('zfill : pads 0')
    for x in range(1, 11):
        print(repr(x).zfill(2), repr(x ** 2).zfill(3), repr(x ** 3).zfill(4), end='\n')

    print('old string formatting')
    import math
    print('the value of pi is %5.3f.' % math.pi)

    print('--- Reading & Writing Files')
    print('reading file with the format: open("filename", "option"')
    print('read options are: r= read, w = writing(overwrite), a=append, r+= read & write, b= binary')
    print('text mode will convert line endings depending on platform\n, \\n for linus and \\r\\n for windows\n when \
    reading, converting \\n to platform readable when writing.')
    print('It is better to read files using "with": \n  with open("filename") as f:\n read_data = f.read()\n\
    This ensures that file will be closed properly.')
    print('else, close file with: f.close()')
    import os
    print('\nTry reading file:')
    with open('func6.py') as f:
        testDat = f.read()
    print(repr(testDat))
    print(len(testDat))
    print('f.closed will print {}, suggesting file no longer available:'.format(f.closed))
    print('\nIf we read without using "with": f = open("filename"):')
    f = open('func6.py')
    print('The first time f.read() is ran, we get:\n', f.read())
    print('Running f.read() again, we get:', f.read().center(10))
    print('The first time f.read() is ran, all the lines were already exhausted.')

    f = open('func6.py')
    print('\nTo read line by line, we use readline()')
    print('First line:', f.readline())
    print('readline() prints "" when EOL is reached.')
    print('for loop can be used to read over the whole file with readline:')
    line = 0
    for fl in f:
        line += 1
        print(line, ':', f.readline())
    print('Note that first line of the file is not read in for loop as it was already read in previous steps')
    print('Alternatively, use readlines() or list(f)')
    print('Using list:', list(open('func6.py')))
    print('Using readlines:', open('func6.py').readlines())
    print('Either method return lines in a list')
    print('Compare these to f.read() which stores the whole file as a continuous string.')

    print('to write a string to the existing file, f.write() can be used')
    f = open('func6.py', 'a')
    print('Remember to write, the file has to be open with "w" or "r+" but this will overwrite the whole file')
    print('To append, we use "a"', f.write('#test'))
    print('f.write() will return length of string written')
    f.close()
    dat = open('func6.py').readlines()
    print('Now check the last line of the file', dat[len(dat)-1])

    print('\nMoving into JSON')
    print('Converting python data into string rep: serializing')
    print('Reconstructing data from string rep: deserializing')
    x = [1, 'oh', 'well']
    import json
    print('Using json dump to serialize object:', json.dumps(x))
    print('We can directly dump serialized object into a file using json.dump(x, openedfile)')
    print('To deserialize json file (string back to data), use object = json.load(jsonfile)')