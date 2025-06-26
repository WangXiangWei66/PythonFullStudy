def outer(a):
    b = 10

    def inner():
        print(a + b)

    # b = b + 1
    return inner


if __name__ == '__main__':
    demo = outer(5)
    demo()

    demo2 = outer(7)
    demo2()
