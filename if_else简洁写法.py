#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: if_else简洁写法.py 
@time: 2021/02/25 
"""
a, b, c = 1, 2, 3
if a>b:
    c = a
else:
    c = b

# 一行表达式
c = a if a>b else b


# 二维列表
c= [b, a][a > b]

# 利用逻辑运算符进行操作，都是最简单的东西，却发挥无限能量啊

c = (a>b and [a] or [b])[0]
# 改编版
c = (a>b and a or b)