import numpy as np
'''本代码演示了在指定范围内随机生成四组参数，并将每次生成的参数数组写入另外的文件中'''
#定义四个参数的取值范围（上界和下界）
theta0_up = 20.
theta0_bottom = 0.
theta1_up = 1.
theta1_bottom = 0.
x_up = 20.
x_bottom = 0.2
y_up = 200.
y_bottom = 2.
nburn = 10 #设置循环次数
for i in range(0, nburn):
    theta_0 = np.random.random() * (theta0_up - theta0_bottom) + theta0_bottom
    theta_1 = np.random.random() * (theta1_up - theta1_bottom) + theta1_bottom
    theta_2 = np.random.random() * (x_up - x_bottom) + x_bottom
    theta_3 = np.random.random() * (y_up - y_bottom) + y_bottom
    #将四个参数组合成一个numpy数组
    theta_try = np.array([theta_0, theta_1, theta_2, theta_3])
    #每次写入会覆盖掉原来的内容
    with open('theta.dat', 'w') as file:
        file.write(str(theta_try))  # 将数据转成str类型就可以存到文件中去了
