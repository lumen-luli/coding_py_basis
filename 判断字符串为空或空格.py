#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 判断字符串为空或空格.py 
@time: 2021/01/20 
"""

s1 = ""
s2 = " "
s3 = "   "


# 字符串为空：长度为0，则字符串为空。（空格有长度）
print(len(s1))


# 字符串为空格： s.isspace() == True 则字符串全部是空格
if s1.isspace():
    print("s1为空")
if s2.isspace():
    print("s2为空")
if s3.isspace():
    print("s3为空")

