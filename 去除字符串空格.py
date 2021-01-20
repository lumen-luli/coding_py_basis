#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 去除字符串空格.py 
@time: 2021/01/20 
"""

# strip()方法，去除字符串开头或者结尾的空格
s = " a b c "
print(s.strip())
#lstrip()方法，去除字符串开头的空格
print(s.lstrip())
#rstrip()方法，去除字符串结尾的空格
print(s.rstrip())
#replace()方法，可以去除全部空格

print(s.replace(" ",""))
#join()方法+split()方法，可以去除全部空格
print("".join(s.split()))