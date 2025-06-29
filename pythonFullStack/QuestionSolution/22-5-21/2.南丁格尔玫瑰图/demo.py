'''本代码演示了使用pyecharts绘制股票K线图（含均线和成交量）的完成案例，主要
功能是从网络获取道琼斯指数数据，然后绘制专业的股票技术分析图表'''

import requests  # 用于从 URL 获取 JSON 格式的股票数据；
from typing import List, Union  # 提供类型注解（如 List[Union[float, str]]），增强代码可读性和 IDE 支持；

from pyecharts import options as opts  # ptions 用于配置图表样式
from pyecharts.charts import Kline, Line, Bar, Grid  # Kline（K 线图）、Line（折线图，用于均线）、Bar（柱状图，用于成交量）、Grid（布局网格，用于组合多个图表）


# 获取数据：从指定 URL 获取道琼斯指数的历史数据（JSON 格式），并调用 split_data 函数处理数据。
def get_data():
    response = requests.get(
        url="https://echarts.apache.org/examples/data/asset/data/stock-DJI.json"
    )
    json_response = response.json()  # json解析，将HTTP响应的文本内容转化为Python字典
    # 解析数据
    return split_data(data=json_response)


# 整理数据 ： 将原始 JSON 数据拆分为三个关键部分，便于后续图表绘制。
def split_data(data):
    category_data = []  # 存日期，作为x轴刻度标签
    values = []  # 存储K线核心数据
    volumes = []  # 存储成交量数据
    # i：获取数据在列表中的索引
    # tick：原始数据的成交量
    for i, tick in enumerate(data):
        category_data.append(tick[0])  # 提取日期
        values.append(tick)  # 存储当前时间点的完整数据（日期+开高低收+成交量）
        ## 处理成交量：[索引, 成交量, 涨跌标识（1=涨，-1=跌）]
        volumes.append([i, tick[4], 1 if tick[1] > tick[2] else -1])
    return {"categoryData": category_data, "values": values, "volumes": volumes}


# 计算均线：计算指定天数的移动平均线（MA，Moving Average），如 MA5（5 日均线）、MA10（10 日均线）等。
def calculate_ma(day_count: int, data):
    result: List[Union[float, str]] = []  # 存储均线结果（数值或"-"）
    for i in range(len(data["values"])):
        if i < day_count:
            result.append("-")  # 数据不足时用"-"表示（无法计算均线）
            continue
        sum_total = 0.0
        # 计算前day_count天的收盘价平均值
        for j in range(day_count):
            sum_total += float(data["values"][i - j][1])  # 假设tick[1]是收盘价
            # 保留3位小数，取绝对值（避免负号干扰，实际均线无负）
        result.append(abs(float("%.3f" % (sum_total / day_count))))
    return result


