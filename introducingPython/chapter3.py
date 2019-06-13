# 3.1 
years_list = [1990, 1991, 1992, 1993, 1994, 1995]

# 3.2
years_list[3]

# 3.3
years_list[-1]

# 3.4
things = ['mozzarella', 'cinderella', 'salmonella']

# 3.5
things[1].title()
# no

# 3.6
things[0].upper()

# 3.7
del things[2]
print(things)

# 3.8
surprise = ['Groucho', 'Chico', 'Harpo']

# 3.9
llast = surprise[2].lower()
print(llast[::-1].upper())

# 3.10
e2f = dict([['dog','chien'], ['cat', 'chat'], ['walrus', 'morse']])

# 3.11
e2f['walrus']

# 3.12
f2e = {}
for eng, fren in e2f.items():
    f2e[fren] = eng

# 3.13
f2e['chien']

# 3.14
e2f.keys()

# 3.15
life = {
    'animals' : {'cats' : {'Henri', 'Grumpy', 'Lucy'}, 'octopi' : {}, 'other' : {}},
    'plants' : {},
    'other' : {}
}

# 3.16
life.keys()

# 3.17
life['animals'].keys()

# 3.18
life['animals']['cats']