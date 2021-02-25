#-*- coding:utf-8 _*-  
""" 
@author:lupang 
@file: 列表合并.py 
@time: 2021/02/23 
"""
alist=[1,2,3]
blist=["w","x","y","z"]


#使用+
clist=alist+blist
print(clist)

#使用  extend
alist.extend(blist)
print(alist)

#使用append
alist.append(blist)
print(alist)

#使用切片
alist[len(alist):len(alist)]=blist
print(alist)

