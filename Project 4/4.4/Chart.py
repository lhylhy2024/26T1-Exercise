import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

# 读取CSV文件
file_path = "C:/Users/LIN/PycharmProjects/T3Exercises/Project 4/4.4/province_data.csv"
data = pd.read_csv(file_path, encoding='utf-8')

# 打印原始数据结构
print("原始数据结构：")
print(data)

# 确保消费总额列的数据类型为数值类型
data['消费总额（亿元）'] = pd.to_numeric(data['消费总额（亿元）'], errors='coerce')

# 按消费总额降序排序，并取前10个省份
top_10_provinces = data.sort_values(by='消费总额（亿元）', ascending=False).head(10)

# 打印用于图表展示的数据结构
print("\n用于图表展示的数据结构：")
print(top_10_provinces)

# 创建条形图
bar = (
    Bar()
    .add_xaxis(top_10_provinces['省份'].tolist())
    .add_yaxis("消费总额（亿元）", top_10_provinces['消费总额（亿元）'].tolist(), label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2024年消费总额最高的10个省份"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),  # 旋转X轴标签，避免重叠
        yaxis_opts=opts.AxisOpts(name="消费总额（亿元）", type_="value", min_=0, max_=top_10_provinces['消费总额（亿元）'].max() * 1.1),  # 设置y轴范围
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(position="insideTop"),
    )
)


# 渲染图表到HTML文件
bar.render("C:/Users/LIN/PycharmProjects/T3Exercises/Project 4/4.4/2024年消费总额最高的10个省份.html")