x = [1, 2, 3]
assert x[0] == 1
assert x[1] == 2
# assert x[7]

y = [2, *x]
assert y == [2, 1, 2, 3]

y.extend(x)
assert y == [2, 1, 2, 3, 1, 2, 3]

assert x * 0 == [], "list __mul__ by 0 failed"
assert x * 2 == [1, 2, 3, 1, 2, 3], "list __mul__ by 2 failed"

# index()
assert ['a', 'b', 'c'].index('b') == 1
assert [5, 6, 7].index(7) == 2
try:
    ['a', 'b', 'c'].index('z')
except ValueError:
    pass
else:
    assert False, "ValueError was not raised"

# insert()
x = ['a', 'b', 'c']
x.insert(0, 'z') # insert is in-place, no return value
assert x == ['z', 'a', 'b', 'c']

x = ['a', 'b', 'c']
x.insert(100, 'z')
assert x == ['a', 'b', 'c', 'z']

x = ['a', 'b', 'c']
x.insert(-1, 'z')
assert x == ['a', 'b', 'z', 'c']

x = ['a', 'b', 'c']
x.insert(-100, 'z')
assert x == ['z', 'a', 'b', 'c']

try:
    x.insert(100000000000000000000, 'z')
except OverflowError:
    pass
else:
    assert False, "OverflowError was not raised"
