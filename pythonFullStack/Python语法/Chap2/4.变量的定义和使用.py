# coding : uyf-8
# 创建一个整型变量luck_number,并为其赋值为8
luck_number = 8

my_name = '王祥伟'  # 字符串类型的变量
print(my_name, '的幸运数字为：', luck_number)
print('luck_number的数据类型是：', type(luck_number))

# Python动态修改变量的数据类型，通过赋不同的值就可以直接修改
# 变量的值可以修改
luck_number = '北京欢迎你'
print('luck_number的数据类型是：', type(luck_number))

# Python允许多个变量指向同一个值
no = number = 1024
print(no, number)
print(id(no))
print(id(number))
