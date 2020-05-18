if __name__ == '__main__':
    print('Modules that support professional programming needs.')
    print('\n1. Output formatting')
    import reprlib
    print(reprlib.repr(set('ahighaifja ohaoijpsa')))
    print(repr(set('ahighaifja ohaoijpsa')))
    print('repr in reprlib provides a version of abbreviated displays of large\n'
          'or deeply nested containers.')
    print('(repr generally prints everything)')

    import pprint
    print('pprint allows for more control over printing, such that output\n'
          'pretty printer adds line and indentations where appropriate.')
    t = [[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]
    print('pprint.pprint(t):\n')
    pprint.pprint(t)
    print('normal print(t):\n')
    print(t)

    import textwrap
    doc = """the wrap() method is just like fill() except that it returns a list of strings
    instead of one big string with newlines to separate wrapped lines"""
    print(textwrap.fill(doc, width=40))

    import locale
    print('locale module accesses a database of Cultural specific data formats.')
    print('for eg: locale.setlocale(locale.LC_ALL, "English_United States.1252")')
    # locale.setlocale(locale.LC_ALL, "English_United States.1252")
    print('we can data into specific formats after setting the desired locale.')

    print('\n2. Templating')
    print('string module includes Template class with a simplified syntax suitable for editing\n'
          'by end users.')
    from string import Template
    tt = Template('${country}man, knows that that $item costs $$10.')
    print(tt.substitute(country='japanese', item='chocolate'))
    print('substitute will raise error when the keyword argument is not provided')
    print('an alternative will be to use safe_substitute')
    print(tt.safe_substitute(country='india'))

    print('subclasses of template can specify specified delimiter')
    import time, os.path
    photofiles = ['img_1045.jpg', 'img_1494.jpg', 'img_2942.jpg']
    class BatchRename(Template):
        delimiter = '%'
    fmt = 'Ashley_%n%f'
    t = BatchRename(fmt)
    date = time.strftime('%d%b%y')
    for i, filename in enumerate(photofiles):
        base, ext = os.path.splitext(filename)
        newname = t.substitute(d=date, n=i, f=ext)
        # d is actually not in template... doesnt matter if you give extra arguments?
        print('{0} --> {1}'.format(filename, newname))

    print('Templating can help in outputting - for eg, outputting reports')

    print('\n3. binary data record layouts')
    print('struct module - pack() and unpack() for variable length binary record formats')
    print('information in a zip file can be access without using zipfile module.')

    print('\n4. multi-threading')
    print('threading: technique to separate processes that are not sequentially dependent')
    print('for eg, having use case running i/o while computations run in another thread')
    print('-- comparing with parallel programming which delegates one computation to multiple channels')
    print('threading module can be used here')
    import threading, zipfile
    class AsyncZip(threading.Thread):
        def __init__(self, infile, outfile):
            threading.Thread.__init__(self)
            self.infile = infile
            self.outfile = outfile

        def run(self):
            f = zipfile.ZipFile(self.outfile, 'w', 'zipfile.ZIP_DEFLATED')
            f.write(self.infile)
            f.close()
            print('finished background zip of: ', self.infile)

    # background = AsyncZip('mydata.txt', 'myarchive.zip')
    # background.start() will start to zip while main program continues to run in foreground
    # background.join() waits for the background tasks to finish
    print('one main challenge in multi threaded applications is the coordination of different threads\n'
          'which share data or other resources.\n'
          'queue module can be used to feed one running thread with requests from other threads,\n'
          'as a way to avoid coordination problems.')

    print('\n5. Logging')
    print('use of logging module to log messages from a program - either sent to a file or sys.stderr')
    import logging
    logging.debug('debug info')
    logging.info('informational message')
    logging.warning('warning: config file %s not found', 'server.conf')
    logging.error('error occured')
    logging.critical('critical error -- shutting down')
    print('debug and info messages are suppressed and the output is sent to standard error.')
    print('logging system can be 1) configured directly from python \n'
          '2) loaded from user editable config file\n')

    print('6. Weak References')
    print('python dose automatic memory management - garbage collection and ref counting')
    print('it frees memory shortly after the last reference to it has been eliminated')
    print('tracking objects creating references which are permanent')
    print('weakref module does so without creating a reference.\n'
          'an object is removed from the weakref table when not needed, and callback is triggered\n'
          'this is useful in situations such as caching objects that are expensive to create')
    import weakref, gc
    class A:
        def __init__(self, value):
            self.value = value
        def __repr__(self):
            return str(self.value)


    # creating a reference
    a = A(10)
    d = weakref.WeakValueDictionary()
    d['primary'] = a # no reference is created here
    print(d['primary'])
    del a
    print(gc.collect())
    print('d["primary"] will no longer be present at this point)')

    print('\n7. Tools for working with lists')
    print('array module')
    from array import array
    print('stores homogeneous data and stores them compactly.')
    a = array('H', [1,45,14,501]) # 'H' here is the typecode - 2 byte unsigned binary nubmers
    print(sum(a))
    print(a[1:4])

    print('\n deque in collections for faster appending and popping from the left')
    print('typical list pops from the right - lifo')
    from collections import deque
    d = deque(['task1', 'taks2', 'task3'])
    d.append('task4') # as per list
    print(d)
    print('handling first: ', d.popleft())
    print('handling last: ', d.pop())
    print('deque can be used for breadth first tree searches')

    print('\n bisect module contains functions for manipulating sorted lists')
    import bisect
    scores = [(100, 'c'), (200, 'e'), (500, 't')]
    print(scores)
    print('using bisect.insort, bisect.insort(score, (300, "r")) returns:')
    bisect.insort(scores, (300, 'r'))
    print(scores)

    print('\nheapq module can implement heaps from regular lists')
    pprint.pprint('heap: a specialized tree based data structure which is an '
          'almost complete tree that satisfies the heap property')

    print('\n8. Decimal floating point arithmetic')
    print('decimal module - Decimal datatype for decimal floating point arithmetic')
    print('this has more precision and control over exact decimal representation,\n'
          'tracking of significant decimal places, etc.')
    from decimal import *
    print('Using Decimal:')
    print(round(Decimal('0.7') * Decimal('1.05'), 2))
    print('Using normal computation:')
    print(round((0.70 * 1.05), 2))

    print('Using Decimal: Decimal("1.00") % Decimal("0.10"): ')
    print(Decimal("1.00") % Decimal("0.10"))
    print('vs normal: 1.00 % 0.10 : ')
    print(1.00 % 0.10)

    print('Using Decimal: sum([Decimal("0.10")*10]) == Decimal("1.0") ')
    print(sum([Decimal('0.10')*10]) == Decimal('1.0'))
    print('vs normal: sum([0.1] * 10) == 1.0: ')
    print(sum([0.1] * 10) == 1.0)

    print('Decimal returns as much precision as required')
    getcontext().prec = 30
    print('if we set precision to 30 with getcontext.prec = 30, 1/7 =')
    print(Decimal(1) / Decimal(7))