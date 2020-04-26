#######################
## Python Tutorial 5 ##
#######################

if __name__ == '__main__':
    # Lists #
    print('--- Lists ----')
    listA = [1,2,3,4]
    listA.append([1,2,3])
    print('Append [1,2,3] to [1,2,3,4]: ', listA, '\n')

    print('--- List comprehension ---')
    print('sequence of x**3 from 0 to 10')
    print([x**3 for x in range(11)], '\n')

    print('sequence of x**3 from 0 to 10 if x is odd')
    listComp = [x**3 for x in range(11) if x % 2 != 0]
    print(listComp, '\n')

    print('pop: last in first out ')
    print(listComp.pop(), '\n')

    print('Using deques')
    from collections import deque
    queue = deque(['apples', 'banana', 'pear'])
    print('queue: ', queue)
    print('we can popleft with deque lists. in other words, first in first out')
    print(queue.popleft(), '\n')

    print('slightly more complex list comprehension: for eg, transpose matrix')
    matrix = [[1,2,3,4], [5,6,7,8]]
    print('Original matrix: ', matrix)
    transMat = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print('Transposed matrix: ', transMat)
    print('Same can be obtained by using zip')
    transZip = [(x,y) for x, y in zip(*matrix)]
    print(transZip, '\n')

    print('del statement')
    del transZip[:]
    print('deleting all elements of transZip using del transZip[:]:', transZip, '\n')

    print('more sequence data types (lists, range) - tuples')
    print('A string like "hello there"')
    print('Converted to tuple becomes:', tuple('hello there'), '\n')

    print('Using sets: ')
    print('set only return unique items')
    print(set(['apple', 'orange', 'apple', 'pear']))
    print('set comprehension works too', {x for x in 'hello ha' if x not in 'abc'})
    a = set('abcd')
    b = set('bcdef')
    print('Suppose we have set a', a)
    print('and set b', b)
    print('Items in a and not in b = a-b', a-b)
    print('Items in a and in b or both = a|b', a|b)
    print('Items in a and b only = a&b', a&b)
    print('Items not in a or b but not in both = a^b', a^b, '\n')

    print('Going on to dictionaries')
    d = dict([('banana', 12), ('apple', 10), ('pear', 40)])
    print('dictionary, d: ', d)
    print('dictionary items in d: ', d.items())
    print('keys of d: ', d.keys())
    print('values of d: ', d.values())
    print('Find value of banana = ', d['banana'], '\n')

    print('Using enumerate')
    for (i, v) in enumerate(['apple', 'orange', 'monkey']):
        print('index: ', i, ' & ', 'item: ', v)

    print('\nReversed order: ')
    print(d.keys())
    print(reversed(d.keys()))
    print('sorted : ')
    print(sorted(d.keys()))




