import pandas as pd
from pyecharts.charts import Bar, Line, Grid
from pyecharts import options as opts

# 读取CSV文件
df = pd.read_csv('C:/Users/LIN/PycharmProjects/T3Exercises/Project 4/4.5/consumption_data.csv')

# 计算每个省份的平均消费额
province_avg = df.groupby('province')['consumption'].mean().round(2).reset_index()
province_avg.columns = ['province', 'avg_consumption']

# 计算每个地区的平均消费额
region_avg = df.groupby('region')['consumption'].mean().round(2).reset_index()
region_avg.columns = ['region', 'avg_consumption']

# 找出平均消费额最高的5个省份
top_5_provinces = province_avg.nlargest(5, 'avg_consumption')

# 打印用于图表展示的数据结构
print("省份平均消费额（前5）：")
print(top_5_provinces)
print("\n地区平均消费额：")
print(region_avg)

# 创建柱状图
bar = (
    Bar()
    .add_xaxis(top_5_provinces['province'].tolist())
    .add_yaxis(
        "省份平均消费额",
        top_5_provinces['avg_consumption'].tolist(),
        category_gap="50%",
        label_opts=opts.LabelOpts(position="top")  # 将数字放在柱子上面
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="省份平均消费额 vs 地区平均消费额"),
        yaxis_opts=opts.AxisOpts(name="平均消费额"),
        xaxis_opts=opts.AxisOpts(name="省份"),
        legend_opts=opts.LegendOpts(pos_bottom="2%", orient="horizontal")  # 将图例放在底部，水平排列
    )
)

# 创建折线图
line = (
    Line()
    .add_xaxis(region_avg['region'].tolist())
    .add_yaxis("地区平均消费额", region_avg['avg_consumption'].tolist(), is_smooth=True)
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(name="平均消费额", position="right"),
        legend_opts=opts.LegendOpts(pos_bottom="8%", orient="horizontal")  # 将图例放在底部，水平排列
    )
)

# 将折线图和柱状图组合到一个Grid中
grid = (
    Grid()
    .add(bar, grid_opts=opts.GridOpts(pos_left="10%", pos_right="60%"))
    .add(line, grid_opts=opts.GridOpts(pos_left="60%", pos_right="10%"))
)

# 渲染图表到HTML文件
grid.render("C:/Users/LIN/PycharmProjects/T3Exercises/Project 4/4.5/省份平均消费额 vs 地区平均消费额.html")