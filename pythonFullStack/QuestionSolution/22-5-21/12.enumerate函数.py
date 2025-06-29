lst = ['hello', 'world', 'python', 'java']
for index, item in enumerate(lst):  # index为序号，  item为列表中的元素，index默认从0开始
    print(index, '--------->', item)

print('---------------')

for index, item in enumerate(lst, 11):  # 指定index初始值为11
    print(index, '--------->', item)
