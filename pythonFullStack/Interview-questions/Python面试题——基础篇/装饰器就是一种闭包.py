#实现了python装饰器的嵌套使用
def makebold(fn): #fn是被装饰的函数
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped

#使用这两个装饰器为函数添加HTML标签
@makebold #先应用这个，返回值被包裹在<i>中
@makeitalic#再应用这个，将上一步结果包裹在<b>中
def hello():
    return "Hello World!"


print(hello())
