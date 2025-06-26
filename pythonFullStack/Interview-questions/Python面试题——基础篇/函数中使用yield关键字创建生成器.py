#用于生成斐波那契数列的生成器函数
def fib():
    a, b = 0, 1
    while True:#无限循环
        yield a #暂停函数执行，并将当前的值返回给调用者，下次调用next，函数会从这里开始
        a, b = b, a + b


def fib_d(times):
    n = 0
    a, b = 0, 1
    while n < times:
        yield b
        a, b = b, a + b
        n += 1

