#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'limin'

from tqsdk import TqApi
from tqsdk.ta import MA

'''
画图示例: 在附图中画指标线
注意: 画图示例中用到的数据不含有实际意义，请根据自己的实际策略情况进行修改
'''

api = TqApi(web_gui="http://192.168.139.1:9876") # web_gui="http://192.168.139.1:9876", 指定 web 界面地址, ip 应为本机 ip 地址
klines = api.get_kline_serial("SHFE.au1910", 24 * 60 * 60)
ma = MA(klines, 30)  # 使用tqsdk自带指标函数计算均线

# 示例: 在附图中画一根绿色的ma指标线
klines["ma_B2"] = ma.ma
klines["ma_B2.board"] = "B2"  # 设置附图: 可以设置任意字符串,同一字符串表示同一副图
klines["ma_B2.color"] = "green"  # 设置为绿色. 以下设置颜色方式都可行: "green", "#00FF00", "rgb(0,255,0)", "rgba(0,125,0,0.5)"

# 示例: 在另一个附图画一根比ma小4的宽度为4的紫色指标线
klines["ma_4"] = ma.ma - 4
klines["ma_4.board"] = "MA4"  # 设置为另一个附图
klines["ma_4.color"] = 0xFF9933CC  # 设置为紫色, 或者 "#9933FF"
klines["ma_4.width"] = 4  # 设置宽度为4，默认为1

# 由于需要在浏览器中查看绘图结果，因此程序不能退出
while True:
    api.wait_update()
