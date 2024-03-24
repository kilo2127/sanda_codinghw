"""
Date: 2024.3.24
Author: 梁玮诚

"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Scatter

# 2018十国人均gdp数据，数据来源：世界银行官网
country_dict = {'USA':62823.31, 'China':9905.34, 'Japan':39727.12, 'Germany':47939.28, 'India':1974.38, 'UK':43306.31, 'France':41557.85, 
                    'Canada':46548.64, 'Russia':11287.36, 'Italy':34622.17}
# 国家按人均GDP从大到小排序
country_dict = dict(sorted(country_dict.items(), key = lambda x: x[1], reverse=True))

x_data = list(country_dict.keys())

bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis(
        "人均GDP",
        list(country_dict.values()),
        yaxis_index=1,
        color="#5793f3",
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="人均GDP（百万美元）",
            type_="value",
            min_=0,
            max_=100000,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
        )
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="恩格尔系数",
            min_=-40,
            max_=40,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#675bba")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value}"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="人均GDP与恩格尔指数组合分析"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    )
)

line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis(
        "恩格尔系数",
        [6.4, 10.7, 9.1, 8.1, 13.2, 16, 14.2, 28, 21.6, 29.8], # 数据来源：美国农业部经济研究局
        yaxis_index=2,
        color="#800080",
        label_opts=opts.LabelOpts(is_show=False),
    )
)

bar.overlap(line)

grid = Grid()
grid.add(bar, 
          opts.GridOpts(pos_left="10%", pos_right="10%"),
          is_control_axis_index=True, # 是否由自己控制 Axis 索引
          )
grid.render('./combination.html')