# 绘制图表：绘制 K 线图、均线（折线）、成交量（柱状图），并通过网格布局组合图表。
def draw_charts():
    kline_data = [data[1:-1] for data in chart_data["values"]]  # 提取K线图的核心数据
    kline = (
        Kline()
        .add_xaxis(xaxis_data=chart_data["categoryData"])
        .add_yaxis(
            series_name="Dow-Jones index",
            y_axis=kline_data,
            itemstyle_opts=opts.ItemStyleOpts(color="#ec0000", color0="#00da3c"),
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(
                is_show=False, pos_bottom=10, pos_left="center"
            ),
            # 数据缩放（用于滑动查看历史数据）
            datazoom_opts=[
                opts.DataZoomOpts(  # 内部缩放（鼠标滚轮）
                    is_show=False,
                    type_="inside",
                    xaxis_index=[0, 1],  # 同时作用于K线和成交量的x轴
                    range_start=98,  # 初始显示范围（98%到100%，即最近数据）
                    range_end=100,
                ),
                opts.DataZoomOpts(  # 底部滑块缩放
                    is_show=True,
                    xaxis_index=[0, 1],
                    type_="slider",
                    pos_top="85%",  # 滑块位置（顶部85%处）
                    range_start=98,
                    range_end=100,
                ),
            ],
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
            ),
            # 提示框（鼠标悬停时显示详情）
            tooltip_opts=opts.TooltipOpts(
                trigger="axis",
                axis_pointer_type="cross",  # 十字准星指示器
                background_color="rgba(245, 245, 245, 0.8)",  # 背景色
                border_width=1,
                border_color="#ccc",
                textstyle_opts=opts.TextStyleOpts(color="#000"),
            ),
            # 视觉映射（关联涨跌颜色）
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,  # 不显示视觉映射组件
                dimension=2,  # 关联数据的第3个维度（涨跌标识）
                series_index=5,
                is_piecewise=True,
                pieces=[
                    {"value": 1, "color": "#00da3c"},
                    {"value": -1, "color": "#ec0000"},
                ],
            ),
            # 坐标轴指示器（十字线）
            axispointer_opts=opts.AxisPointerOpts(
                is_show=True,
                link=[{"xAxisIndex": "all"}],
                label=opts.LabelOpts(background_color="#777"),
            ),
            # 刷子工具（用于框选区域）
            brush_opts=opts.BrushOpts(
                x_axis_index="all",
                brush_link="all",
                out_of_brush={"colorAlpha": 0.1},  # 窗外区域透明度
                brush_type="lineX",  # 水平方向框选
            ),
        )
    )
    # 绘制均线
    line = (
        Line()
        .add_xaxis(xaxis_data=chart_data["categoryData"])
        .add_yaxis(
            series_name="MA5",  # 五日均线
            y_axis=calculate_ma(day_count=5, data=chart_data),  # 调用计算函数
            is_smooth=True,
            is_hover_animation=False,  # 关闭动画
            linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="MA10",
            y_axis=calculate_ma(day_count=10, data=chart_data),
            is_smooth=True,
            is_hover_animation=False,
            linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="MA20",
            y_axis=calculate_ma(day_count=20, data=chart_data),
            is_smooth=True,
            is_hover_animation=False,
            linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="MA30",
            y_axis=calculate_ma(day_count=30, data=chart_data),
            is_smooth=True,
            is_hover_animation=False,
            linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(xaxis_opts=opts.AxisOpts(type_="category"))
    )
    # 绘制成交量
    bar = (
        Bar()
        .add_xaxis(xaxis_data=chart_data["categoryData"])
        .add_yaxis(
            series_name="Volume",
            y_axis=chart_data["volumes"],  # 数据来源
            xaxis_index=1,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            # 配置成交量的x轴（下方网格）
            xaxis_opts=opts.AxisOpts(
                type_="category",
                is_scale=True,
                grid_index=1,
                boundary_gap=False,
                axisline_opts=opts.AxisLineOpts(is_on_zero=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
                axislabel_opts=opts.LabelOpts(is_show=False),
                split_number=20,
                min_="dataMin",
                max_="dataMax",
            ),
            yaxis_opts=opts.AxisOpts(
                grid_index=1,
                is_scale=True,
                split_number=2,
                axislabel_opts=opts.LabelOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(is_show=False),
                axistick_opts=opts.AxisTickOpts(is_show=False),
                splitline_opts=opts.SplitLineOpts(is_show=False),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    # 叠加K线和均线（将均线绘制在K线图上）
    overlap_kline_line = kline.overlap(line)

    # 创建网格布局（组合K线+均线和成交量图表）
    grid_chart = Grid(
        init_opts=opts.InitOpts(
            width="1000px",
            height="800px",
            animation_opts=opts.AnimationOpts(animation=False),  # 关闭动画
        )
    )
    # 添加成交量到下方网格（顶部63%处，高度16%）
    grid_chart.add(
        overlap_kline_line,
        grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", height="50%"),
    )
    grid_chart.add(
        bar,
        grid_opts=opts.GridOpts(
            pos_left="10%", pos_right="8%", pos_top="63%", height="16%"
        ),
    )
    # 生成HTML文件
    grid_chart.render("professional_kline_brush.html")


if __name__ == "__main__":
    chart_data = get_data()  # 获取并处理数据
    draw_charts()  # 绘制图表
