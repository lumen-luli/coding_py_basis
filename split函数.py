#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: split函数.py 
@time: 2021/01/20 
"""

# split() 方法可以实现将一个字符串按照指定的分隔符切分成多个子串，这些子串会被保存到列表中（不包含分隔符），作为方法的返回值反馈回来
#参数
#str：表示要进行分割的字符串；
#sep：用于指定分隔符，可以包含多个字符。此参数默认为 None，表示所有空字符，包括空格、换行符“\n”、制表符“\t”等。不含参数，以空格进行分割，含参数时，以该参数进行分割。
#maxsplit：可选参数，用于指定分割的次数，最后列表中子串的个数最多为 maxsplit+1。如果不指定或者指定为 -1，则表示分割次数没有限制

s = "1 2 \n 3 4 "
print(s.split())


s1 = " 1 2 3 4 5 "
print(s1.split(" "))