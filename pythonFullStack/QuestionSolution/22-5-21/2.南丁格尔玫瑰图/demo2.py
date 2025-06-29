'''本代码演示了用pyecharts库绘制自定义的南丁格尔玫瑰图，来显示不同品牌的数据占比'''
import pyecharts.options as opts  # 导入图表配置模块，用于设置标题、标签、样式等细节。
from pyecharts.charts import Pie  # 导入饼图类，用于绘制玫瑰图（饼图的一种变体）。

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.apache.org/examples/editor.html?c=pie-doughnut

目前无法实现的功能:

1、迷之颜色映射的问题
"""

x_data = ["华为", "OPPO", "小米", "Vivo", "苹果"]  # 品牌名称
y_data = [1000, 852, 689, 897, 50]
data_pair = [list(z) for z in zip(x_data, y_data)]  # 组合x、y的数据
data_pair.sort(key=lambda x: x[1])  # 按数值从小到大排序（影响图表展示顺序）
# 下面开始绘制玫瑰图
(
    # 初始化饼图，设置画布宽1600px、高800px，背景色为深灰色（#2c343c）
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px", bg_color="#2c343c"))
    .add(
        series_name="访问来源",  # 系列名称（用于提示框等标识）
        data_pair=data_pair,  # 传入数据：[(品牌, 数值), ...]
        rosetype="radius",  # 设置为南丁格尔玫瑰图（按半径区分大小）
        radius="55%",  # 图表半径占画布的55%
        center=["50%", "50%"],  # 图表中心位置（水平50%，垂直50%，即居中）
        label_opts=opts.LabelOpts(is_show=False, position="center"),  # 隐藏中心标签
    )
    # 添加数据系列，配置玫瑰图的关键参数
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Customized Pie",  # 图表标题
            pos_left="center",  # 标题水平居中
            pos_top="20",  # 标题距离顶部20px
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),  # 标题文字为白色
        ),
        legend_opts=opts.LegendOpts(is_show=False),  # 隐藏图例（右侧的类别标识）
    )
    # 设置全局配置（标题、图例等）
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),  # 提示框格式：系列名<br/>品牌: 数值 (百分比)
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),  # 提示框格式：系列名<br/>品牌: 数值 (百分比)
    )
    # 设置系列配置（提示框、扇区标签样式）
    .render("customized_pie.html")  # # 生成HTML文件，保存路径为当前目录
)
