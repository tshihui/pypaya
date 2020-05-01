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
