#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 列表去除重复元素.py 
@time: 2021/02/22 
"""

list1 = [1, 2, 5, 6, 7, 4, 8, 2, 7, 9, 4, 6, 3]

#方法一
print(set(list1))

#方法二 for 循环
list2=[]
for i in list1:
    if not i in list2:
        list2.append(i)
print(list2)


#方法三 列表推导式
list3 = []
[list3.append(i) for i in list1 if not i in list3]  # append别忘记添加参数
print(list3)