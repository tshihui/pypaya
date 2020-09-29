if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    print('Three fundamental Pandas data structures:\n'
          '1. Series\n'
          '2. DataFrame\n'
          '3. Index\n')

    print('1. Pandas Series Object\n')
    print('1-D array of indexed data')
    data = pd.Series([1, 3, 6, 4])
    print(data)
    print('data.index returns the index of the Pandas Series', data.index)
    print('data.values returns the index of the Pandas Series', data.values)
    print('Series object can be accessed by indexing', data[3])
    print(data[1:2])
    print('* Series is more flexible than NumPy array *')
    print('NumPy array has index that are implicitly defined, while the index of Series is explictly defined.')
    print('What this means is that the index of Series can be something other than numbering.')
    data = pd.Series([3, 5, 6, 2], index=['john', 'jay', 'hannah', 'olivia'])
    print(data)
    print('We can also specify the dtype of the Series.')
    data = pd.Series([3, 5, 6, 2], index=['john', 'jay', 'hannah', 'olivia'], dtype='float64')
    print(data)
    print('Index-ing can be done via the associated tag, for eg data["jay"]:', data["jay"])
    print('Series is akin to a specialized dictionary - type specified.\n'
          'Like how type-specific NumPy array makes it more efficient than list,\n'
          'type-specific Series is more efficient that dictionaries for certain operations.')
    pdict = {'john':140, 'lydia':159, 'jay':130, 'mel':193}
    pSeries = pd.Series(pdict)
    print(pSeries)
    print('Pandas Series can be created from Dictionary. ! note that index will be SORTED.')
    print(pSeries['lydia':'jay'])
    print('Like dictionary, key can be used to extract value from the Pandas Series.\n'
          'Additionally, unlike dictionary, indexing using keys can be done to extract multiple values.')
    print('Creating some Pandas Series:')
    print(pd.Series(4, index=[x for x in range(5)]))
    print(pd.Series('oh', index=['japan', 'india']))
    print(pd.Series({'kfc':'chicken', 'macs':'fish burger', 'mos':'rice burger'}, index=['kfc', 'macs']))
    # Only specified index is returned.

    print('\n2. Pandas DataFrame Object')
    print('Similar to Series, DataFrame is a generalized version of Numpy array or specialized dictionary.')
    print('DataFrame can be thought of as a sequence of aligned 1-D Series Objects sharing the same index.')
    dic = {'omotesando':'hanzonmon', 'kudanshita':'tozai', 'akihabara':'hibiya'}
    dicCol = {'omotesando':'purple', 'kudanshita':'blue', 'akihabara':'grey'}
    chika = pd.Series(dic)
    print(chika)
    chikaIro = pd.Series(dicCol)
    print(chikaIro)
    chikaDF = pd.DataFrame({'lineName':chika, 'lineColor':chikaIro})
    print(chikaDF)
    print('index of DataFrame:', chikaDF.index)
    print('columns of DataFrame:', chikaDF.columns)
    print('Pandas DF acts like a specialized dictionary as we can use the "key" which is the column name,\n'
          'to obtain the values of the entire column, returning it as a Series Object.\n')
    print(chikaDF['lineName'])
    print('Creating DataFrame objects:')
    print('single series object:')
    print(pd.DataFrame(chikaIro, columns=['lineColor']))
    print('list of dictionaries:')
    print(pd.DataFrame([{'a':10*i, 'b':30} for i in range(3)]))
    print(pd.DataFrame([{'a':1, 'b':2}, {'b':10, 'c':40}]))
    print('dictionary of Series:')
    print(pd.DataFrame({'lineName':chika, 'lineCol':chikaIro}))
    print('2D Numpy Array:')
    print(pd.DataFrame(np.random.rand(3,4),
                       columns=['a', 'b', 'c', 'd'],
                       index=['one', 'two', 'three']))
    print('NumPy structured array:')
    A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
    print(A)
    print(pd.DataFrame(A))

    print('\n3. Pandas Index Object')
    print('index object is like an immutable array or an ordered set.')
    print(pd.Index([1,4,5,3]))
    print(pd.Index(['jay', 'hannah', 'jolin']))
    namesIdx = pd.Index(['jay', 'hannah', 'jolin'])
    print('index object can be indexed as per usual')
    print(namesIdx[1])
    print('and other common attributes of NumPy array', namesIdx.shape, namesIdx.dtype)
    print('The main diff between Index object and Numpy array is that INDEX OBJECT IS IMMUTABLE.')
    print('Index object has the conventions of Python sets structure, sets notations can be used.')
    namesIdx2 = pd.Index(['jay', 'hathaway', 'hathaway', 'romeo'])
    print('intersection: ', namesIdx & namesIdx2) # intersect
    print('union: ', namesIdx | namesIdx2) # union
    print('differences:', namesIdx2.difference(namesIdx)) # difference
    print(namesIdx2)

    print('\nData Indexing & Selection\n'
          '1. Data Selection in Series')
    print('Indexing of Series object builds on the concepts of NumPy array and python Dictionary')
    print('Series as dictionary:')
    data = pd.Series([1,2,4,5], index=['a', 'b', 'c',' d'])
    print(data['b'])
    print("'a' in data will return True or False", 'a' in data)
    print("data.keys return index", data.keys)
    print("list(data.items())", list(data.items()))
    print('we can modify Series objects like dictionary')
    data['e'] = 10
    print('Series as 1D arrays:')
    print("data['a':'c']", data['a':'c']) # 'c' is INCLUDED
    print("data[0:2]", data[0:2]) # 2 is EXCLUDED
    print("data[(data > 3) & (data < 10)]", data[(data > 3) & (data < 10)])
    print("data[['a', 'e']]", data[['a', 'e']])
    print('Indexers - loc, iloc, ix:')
    print('If Series has explicit numeric index, slicing with implicit index via data[1:3]\n'
          'will yield different output as data[1]')
    data = pd.Series(['oh', 'be', 'ko'], index=[1,4,5])
    print('data[1]', data[1])
    print('data[1:2]', data[1:2])
    print('.loc refers to the EXPLICIT INDEX')
    print('data.loc[1]', data.loc[1])
    print('data.loc[1:3]', data.loc[1:3])
    print('! note that if you call for an explicit index that is not present, an error will surface.')
    print('.iloc refers to the IMPLICIT INDEX')
    print('data.iloc[2]: getting element in position 2', data.iloc[2])
    print('data.iloc[1:2]: getting element in position 1 till 2(excluded)', data.iloc[1:2])
    print('Remember: Explicit is better than implicit!')

    print('\nData Selection in DataFrame')
    print('\nDataFrame as a dictionary')
    trainLine = pd.Series({'tozai': 'blue', 'hanzonmon': 'purple', 'asakusa':'red'})
    trainArea = pd.Series({'tozai':'nishikasai', 'hanzonmon':'hanzonmon', 'asakusa':'asakusa'})
    data = pd.DataFrame({'color':trainLine, 'area':trainArea})
    print(data)
    print('The columns can be called by "data.area" or data["area"], \n'
          'however if you have a column name = method name of DataFrame, the calling will\n'
          'point to the method instead of the column. As such, it is better to use [].')
    print('with pd.DataFrame, you can derive variables easily. For eg.\n'
          'data["lenDiv"] = data["color"].agg(len) / data["color].agg(len)')
    data['lenDiv'] = data['color'].agg(len) / data['area'].agg(len)

    print('\nDataFrame as a 2D array')
    print('data.values will return data in dataframe as an array')
    print(data.values, '\n', data.values.shape)
    print('This allows application of array functions')
    print('Transpose dataframe:', data.T)
    print('data.values[x] will return x row', data.values[0])
    print('while data[x] will throw error.')
    print('data.colname or data["colname"] will return the column.', data.color)
    print('we can again use loc, iloc and ix')
    print('get tozai&hanzonmon, and "area" column\n', data.loc['tozai':'hanzonmon', 'area'])
    print('get last 2 rows and last 2 columns\n', data.iloc[1:3, 1:3])
    print('get all rows and last column with iloc\n', data.iloc[:, 2])
    print('get tozai info with all columsn with loc\n', data.loc['tozai', :])
    print('conditional slicing can be performed with loc\n', data.loc[data.lenDiv > 0.4, 'color'])
    print('Values can be directly updated per position via iloc.')
    data.iloc[0,1] = 'kiba'
    print(data)
    print('note that even thought data[0] does not work,\n'
          'data[0:] works to return all the rows, or data[1:2] to return the 2nd row.\n', data[1:2])
    print('data["hanzonmon":] will also return rows from hanzonmon and after.', data["hanzonmon":])
    print('conditional splicing works too for eg, data[data.lenDiv > 0.4]', data[data.lenDiv > 0.4])

    print('\nOperating on Data in Pandas')
    print('\nUfuncs: Index Preservation')
    rng = np.random.RandomState(40)
    ser = pd.Series(rng.randint(0, 10, 4))
    print(ser)
    df = pd.DataFrame(rng.randint(0, 10, (3,4)), columns = ['A','B','C', 'D'])
    print(df)
    print('We can apply numpy ufuncs onto pandas Series of DataFrames')
    print('np.exp on Series\n', np.exp(ser))
    print('np.exp on DataFrame\n', np.exp(df), '\n'
                                               'applies exp to all columns')
    print('note that if any columns in Df is not numeric, then this application wont work.')

    print('\nUfuncs: Index Alignment')
    print('Pandas automatically align indices - if index is present in one and missing in order\n'
          'it will process accordingly.')
    sales = pd.Series({'bacon':30, 'eggs':20, 'ham':40})
    print(sales.index)
    earns = pd.Series({'bacon':100, 'tea':150, 'ham':130})
    print(earns.index)
    price = earns/sales
    print('taking earns/sales, we get\n', price)
    print('Note that this resuls is a UNION OF INDICES.', sales.index | earns.index)
    print('Where match of index didnt occur, pandas will fill it with NaN (not a number)')
    print('if we want to fill with some other value, we can perform the following\n'
          'earns.div(sales, fill_value = 0)\n',
          earns.div(sales, fill_value=0))
    print('Note that over here, fill_value\n'
          '    first: match indices of 2 series\n'
          '    secondly:  fill 0 for sales values that are missing\n'
          '    finally: take division\n'
          'this explains the inf value for tea as it was 150/0.')
    print('in DataFrame,\n')
    A = pd.DataFrame(rng.randint(0, 20, (2,2)), columns= list('ab'))
    print(A)
    B = pd.DataFrame(rng.randint(0, 40, (3,3)), columns=list('bac'))
    print(B)
    print('A+B', A+B)
    print('Note that as C was not present in A, NaN is returned for C.')
    print('If we used A.add(B, fill_value = 0)')
    print(A.add(B, fill_value = 0))
    print('After indices mapping between df A and B, missing values will take 0, then addition occurs')
    print('We can fill with more sophisticated values, such as mean per row for a and b')
    print('this can be achieved using A.stack(). Stack here stack values per row per columns')
    print('one can then perform function such as mean to get overall mean')
    print("A.stack().mean()", A.stack().mean())
    print(A.add(B, fill_value = A.stack().mean()))

    print('\nUfuncs: Operations Between DataFrame & Series')
    ran = np.random.RandomState(49)
    A = ran.randint(0,30, (3,4))
    print('In arrays, for eg if 1D array is subjected from 2D array, by the broadcasting rules\n'
          'subtraction is done row wise. For eg\n{}'.format(A))
    print('Subtracting A[0] from A, we get {}'.format(A -A[0]))
    df = pd.DataFrame(ran.randint(0,20, (3,4)), columns=list('agwo'))
    print('This is the same for DataFrame\n{}'.format(df))
    print('Subtracting first row, we get\n{}'.format(df-df.iloc[0]))
    print('Subtraction can be done column wise true specifying axis=0 in df.subtract()\n'
          'For eg, df.subtract(df["g"], axis=0)\n {}'.format(df.subtract(df['g'], axis=0)))
    print('If columns do not match completely, similar to before\n'
          '    first: match all - row/col wise\n'
          '    secondly: fill with NaN for missing\n'
          '    finally: perform arithmetic')
    print('for eg, if we subtract\n{a}\n'
          'from\n{b}\n'
          'we get\n{c}'
          ''.format(a=df.iloc[0,::2], b=df, c=df-df.iloc[0, ::2]))

    print('\nHandling Missing Data'
          '\nNONE:'
          '\nThe default type of an array with None will be object, which causes operations to be done\n'
          'on python level instead of the faster operations for native array types.\n'
          'Additionally, aggregations performed on object with None will throw an error.')
    print('\nNaN (not a number)'
          '\n np.nan is a special floating-point value following the IEEE floating-point representation.'
          '\n array with nan will be identified as float64 type, and operations will work, just returning nan.')
    print('To ignore nan during aggregations, functions in NumPy such as np.nansum(), np.nanmin() can be used')
    print(np.nansum(np.array([1,np.nan, 1, 4])))
    print('Note that whenever np.nan is included or None is included to a floating point array, upcasting might occur.\n'
          'None might be converted to nan.')

    print('methods such as isnull(), notnull(), dropna() are available in Pandas to handle missing vals.')
    df.loc[1, 'a'] = None
    print(df)
    df_drpna = df.dropna()
    print(f'For eg, to extract rows without na values\n{df_drpna}')
    print('! Note that only dropping of ENTIRE column or row is allowed in pd.DataFrame')
    df_drpnaCol = df.dropna(axis=1) # axis='columns' works too
    print(f'Dropping by col\n{df_drpnaCol}')
    df_fillna = df.fillna(-999)
    print(f'Using fillna, we will get\n{df_fillna}')
    print('dropna can be controlled, instead of dropping all rows/columns with 1 or few na,\n'
          'the option how="all" can be set, to only drop when all elements are na\n'
          , df.dropna(how='all'))
    print('Otherwise, we can set a threshold using thresh option\n - only drop if >= thres'
          , df.dropna(thresh=2))
    print('fillna has allows other methods of filling by setting method=\n'
          , df.fillna(method='ffill'), '\n'
                                       'or backfill\n',
          df.fillna(method='bfill', axis=1))

    print('\nHierarchical indexing / multiindexing')
    index = [('Singapore', 2015), ('Singapore', 2020), ('Japan', 2017), ('Japan', 2018)]
    index = pd.MultiIndex.from_tuples(index)
    print(f'Multilevel index\n'
          f'{index}')
    pay = pd.Series([4000, 7000, 3000, 6000], index=index)
    print(f'Setting multindex to pd.Series\n{pay}')
    paydf = pd.DataFrame(pay, columns=['pay'])
    paydf['save'] = [2000, 5000, 1000, 3000]

    print('Calling Series df["Singapore"] returns all regarding Singapore info,\n'
          'while df[:, 2015] returns all regarding 2015.')
    print('For DataFrame, we can use df.loc["Singapore"], df.loc["Singapore", "var1"]\n'
          'or df.loc["Singapore", 2015, "var1"]')
    print('Note that dfSeries.stack or df.unstack() can create different versions of dataframe (like melt & cast in R)')
    print('It is more straightforward to create series with multilevel then convert it into DataFrame\n'
          'then trying to set the indexes in the DF')

    print('\nMethods to create multiindex:')
    df = pd.DataFrame(np.random.rand(4,2),
                      index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                      columns=['v1', 'v2'])
    print(f'a) list of multiple lists in index while creating DF\n{df}')
    data = {('a', 2020):49, ('a', 2014):35, ('b', 2020):25, ('b', 2014):4}
    dataSe = pd.Series(data)
    print(f'b) using tuples as keys in dictionary for Series\n{dataSe}')
    multiArray = pd.MultiIndex.from_arrays([['a', 'a', 'b'], [1,2,2]])
    print(f'c) using pd.MultiIndex,\n'
          f'i. from_arrays()\n'
          f'{multiArray}')
    multiTuples = pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 2)])
    print(f'ii. from tuples()\n'
          f'{multiTuples}')
    multiLevels = pd.MultiIndex(levels=[['a', 'b'], [1,2]],
                                codes=[[0,0,1],[1,0,1]])
    print(f'iii. directly from MultiIndex with levels and codes\n'
          f'{multiLevels}')
    print('One can also name the indexes.')
    df.index.names = ['name1', 'name2']
    print(df)
    print('Columns in DataFrame can have multilevel indexes, like the rows.')
    index = pd.MultiIndex.from_product([[2013, 2014], [1,2]],
                                       names=['year', 'visit'])
    columns = pd.MultiIndex.from_product([['bob', 'lydia', 'jane'], ['hr', 'temp']],
                                         names=['subject','type'])
    print(f'iv. use from_product() to create indexes\n{index}\nand\n{columns}')
    data = np.round(np.random.rand(4,6), 1)
    data[:, ::2] *= 10
    data += 37

    health_data = pd.DataFrame(data, index=index, columns=columns)
    print(health_data)
    print('We can then extract by name\n health_data["lydia"]', health_data['lydia'])

    print('\nIndexing & Slicing a multiIndex\n'
          '- Multiply Indexed Series')
    print('For eg: pay["Singapore", 2015] or pay["Singapore"] or pay[:, 2015]\n'
          'or pay[pay>5000] or pay[["Singapore", "Japan"]]')
    print('- Multiply Indexed DataFrames')
    print('for eg, health_data["lydia", "hr"] which is calling by columns\n'
          'Or again using loc, iloc. health_data.loc[:, "jane"] or health_data.iloc[0:2, 1]\n'
          'health_data.loc[:, ("lydia", "hr")]')
    idx = pd.IndexSlice
    print(f'For more complex indexing of DataFrame slices, we can use pd.IndexSlice\n{idx}')

    print('\nRearranging Multi-indices')
    print('\n- Sorted and unsorted indices')
    print('! multiIndex slicing operations will FAIL IF index is NOT SORTED.')
    print('sort_index() can be used to sort by index')
    print('unstack & stack can be used to convert datasets')
    print('unstack.stack returns original. unstack(level=0 or 1).')
    print('essentially we are stacking or unstacking various indices together/apart')
    print('reset_index converts all indices into columns, works on both Series and DF')
    dat = pd.DataFrame({'val': [1, 2, 3, 4], 'co': [1, 3, 5, 3]},
                       index=pd.MultiIndex.from_product([['oh', 'no'], [1, 2]],
                                                        names = ['a','b']))
    print(f'If initial dataset is\n{dat}')
    print('We get\n{}\n'
          'after resetting index'.format(dat.reset_index()))

    print('\nData Aggregations on Multiple Indices')
    print('we can get the mean per a multiIndex by doing data.mean(level=xvar)')
    health_mean = health_data.mean(level='year')
    dat_mean = dat.mean(level='a')
    print(health_mean)
    print(dat_mean)

    print('\nCombining Datasets: Concat & Append')
    def make_df(cols, ind):
        """Quickly make a dataframe"""
        data = {c: [str(c) + str(i) for i in ind]
                for c in cols}
        return(pd.DataFrame(data, ind))

    # Recall numpy
    x = [1,2,3]
    y = [3,4,5]
    z = [4,5,6]
    print(np.concatenate([x,y,z]))
    # np.concatenate basically combines all into a single array
    # or
    x = [[1,2], [3,4]]
    print(np.concatenate([x,x], axis=1))

    ser1 = pd.Series(['a', 'b', 'c'], index=[1,2,3])
    ser2 = pd.Series(['b', 'd', 's'], index=[4,5,6])
    print('Pandas concat:', pd.concat([ser1, ser2]))

    print('concatente higher dimensional objects:')
    df1 = make_df('AB', [1,2])
    df2 = make_df('AB', [3, 4])
    print(df1)
    print(df2)
    print(pd.concat([df1, df2])) #rbind
    print('\n By default, concat is ROW-WISE.')

    df3 = make_df('AB', [0, 1])
    df4 = make_df('CD', [0, 1])
    print(df3)
    print(df4)
    print(pd.concat([df3, df4], axis=0))
    print(pd.concat([df3, df4], axis=1))
    print('Use axis argument. axis=0: row-wise (rbind), axis=1: col-wise (cbind')

    print('\nDuplicate indices')
    print('pandas concatenation preserves indices while np.concatenate does not')
    x = make_df('AB', [0,1])
    y = make_df('AB', [2,3])
    x.index = y.index
    print(x.index)
    print(x)
    print(y)
    xyCat = pd.concat([x, y])
    print('Duplicated indices are kept', xyCat)
    print(xyCat.index)
    print('Np version keeps no indices at all', np.concatenate([x,y]))

    print('\nRepeated indices are not a good idea in dataframes')
    print('Use pd.concat argument: verify_integrity raises an exception when there are duplicated indices\n')
    try:
        print(pd.concat([x, y], verify_integrity=True))
    except ValueError as e:
        print('ValueError:', e)

    print('\nWe can also choose to ignore existing indices and allow concat to automatically create new ones')
    print('Using ignore_index in pd.concat', pd.concat([x,y], ignore_index=True))

    print('\nKeys can be also included to preserve the structure of the concat, producing a multi-index DF')
    print(pd.concat([x,y], keys=['x', 'y']))

    print('\nTo concatenate DFs with different columns, we can use the join argument in pd.concat')
    print('note that the default join method is outer')
    df5 = make_df('abc', [4,5])
    df6 = make_df('cdf', [3,1])
    print(df5)
    print(df6)
    print(pd.concat([df5,df6]))
    print(pd.concat([df5, df6], join='inner'))

    print('\nAppend: df1.append(df2) is the same as pd.concat([df1,df2])')
    print('df5.append(df6): ', df5.append(df6))
    print('pd.concat([df5, df6]): ', pd.concat([df5, df6]))
    print('pd.append is not the same as list append - does not modify original object')
    print('in short, to concat many, pd.concat is more efficient than append method')

    print('\nCombining datasets: merge & join')
    print('\nCategories of Joins- pd.merge: 1) one-to-one\n'
          '2) many-to-one 3) many-to-many joins')
    print('1) one-to-one join')
    df1 = pd.DataFrame({'employee':['bob', 'jake', 'linda', 'lydia'],
                        'group': ['account', 'enginer', 'hr', 'hr']})
    df2 = pd.DataFrame({'employee': ['bob', 'linda'],
                        'hireDate': ['2004', '2008']})
    df3 = pd.merge(df1, df2)
    print(df1)
    print(df2)
    print(pd.merge(df1, df2))

    print('2) many-to-one join - preserves duplicates')
    df4 = pd.DataFrame({'group': ['account', 'enginer', 'hr', 'hr'],
                        'supervisor': ['mabel', 'john', 'mary', 'krissy']})
    df5 = pd.merge(df3, df4)
    print(df4)
    print(pd.merge(df3, df4))

    print('3) many-to-many join - duplicates in both left & right: exhaustive amount of duplicates')
    df6 = pd.DataFrame({'group':['account', 'account', 'enginer','hr', 'hr'],
                        'skills': ['math', 'excel', 'physics', 'communication', 'conversation']})
    print(pd.merge(df1, df6))

    print('we can use the on argument to specify which is the key column to merge on in pd.merge')
    print('if var names are different in left & right\n'
          'need to user left_on and right_on.')
    print('to drop unnecessary column, we can do pd.merge(df1, df2, left_on="x", right_on="y").drop("a", axis=1)')
    print(pd.merge(df1, df6).drop('skills', axis=1))

    print('merge can be on index too')
    df1a = df1.set_index('employee')
    df2a = df2.set_index('employee')
    print(df1a)
    print(df2a)
    print(pd.merge(df1a, df2a, left_index=True, right_index=True))
    print('this is essentially the same as df1a.join(df2a)')
    print(df1a.join(df2a))
    print('we can also set left_index with right_on and vice versa')
    print(df1a.columns.values)
    print(df2)
    print(pd.merge(df1a, df2, left_index=True, right_on='employee'))

    print('\nSpecifying Set Arithmetic for Joins')
    df6 = pd.DataFrame({'name': ['peter', 'lydia', 'mayu'],
                        'food': ['fish', 'cake', 'miso']},
                       columns=['name', 'food'])
    df7 = pd.DataFrame({'name': ['mayu', 'joseph'],
                        'drink': ['wine', 'beeer']},
                        columns=['name', 'drink'])
    print(df6)
    print(df7)
    print(pd.merge(df6,df7))
    print('by default, merge performs inner join. we can define how="left", "right", "outer"')
    print('outer', pd.merge(df6, df7, how='outer'))
    print('inner: intersect\n'
          'outer: union\n'
          'left: all left df\n'
          'right: all right df')
    print('left join', pd.merge(df6, df7, how='left'))
    print('right join', pd.merge(df6, df7, how='right'))

    print('\nOverlapping Column Names: suffixes keyword')
    df8 = pd.DataFrame({'name':['lydia', 'may', 'grace'],
                        'rank':[1,2,3]})
    df9 = pd.DataFrame({'name':['lydia', 'may', 'grace'],
                        'rank':[3,4,5]})
    print(df8)
    print(df9)
    print('rank in df8 and df9 are not the same. when joining, we can specify to only merge on name')
    print(pd.merge(df8, df9, on='name'), '\nNotce the suffixes on rank columns')
    print('we can specify the suffixes we want')
    print(pd.merge(df8, df9, on='name', suffixes=['_L', '_R']))

    datDir = '~/Documents/Programming/Python/data-USstates-master'
    pop = pd.read_csv(datDir+'/state-population.csv')
    areas = pd.read_csv(datDir+'/state-areas.csv')
    abbrevs = pd.read_csv(datDir+'/state-abbrevs.csv')

    print(pop.head())
    print(areas.head())
    print(abbrevs.head())

    m1 = pd.merge(pop, abbrevs, how='left', left_on='state/region',
                  right_on='abbreviation').drop('abbreviation', axis=1)
    print(m1)
    print(m1[m1['population'].isnull()].head())
    m1.loc[m1['state/region'] == 'PR', 'state'] = 'Puerto Rico'
    m1.loc[m1['state/region'] == 'USA', 'state'] = 'United States'
    print(m1.loc[m1['state/region'] == 'USA'])
    m2 = pd.merge(m1, areas, how='left', on='state')
    print(m2)
    print(m2.isnull().any())
    print(m2['state'][m2['area (sq. mi)'].isnull()].unique())
    m2.dropna(inplace=True) #removes all rows with NA

    # Problem: rank US states and territories by 2010 pop density
    m2['popDensity'] = m2['population']/m2['area (sq. mi)']
    m2010 = m2.query('year == 2010 & ages== "total"')
    print(m2010.shape)
    print(m2010.sort_values(by='popDensity', ascending=False))
    # alternatively, cleaner way:
    m2010.set_index('state', inplace=True)
    density = m2010['popDensity'].sort_values(ascending=False)
    print(density.head())

    print('\nAggregation & Grouping')
    import seaborn as sns
    planets = sns.load_dataset('planets')
    print(planets.shape)
    print(planets.head())
    rng = np.random.RandomState(23)
    ser = pd.Series(rng.rand(5))
    print(ser)
    print('df.sum()', ser.sum())
    print('df.mean()', ser.mean())
    df = pd.DataFrame({'A': rng.rand(3),
                       'B': rng.rand(3)})
    print(df)
    print('df.mean returns mean of each col\n', df.mean())
    print('df.mean(axis=1) returns mean of each row\n', df.mean(axis=1))

    print('describe() method is akin to summary in R which provides some sum stats of data')
    print(planets.dropna().describe())
    print('other typical methods exist - mean(), max(), prod(), sum()...')

    print('\nGroupBy:split, apply, combine')
    print('Think of groupby in R: split-apply-combine')
    df = pd.DataFrame({'key':['a','b','c','a','b', 'c'],
                       'data':range(6)},
                      columns=['key', 'data'])
    print(df)
    print('a groupby object can be created by calling df.groupby', df.groupby('key'))
    dfgroupbyobj = df.groupby('key')
    print('we can then apply the aggregate methods to the groupby object', dfgroupbyobj.sum())

    print('We can select groupby for specifc col in df\n', planets.groupby('method')['orbital_period'].median())

    print('groupby object also supports direct iteration over groups')
    for (method, group) in planets.groupby('method'):
        print("{0:40s} shape={1}".format(method, group.shape))

    print('Describe method can be also be used on groupby objects')
    print(planets.groupby('method')['year'].describe())
    print('Using .unstack()')
    print(planets.groupby('method')['year'].describe().unstack())

    print('/nAggregate, filter, transform, apply')
    rng = np.random.RandomState(0)
    df = pd.DataFrame({'key':['a', 'b', 'c', 'a', 'b', 'c'],
                       'data1':range(6),
                       'data2':rng.randint(0, 10, 6)}, columns=['key', 'data1', 'data2'])
    print(df)
    print('1) Aggregation')
    print('Allows for applying multiple functions to groups in groupby objects in one string of code')
    print(df.groupby('key').aggregate(['min', np.median, 'max']))

    print('2) Filtering')
    print('Allows for filtering on defined logical function')
    def filter_func(x):
        return x['data2'].std() > 4

    print(df.groupby('key').std())
    print(df.groupby('key').filter(filter_func))
    print('filter() returns boolean values which get passes back onto the groupby object')

    print('3) Transformation')
    print(df.groupby('key').transform(lambda x: x - x.mean()))

    print('4) Apply')
    print('Allows for application of function onto groupby results - function takes a Df, returns Df/Series/scalar')
    def norm_by_data2(x):
        x['data1'] /= x['data2'].sum()
        return x
    print(df.groupby('key').apply(norm_by_data2))

    print('5) Specifying keys for groupby splits')
    L = [0,1,0,1,2,0]
    D = {'a':'consonant', 'b':'consonant', 'c':'vowel'}
    print(f'For example, if we specify split to be on, {L}, we get {df.groupby(L).sum()}\n'
          f'We can also split by dictionary mapping such as {D}\n'
          f'We will get {df.set_index("key").groupby(D).sum()}\n'
          f'In other words, unless we specify the column name in groupby() for split, index will be reference\n'
          f'Therefore for {df.set_index("key")}\n'
          f'we can get {df.set_index("key").groupby(str.lower).sum()}\n'
          f'Multi-index can also be used in groupby.{df.set_index("key").groupby([str.lower, D]).mean()}')

    decade = 10 * (planets['year']//10)
    decade = decade.astype(str) + 's'
    decade.name = 'decade'
    print(decade)
    print('To return the sum of "number" in planets df grouping by method and number of decades\n'
          f'We can get \n{planets.groupby(["method", decade])["number"].sum().unstack().fillna(0)}')

    print('\nPivot tables are like multidimensional groupby')
    titanic = sns.load_dataset('titanic')
    print(titanic.head())
    print('The long coding that we will get when trying to groupby multiple indexes can be resolved '
          f'with the use of pivot tables.\n{titanic.groupby(["sex", "class"])["survived"].aggregate("mean").unstack()}')
    print('Pivot tables can be achieved with pivot_table method\n'
          f'{titanic.pivot_table("survived", index="sex", columns="class")}\n'
          f'a shorter string of code with pivot_table instead of aggregate returns the same output')

    print('Mutilevel pivot tables')
    age = pd.cut(titanic['age'], [0, 18,80])
    print(titanic.pivot_table('survived', ['sex', age], 'class'))
    fare = pd.qcut(titanic['fare'],2)
    print('We can automatically compute quantiles by using pd.qcut\n'
          f'{titanic.pivot_table("survived", ["sex", age], [fare, "class"])}\n'
          f'we will get pivot table tabulating results for survived, by sex and age, and 2 quantiles of fare & class.')
    print('df.pivot_table(data, values, index, columns, aggfunc, fill_value, margins, dropna, margins_name)'
          'is the full call for pivot_table\n'
          'the default aggregate function in pivot_table is mean. a dictionary can also be given to apply specifc'
          'functions to a column.\n'
          'For example,'
          f'{titanic.pivot_table(index="sex", columns="class", aggfunc={"survived":sum, "fare":"mean"})}\n'
          f'values have been left out here as the function will automatically select "survived" and "fare"\n'
          f'which have been parsed in the dictionary to aggfunc.\n'
          f'If one is keen to compute totals, we can use margins\n'
          f'{titanic.pivot_table("survived", index="sex", columns="class", margins=True)}\n'
          f'the totals column name can be set using margins_name="xxx", otherwise default="All"')

    print('Example data...')
    births = pd.read_csv("/Users/shihuitan/Documents/Programming/Python/births.csv")
    print(births.head())
    births['decade'] = 10 * (births['year'] // 10)
    print(births.pivot_table('births', index='decade', columns='gender', aggfunc='sum'))
    import matplotlib.pyplot as plt
    sns.set()
    births.pivot_table("births", index="year", columns='gender', aggfunc='sum').plot()
    plt.ylabel('total births per year')
    # plt.show()
    # data cleaning
    quartiles = np.percentile(births['births'], [25, 50, 75])
    mu = quartiles[1]
    sig = 0.74 * (quartiles[2] - quartiles[0]) # this gives a robust estimate of the sample mean
    # 0.74 * IQR of gaussian distribution
    births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
    # set day column to integer as it has become a string due to null values previously
    births['day'] = births['day'].astype(int)
    # create a date index
    births.index = pd.to_datetime(10000 * births.year +
                                  100 * births.month + births.day, format='%Y%m%d')

    births['dayofweek'] = births.index.dayofweek
    import matplotlib as mpl
    births.pivot_table('births', index='dayofweek', columns='decade', aggfunc='mean').plot()
    plt.gca().set_xticklabels(['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
    plt.ylabel('mean births by day')
    plt.show()

    births_by_date = births.pivot_table('births', [births.index.month, births.index.day])
    # this results in 2D pivot table - need to flatten it. can be done by converting both into a single index
    print(births_by_date.head())
    births_by_date.index = [pd.datetime(2012, month, day) for (month, day) in births_by_date.index]
    print(births_by_date.head())
    fig, ax = plt.subplots(figsize=(12,4))
    births_by_date.plot(ax=ax)
    plt.show()






