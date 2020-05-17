if __name__ == '__main__':
    print('Brief Tour of the Standard Library')
    print('\n1. Operating System Interface')
    print('import os brings in functions for interaction with the operating system.')
    print('For eg, os.getcwd() prints working directory\n'
          'os.chdir("newDir") sets a new working directory.\n'
          'and os.system("mkdir today") creates the directory "today" in the working directory.')
    print('Another module, shutil, provides a higher level interface than os.\n'
          'for eg: shutil.copyfile("file", "newfile")'
          'or shutil.move("movefrom", "to")')

    print('\n2. Wildcards')
    print('import glob\n'
          'glob.glob("*.py")\n'
          'return list of filenames with .py ')

    print('\n3. Command Line Arguements')
    print('import sys')
    print('command line arguments can be obtained by calling sys.argv')
    print('this will be helpful when writing scripts that takes in args directly from cmd')
    print('there is also a module argparse that is more complex')
    print('for eg:\n'
          'parser = argparse.ArgumentParser(prog="progname", description="description")\n'
          '# creates an instance of argparse.ArgumentParser\n'
          '# this is the "box" which will hold all info required to parse cmd info to python data'
          'parser.add_argument("filenames", nargs="+")\n'
          '# add_argument method is called to add on program arguments.\n'
          '# it defines how strings from cmd will be used and converted into objects\n'
          '# filenames will take narg="+" will take all arguments present and '
          '# error will be generated if none exists\n'
          '# nargs="*" does similar but will not throw error if no arguments are avail\n'
          '# nargs="?" consumes 1 arg, default value will be used if arg not identified in cmd\n'
          '# can also be used for default arguments\n'
          'parse.add_argument("-l", "--lines", type=int, default=10)\n'
          '# "-l" is a short form for "--lines". single dash will always consist a single characters\n'
          '# so -abc is -a -b -c. over here, -l or --lines can be called in cmd\n'
          '# value identified will take the long name, unless dest="xxx" is defined too\n'
          '# in cmd if --lines=5 is given then lines will take value 5, else it will be 10,\n'
          '# alternatively, if const=5 is defined in add_argument method, with action="store_const"\n'
          '# simply parsing --lines in cmd will suffice. lines will take value 5 instead of 10.\n'
          '# do note that the action has to be specified correctly.\n'
          '# another example will be if we want to store bool, action="store_true"\n'
          '# if --name is parsed., name will take value True.'
          'args = parser.parse_args()')

    print('\nAnother eg:')
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--test', dest='test2', nargs='*', type=int)
    p.add_argument('-o', '--oh', action='store_false')
    print('p.add_argument("-o" ,"--oh", action="store_false")\n'
          'p.parse_args(["--oh"]) will return\n',
          p.parse_args(["--oh", '--test=1', '--test=3']))

    print('\n4. Error output redirection & program termination:')
    print('sys.stderr.write("output error message" and carry on)')
    print('sys.exit() is the most direct way to terminate script')
    import sys
    sys.stdout.write('This is outputted\n')
    sys.stderr.write('chest')

    print('\n5. String pattern matching')
    print('re module provides regular exp tools for string processing.')
    import re
    print('re.findall, finds all words of string pattern')
    print(re.findall('f[A-Z]*', 'this is fAb, f13f, fAZD'))
    print('re.sub, sub all identified pattern with new pattern')
    print(re.sub('[0-9]', '1', 'ioh29'))
    print('simple substring methods such as string.replace("word", "replace") works')
    print("this is crazy".replace('crazy', 'insane'))

    print('\n6. Mathematics')
    print('math module: math.pi, math.cos etc')
    print('random module: for random selections')
    import random
    print('random.choice', random.choice(['bacon', 'ham', 'cheese']))
    print('random.choice', random.sample(range(10, 50), 5))
    print('random.random returns random float', random.random())
    print('random.randrange(x) returns random number within range of x', random.randrange(100))
    import statistics
    print('statistics module: for simple statistics')
    data = [1.42, 6.4, 15.14, 14.2]
    print('statistics.mean, ', statistics.mean(data))
    print('statistics.median, ', statistics.median(data))

    print('\n7. Internet access')
    print('urllib.request allows retrieving data from URL and smtplib allows for sending of emails')
    from urllib.request import urlopen
    print("with urlopen('url') as f:\n"
          "    for line in f:\n"
          "        line = line.decode('utf-8')\n")
    print('\n if you have a mailserver running on localhost\n'
          'import smtplib\n'
          'server = smtplib.SMTP("localhost")\n'
          'server.sendemail("fromAdd", "toAdd", """content"""\n'
          'server.quit()')

    print('\n8. Dates and times')
    from datetime import date
    print('from datetime import date')
    print("print today's date:", date.today())
    print('birthday, ', date(1990, 11, 14))
    bday = date(1990, 11, 14)
    print('number of days old:', date.today() - bday)

    print('\n9. Data compression')
    print('data archiving/compression can be done using modules such as\n'
          'zlib, gzip, bz2, lzma, zipfile and tarfile')
    print('For eg: import zlib\n'
          's = b"hello"\n'
          '# note that b here indicates bytes-like object instead of string literal\n'
          '# this is required for zipping\n'
          't = zlib.compress(t)')
    import zlib
    s = b'helllo ha'
    print(s)
    print('length of s = ', len(s))
    t = zlib.compress(s)
    print('length of zlib.compress(s) =', len(t))
    print('compressed object = ', t)
    print('zlib.decompress(t) = ', zlib.decompress(t))

    print('\n10. Performance measurement')
    print('timeit can be used to compute performance of a feature')
    from timeit import Timer
    print('from timeit import Timer')
    print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
    print(Timer('a,b = b,a', 'a=1; b=2').timeit())
    print('other modules like profile and pstats can be used to identify\n'
          'time critical sections in large blocks of code')

    print('\n11. Quality control')
    print('doctest module is a tool for scanning module and validating tests\n'
          'embedded in docstrings of programs')
    print('for eg:\n'
          'def avg(values):\n'
          '    """docstring something   \n'
          '    >>> print(avg([30, 20, 70]))\n'
          '    40.0\n'
          '    """\n'
          '    return sum(values)/len(values)')
    import doctest
    def avg(values):
        """get avg
        >>> print(avg([20, 30, 70]))
        40.0
        """
        return sum(values) / len(values)

    print(doctest.testmod())
    print('alternatively, unittest module allows for a more comprehensive set of tests\n'
          'for a program')
    import unittest

    class TestStatsFunctions(unittest.TestCase):
        def test_avg(self):
            self.assertEqual(avg([20, 30, 70]), 40.0)
            self.assertEqual(round(avg([1, 5, 7]), 1), 4.3)
            with self.assertRaises(ZeroDivisionError):
                avg([])
            with self.assertRaises(TypeError):
                avg(20, 30, 70)

    print('when unittest.main() is called, all the tests within the class will be ran')
    unittest.main()


