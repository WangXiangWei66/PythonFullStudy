x = range(1, 10, 3)  # start=1, stop=10,step=3  ,产生一个1到10之间的整数，不包含10
# 结果为 1,4,7
print(list(x))  # [1,4,7] ,如果将x作为循环使用，循环会执行三次

for x in range(1, 10, 3):
    print(x)
