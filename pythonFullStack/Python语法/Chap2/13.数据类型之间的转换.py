# coding:utf-8
x=10
y=3
z=x/y # 在执行除法运算，将运算的结果赋值给z
print(z,type(z)) # 隐式转换， 通过运算隐式的转了结果的数据类型

# float类型转换成int类型，只保留整数部分
print('float类型转换成int类型',int(3.14))
print('float类型转换成int类型',int(3.9))
print('float类型转换成int类型',int(-3.14))
print('float类型转换成int类型',int(-3.9))

# 将int类型转换成float类型
print('将int类型转换成float类型',float(10))

#将str类型转成int类型
print(int('100')+int('200'))

#将str类型转成float类型
print('将str类型转成float类型',float('3.14'))

#将str转成int或float类型报错的情况
# print(int('18a')) #ValueError: invalid literal for int() with base 10: '18a'
# print(int('3.14')) #ValueError: invalid literal for int() with base 10: '3.14'

#将str转成float类型报错的情况
#print(float('45a.987')) #ValueError: could not convert string to float: '45a.987'

#chr()与ord()函数
print(ord('杨')) #26472 ，将字符“杨”转成对应的整数 值
print(chr(26472)) #杨  将整数 值转成对应的字符

# 进制之间的转换操作 十进制与其它进制之间的转换
print('十进制转成十六进制:'+hex(26472))
print('十进制转成八进制:'+oct(26472))
print('十进制转成二进制:'+bin(26472))
