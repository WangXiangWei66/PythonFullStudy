import io  # io模块提供了处理各种 I/O 类型的工具。
import sys  # 可访问与 Python 解释器紧密关联的变量和函数。
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table  # table函数能够在图表中生成表格

# 将标准输出的编码设置为gb18030，目的是确保中文能在控制台正确显示
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于解析中文乱码

fig = plt.figure(figsize=(9, 10), dpi=1400)  # dpi为文件分辨率
ax = fig.add_subplot(111, frame_on=False)  # 添加一个子图，并且不显示边框
# 隐藏坐标轴
ax._axes.set_visible(False)
ax._axes.set_visible(False)

datas = pd.read_excel('Python课程班内序号表.xlsx')  # 读取excel文件

table(ax, datas, loc='center')
plt.savefig('result.jpg')  # 存成图片
