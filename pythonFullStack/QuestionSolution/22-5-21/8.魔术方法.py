print('abc' + 'bdc')  # 为什么可以进行字符串拼接呢？


# 因为str类里重写有__add__方法，所以可以执行拼接操作
# 自定义的，如果重写__add__方法，也可以实现这个操作

class A:  # 自定义类
    def __init__(self, name):  # 类的初始化方法,用于给实例属性进行赋值操作
        self.name = name

    def __add__(self, other):  # __add__方法
        return self.name + other.name

    def __len__(self):
        return 6


a = A('aaa')  # 创建一个A类的对象
b = A('bbb')  # 创建一个A类的对象
print(a + b)  # 由于重写了__add__方法，所以A类的对象a，b可以执行+ 操作

print(len(a))  # 结果为6，因为重写了__len__()方法
