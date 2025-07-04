# coding : utf-8
num = eval(input('请输入一个四位整数：'))
sd = num % 10 #个位上的数字
tens = num // 10 % 10 #十位上的数字
hundred = num // 100 % 10 #百位上的数字
thousand = num // 1000 #千位上的数字
print('个位上的数字:',sd)
print('十位上的数字:',tens)
print('百位上的数字:',hundred)
print('千位上的数字:',thousand)
