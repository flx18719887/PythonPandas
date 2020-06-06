import numpy as np
import pandas as pd

# columns = ['年龄', '星座', '身高']
# data= [[30, '巨蟹', '160cm'],
#        [28, '白羊', '168cm'],
#        [23, '金牛', '158cm'],
#        [25, '双子', '178cm'],
#        [22, '摩羯', '173cm']]
#
# index = ['小芳', '小宛', '小风', '阿泰', '小明']
# df = pd.DataFrame(data=data, index=index, columns=columns)
# df.index.name = '姓名'
# # print(df)
#
#
# # 将数据储存成csv格式
# df.to_csv('m1.csv')
# df.to_csv('m2.csv', encoding='gbk')
# df.to_csv('m3.csv', encoding='gbk', columns=['星座', '身高'])
# df.to_csv('m4.csv', encoding='gbk', header=False)
# df.to_csv('m5.csv', encoding='gbk', header=[1,2,3])
# df.to_csv('m6.csv', encoding='gbk', index=False)
# df.to_csv('m7.csv', encoding='gbk', sep='\t')
#
#
#
# # 将数据储存成excel格式
# df.to_excel('m.xlsx')
# df.to_excel('m1.xlsx', sheet_name='居民信息')


# 读取 csv 数据
# df = pd.read_csv('m1.csv')
# df = pd.read_csv('m1.csv', index_col=0)
# print(df)
# df = pd.read_csv('m2.csv', encoding='gbk', index_col=3, header=0)
# df = pd.read_csv('m7.csv', index_col=0, encoding='gbk')
# print(df)
# df = pd.read_csv('m7.csv', index_col=0, encoding='gbk', sep='\t')
# print(df)


# 读取 excel 数据
# df = pd.read_excel('m.xlsx')
# print(df)
# df = pd.read_excel('m.xlsx', index_col=0)
# print(df)
#
# df = pd.read_excel('m1.xlsx')
# print(df)
#
# df = pd.read_excel('m1.xlsx', sheet_name='居民信息')
# print(df)

# print("\n")
# # 将数据转换成其他数据类型
# s = df.to_string()
# print(s)
# print("\n")
#
# d = df.to_dict()
# print(d)
#
# print('\n')
# DF = pd.DataFrame(d)
# print(DF)
#
# print('\n')
# d_list = df.to_dict('list')
# print(d_list)
#
# print('\n')
# DLIST = pd.DataFrame(d_list)
# print(DLIST)
#
# print('\n')
# d_series = df.to_dict('series')
# print(d_series)
# print('\n')
#
# print(d_series.keys())
# print('\n')
#
# print(d_series.values())
# print('\n')
#
# print(d_series.items())
#
# print('\n')
# print(d_series['星座'])


# ds = df.to_dict('split')
# print(ds)
#
# print('\n')
# dr = df.to_dict('records')
# print(dr)
#
# print('\n')
# di = df.to_dict('index')
# print(di)


# 查看基本信息
df = pd.read_csv('m3.csv', encoding='gbk', index_col=0)
print(df)
print('\n')
print(df.head(2))
print('\n')
print(df.tail(2))
print('\n')
print(df.info())
print('\n')
print(df.index)
print('\n')
print(df.columns)
print('\n')
print(df.values)


