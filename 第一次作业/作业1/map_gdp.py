"""
Date: 2024.3.24
Author: 梁玮诚

"""
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType

# 读取数据
with open('./gdp_data.txt', 'r') as f:
    data = [line.strip().split('\t') for line in f]

# 处理数据
formatted_data = [(d[0], float(d[1])) for d in data]

c = (
    Map()
    .add("GDP（单位：百万美元）",
         formatted_data,
         maptype="world",
         is_map_symbol_show=False,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="世界GDP地图"),
        visualmap_opts=opts.VisualMapOpts(min_=min(d[1] for d in formatted_data), 
                                          max_=max(d[1] for d in formatted_data)),
    )
)

c.render('./output/map_gdp.html')