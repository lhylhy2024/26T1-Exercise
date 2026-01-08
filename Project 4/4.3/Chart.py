import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts

# 读取CSV文件
file_path = "C:/Users/LIN/PycharmProjects/T3Exercises/Project 4/4.3/taobao_data.csv"
data = pd.read_csv(file_path, encoding='utf-8')  # 根据实际情况调整编码

# 去除列名中的空格
data.columns = data.columns.str.strip()

# 打印数据结构
print("用于图表展示的数据结构：")
print(data)

# 提取年份和纺织鞋服类目数据
years = data['年份'].astype(str).tolist()  # 确保年份为字符串类型
textile_shoes_clothing = data['纺织鞋服'].astype(float).tolist()  # 确保数据为浮点数类型

# 检查数据范围
print("年份数据：", years)
print("纺织鞋服数据：", textile_shoes_clothing)

# 创建折线图
line = (
    Line()
    .add_xaxis(years)
    .add_yaxis("纺织鞋服", textile_shoes_clothing, is_smooth=True)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="淘宝纺织鞋服类目每年上架商品数量变化情况"),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        yaxis_opts=opts.AxisOpts(name="上架商品数量（亿件）", type_="value", min_=0, max_=40),  # 设置y轴范围
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
)

# 渲染图表到HTML文件
line.render("C:/Users/LIN/PycharmProjects/T3Exercises/Project 4/4.3/淘宝纺织鞋服类目每年上架商品数量变化情况.html")