import random  # "Return random integer in range [a, b], including both end points.

number = random.randint(1, 100)

for i in range(1, 11):
    #input输出的内容默认以字符串形式返回
    Random_number = int(input('我在引种有一个1-100之间的数，请你猜一猜:'))
    if Random_number > number:
        print('大了')
    elif Random_number < number:
        print('小了')
    else:
        print('整好')
        print('恭喜你答对了,\n您一共猜了{}次'.format(i))
        break

if i < 3:
    print('真聪明')
elif 2 < i < 8:
    print('还凑合')
else:
    print('哦！天哪')
