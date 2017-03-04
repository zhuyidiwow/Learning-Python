#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *  # 导入 Tkinter 库
root = Tk()  # 创建窗口对象的背景色

# 创建两个列表
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']

# 创建两个列表组件
listb = Listbox(root)
listb2 = Listbox(root)

# 第一个小部件插入数据
for item in li:
    listb.insert(0, item)

# 第二个小部件插入数据
for item in movie:
    listb2.insert(0, item)

# 将小部件放置到主窗口中
listb.pack()
listb2.pack()

# 进入消息循环
root.mainloop()
