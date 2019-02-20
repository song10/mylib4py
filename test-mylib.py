#!/usr/bin/env python3

from mylib import dictView, dictEx

tab = {'a': 1, 'b': 'hello'}

obj = dictView(tab)
assert (obj.a == tab['a'])
assert (obj.b == tab['b'])
print(obj.a, obj.b)

tab2 = dict(tab)
obj = dictEx(tab2)
obj.a = tab2['a'] = 2
obj.b = tab2['b'] = 'world'
assert (obj.a == tab2['a'])
assert (obj.b == tab2['b'])
print(obj.a, obj.b)
print(obj)
