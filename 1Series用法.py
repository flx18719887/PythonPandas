# pandas 之 Series的创建与索引
import numpy as np
import pandas as pd
import random

age = [10, 20, 30, 40, 50, 60]
name = ['马一', '成二', '张三', '李四', '王五','周六']
s = pd.Series(age, index=name)
print("一维数组：\n", s)

# s.name # 提取名称
# s.index # 提取 索引
# s.values # 提取 值
# s.dtype # 提取 数据类型
# s.index.name # 索引名称
print('数组名称：', s.name)
print('数组元素：', s.values)
print('数组索引名称：', s.index.name)
print("=" * 50)

s.name = '居民年龄'
print(s)
print("=" * 50)
s.index.name = "姓名"
print(s)


# Series的索引有两种思路:
# 第一种把Series当做列表
# 第二种把Series当做字典
print("=" * 50)
print("s[3] =>", s[3])
print("s[王五] =>", s['王五'])
print("=" * 50)

# Series的切片：
print('s[2:4]=>\n', s[2:4])
print("=" * 50)
print("s[马一:李四]=>\n", s['马一':'李四'])
print("=" * 50)


print('s[s<30]=>\n', s[s<30])
print("=" * 50)
print('s[s>30]=>\n', s[s>30])
print("=" * 50)
print('s[s!=30]=>', s[s!=30])

print("*" * 50)
print(s[['张三', '李四', '王五']])
print("*" * 50)
print(s['成二':'王五'])
