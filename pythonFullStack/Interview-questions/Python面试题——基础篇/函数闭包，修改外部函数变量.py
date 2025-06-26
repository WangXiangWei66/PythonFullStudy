def outer(a):
    b = 10

    def inner():
        nonlocal b #表示这个变量不是局部空间的变量，需要向上一层变量空间找这个变量
        print(b)
        b = b + 1
        print(a + b)
#外函数结束的时候发现内函数会用到自己的临时变量，这两个临时变量就不会释放，会绑定给内部函数
    return inner


if __name__ == "__main__":
    demo = outer(5)
    demo()

    demo2 = outer(7)
    demo2()
