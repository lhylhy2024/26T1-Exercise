import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

# 读取CSV文件
file_path = "C:/Users/LIN/PycharmProjects/T3Exercises/Project 4/4.2/city_consumption_data.csv"
data = pd.read_csv(file_path, encoding='utf-8')  # 根据实际情况调整编码

# 打印数据结构
print("用于图表展示的数据结构：")
print(data)

# 计算消费总额占比
total_consumption = data['社会消费品零售总额（亿元）'].sum()
data['占比（%）'] = data['社会消费品零售总额（亿元）'] / total_consumption * 100

# 准备绘图数据
labels = data['城市'].tolist()
sizes = data['社会消费品零售总额（亿元）'].tolist()

# 创建南丁格尔玫瑰图
pie = (
    Pie()
    .add(
        series_name="消费总额占比",
        data_pair=[list(z) for z in zip(labels, sizes)],
        radius=["30%", "70%"],
        rosetype="radius",  # 设置为南丁格尔玫瑰图
        label_opts=opts.LabelOpts(is_show=True, formatter="{b}: {c}亿元 ({d}%)"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2024年各地区消费总额占比"),
        legend_opts=opts.LegendOpts(is_show=True, orient="vertical", pos_top="15%", pos_left="2%"),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}亿元 ({d}%)")
    )
)

# 渲染图表到HTML文件
pie.render("C:/Users/LIN/PycharmProjects/T3Exercises/Project 4/4.2/2024年各地区消费总额占比.html")