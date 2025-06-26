gen = (x for x in range(5))
print(gen)#并不会生成所有的值，而是按需生成
#Iterable（可迭代对象）和Iterator（迭代器）这两个类。
# 这两个类在 Python 中用于检查对象是否具有可迭代或迭代器的特性。
from collections.abc import Iterable, Iterator
#判断gen是否为可迭代对象
print(isinstance(gen, Iterable))
