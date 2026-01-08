import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

# 读取CSV文件
data = pd.read_csv("C:/Users/LIN/PycharmProjects/T3Exercises/Project 4/4.1/consumption_data.csv",encoding="utf-8-sig")

# 计算各省份消费额的中位数
province_median = data.groupby('province')['consumption'].median().reset_index()
province_median['consumption'] = province_median['consumption'].round(2)
province_median = province_median.sort_values(by='consumption', ascending=False).head(10)

# 打印数据结构到控制台
print("子任务一数据结构：")
print(province_median)

# 使用pyecharts绘制柱状图
bar = Bar()
bar.add_xaxis(province_median['province'].tolist())
bar.add_yaxis("消费额中位数", province_median['consumption'].tolist())
bar.set_global_opts(
    title_opts=opts.TitleOpts(title="2024年各省份消费额中位数"),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
    yaxis_opts=opts.AxisOpts(name="消费额（元）"),
    datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
)

# 渲染图表到HTML文件
bar.render("C:/Users/LIN/PycharmProjects/T3Exercises/Project 4/4.1/province_median.html")

print("图表已生成并保存到 province_median.html 文件中。")