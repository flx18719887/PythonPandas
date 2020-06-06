import numpy as np
import pandas as pd
# DataFrame 是一个带有索引的二维数据结构，每列可以有自己的名字，并且可以有不同的数据类型。

age = np.random.randint(20, 40, 6)
index = ['马一', '成二', '张三', '李四', '王五','周六']
s = pd.Series(age, index=index, name="居民年龄")
print(s)


print("=" * 60)
print("使用字典形式创建 DataFrame：\n")
name = ['马一', '成二', '张三', '李四', '王五','周六']
data = {'年龄':np.random.randint(30, 40, 6),
        '星座':['金牛座', '白羊座', '巨蟹座', '处女座', '狮子座', '摩羯座']}
df = pd.DataFrame(data, index)
print(df)


print("=" * 50)
print('使用二维列表形式创建 DataFrame：\n')
data = [[20, "天秤座"], [30, "水瓶座"], [23, "天蝎座"], [33, "双子座"], [26, "金牛座"], [22, "牡羊座"]]
df1 = pd.DataFrame(data, index = index)
print(df1)
print("*" * 30)
df1 = pd.DataFrame(data, index, columns=['年龄', '星座'])
print(df1)

print("=" * 60)
print("DataFrame的索引和切片：\n")
columns = ['年龄', '星座', '身高']
data = [[30, '白羊座', '160cm'],
        [26, '牧羊座', '162cm'],
        [28, '狮子座', '163cm'],
        [33, '水瓶座', '161cm'],
        [29, '金牛座', '158cm'],
        [22, '处女座', '177cm']]
index = ['小王', '小李', '小马', '小张', '小吴', '小夏']
df2 = pd.DataFrame(data = data, index = index, columns = columns)
print(df2)
print("*" * 30)
print('df2[年龄]=>\n', df2['年龄'])
print("*" * 30)
print('df2[身高]=>\n', df2['星座'])
print("*" * 30)
print('df2[["年龄", "身高"]]=>\n', df2[["年龄", "身高"]])
print("*" * 30)
print('df2[["年龄", "星座"]]=>\n', df2[["年龄", "星座"]])
print("*" * 30)
print('df2[["年龄", "身高", "星座", "身高"]]=>\n', df2[["年龄", "身高", "星座", "身高"]])

print("=" * 60)
print('df2.年龄=>\n', df2.年龄)
print("*" * 30)
print('df2.星座=>\n', df2.星座)

print("=" * 60)
print("df2=>\n", df2)
print("*" * 30)
df2['血型'] = "AB"
print("df2=>\n", df2)
print("*" * 30)
df2.pop('血型')
print("df2=>\n", df2)


print("显式索引 loc：\n")
# DataFrame.loc['行索引','列索引']
print(df2)
print("=" * 60)

print(df2.loc['小马', '星座'])
print("=" * 60)

print(df2.loc['小王', '年龄'])
print("=" * 60)

print(df2.loc['小李':'小吴', '年龄':'星座'])
print("=" * 60)

print(df2.loc['小王':'小吴':2])
print("=" * 60)

print(df2.loc[::-1, :])
print("=" * 60)

print(df2.loc[::-1])
print("=" * 60)

print(df2.loc[:, '年龄'])
print("=" * 60)

print(df2.年龄)
print("=" * 60)

print(df2.loc['小王'])
print("=" * 60)

print(df2.loc[['小李', '小张', '小夏'], ['年龄', '身高']])

print("\n")
print("隐式索引 iloc：\n")
print(df2)
print("=" * 60)
print('df2.iloc[2,1]=>', df2.iloc[2,1])
print('df2.iloc[4,2]=>', df2.iloc[4,2])
print('df2.iloc[5,1]=>', df2.iloc[4,2])
print('df2.iloc[3,0]=>', df2.iloc[3,0])
print("=" * 60)
print("切片：\n")
print(df2)
print("=" * 60)
print('df2.iloc[:3, 1:3]=>\n', df2.iloc[:3, 1:3])
print("=" * 60)
print('df2.iloc[::-1]=>\n',df2.iloc[::-1])
print("=" * 60)
print(df2)
print("=" * 60)
print('df2.iloc[[0, 1, 3, 5], [0, 2]]=>\n', df2.iloc[[0, 1, 3, 5], [0, 2]])

print("\n")
print("新增列数据：\n")
print(df2)
print("=" * 60)
df2['血型'] = ['A', 'O', 'B', "AB", 'A', 'O']
print(df2)


print("\n")
print("新增行数据：\n")
print(df2)
print("=" * 60)
df2.loc['阿泰'] = [31, '巨蟹座', '170cm', 'A']
print(df2)
print("=" * 60)
print(df2.loc['阿泰'])

print("\n")
print("删除数据：\n")
print(df2)
print("=" * 60)
df2.pop('血型')
print(df2)
print("=" * 60)

# df.drop() 可以通过 labels 和 axis 或者 index 和 columns 去进行数据的定位
df3 = df2.drop(index = '阿泰')
print(df3)
print("=" * 60)

df4 = df2.drop(index=['小王', '小夏'])
print(df4)

print("=" * 60)
df5 = df2.drop(columns = "星座")
print(df5)


print("=" * 60)
df6 = df2.drop(columns=['年龄', '身高'])
print(df6)

print("=" * 60)
df7 = df2.drop(index = ['小王', '小张', '阿泰'], columns = ['身高', '星座'])
print(df7)

print("=" * 60)
df8 = df2.drop(labels=['小王', '小马'])
print(df8)

print("=" * 60)
df9 = df2.drop(labels=['小吴', '小夏', '小张'], axis=0)
print(df9)



print("=" * 60)
df10 = df2.drop(labels=['年龄', '身高'], axis=1)
print(df10)

print("n")
print("修改数据：\n")
print(df2)
print("=" * 60)

df2.loc['小王', '星座'] = '金牛座'
print(df2)
print("=" * 60)

df2.loc['阿泰'] = [18, '狮子座', '180cm']
print(df2)
print("=" * 60)

df2.iloc[2,1] = '摩羯座'
print(df2)
print("=" * 60)

# df2.血型 = 'AB'
# print(df2)

 
