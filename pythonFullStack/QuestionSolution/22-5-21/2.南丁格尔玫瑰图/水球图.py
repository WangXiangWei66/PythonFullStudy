from pyecharts import options as opts #用于设置图表样式和标题
from pyecharts.charts import Liquid #导入水球图类
from pyecharts.globals import SymbolType #导入符号类型，用于定义水球图形状

c = (
    Liquid() #对水球图图像初始化
    .add("lq",# 系列名称（用于标识该数据系列，在提示框等场景中显示）
         [0.6, 0.4], # 水球图的数据，0.6表示60%，0.4表示40%（会显示两个重叠的水球）
         is_outline_show=False,# 不显示外轮廓边框
         shape=SymbolType.DIAMOND)# 设置水球形状为钻石形（可选圆形、三角形等）
    #设置全局配置，标题等
    .set_global_opts(title_opts=opts.TitleOpts(title="Liquid-Shape-Diamond"))
    # 生成html文件
    .render("liquid_shape_diamond.html")
)
