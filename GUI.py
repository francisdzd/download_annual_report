#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020-10-09
# @Author  : dongdong

import tkinter as tk
import datetime as dt
import re
from DownJCZXW import *
import threading
import sys
global exit_flag
exit_flag=0

def down_by_stock():
    global exit_flag
    print('here is down_by_stock')
    print(e_search_key.get(),e_date_range.get())
    search_key = re.split("[ ;；，,]]",str(e_search_key.get()));
    search_key=';'.join(search_key)
    seDate=re.split('[~ ]]',str(e_date_range.get()))
    seDate='~'.join(seDate)
    filename = 'stock.txt'
    stock_arr = read_file_as_stock(filename)
    count = 0
    for stock in stock_arr:
        print(exit_flag)
        if exit_flag:
            sys.exit(0)
        count = count + 1
        print('正在查询公司代码：', stock, '   进度： ', count / len(stock_arr) * 100 // 1, '%')
        textshow.set('正在查询公司代码：' + str(stock) + '\n进度： ' + str(count / len(stock_arr) * 100 // 1) + '%')
        text.update()
        get_annList(stock, seDate,search_key)
    pass
def thread_fun(fun):
    global exit_flag
    thread=threading.Thread(target=fun)
    thread.setDaemon(True)
    thread.start()
def exit_all():
    exit_flag=1
    print('exit all',exit_flag)
    sys.exit(0)

L=5
start_row=2
today=dt.date.today()

root=tk.Tk()
root.geometry('320x320')
root.title('报告下载')

tk.Label(root,text="搜索关键词：").grid(row=0+start_row,pady=2*L)
tk.Label(root,text="时间范围  ：").grid(row=1+start_row,pady=2*L)
# row=1
e_search_key=tk.Entry(root)
e_search_key.grid(row=0+start_row,column=1,columnspan=2,padx=2*L,pady=2*L)
e_search_key.delete(0,tk.END)
e_search_key.insert(0,"年报;年度报告;中期")
#row=2
e_date_range=tk.Entry(root)
e_date_range.grid(row=1+start_row,column=1,columnspan=2,padx=2*L,pady=2*L)
e_date_range.delete(0,tk.END)
e_date_range.insert(0,str(today-dt.timedelta(days=3*365))+'~'+str(today))
#row=3
tk.Button(root,text="开始下载",width=3*L,command=lambda :thread_fun(down_by_stock)).grid(row=2+start_row,column=0,columnspan=2,padx=2*L,pady=L)
tk.Button(root,text="退出",width=3*L,command=exit_all).grid(row=2+start_row, column=2,padx=2*L,pady=L)

#row=4
textshow=tk.StringVar()
text=tk.Label(root,width=8*L,height=3*L,textvariable=textshow,justify=tk.LEFT,wraplength=250)
text.grid(row=3+start_row,columnspan=3,padx=L)
textshow.set('说明：点击开始下载按钮，从stock.txt中读入股票代码,从巨潮资讯网www.cninfo.com.cn下载该股票公司含关键词的公告文件' \
         '\n\n声明：本程序开源，仅用于个人学习使用，禁止用于商业用途')


tk.mainloop()




