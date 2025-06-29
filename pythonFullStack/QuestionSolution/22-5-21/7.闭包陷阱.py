'''闭包中变量的延迟绑定'''
def test3():
    fun_list = []
    for i in range(1, 4):
        def test4():
            return i ** 2

        fun_list.append(test4)
    return fun_list


f1, f2, f3 = test3()
print(f1(), f2(), f3())
