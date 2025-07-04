# coding:utf-8
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print('--------------------------------------')
print(8>7 and 6>5) # True and True
print(8>7 and 6<5) # True and False
print(8<7 and 10/0) # 当第一个表达式为False时，不计算第二个表达式

print('--------------------------------------')
print(True or True)
print(True or False)
print(False or False)
print(False or True)
print('--------------------------------------')
print(8>7 or 10/0) #当第一个表达式为True时，不计算第二个表达式

print('--------------------------------------')
print(not True )
print(not False)
print(not (8>7))


