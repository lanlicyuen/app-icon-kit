#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图标演示程序 - 展示窗口图标和菜单图标
"""

import tkinter as tk
from tkinter import ttk, Menu
import os

class IconDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("图标演示 - by 1Plabs.pro")
        self.root.geometry("400x300")
        
        # 设置窗口图标
        try:
            if os.path.exists('assets/window_icon.ico'):
                self.root.iconbitmap('assets/window_icon.ico')
        except:
            pass
        
        # 创建菜单
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
        # 文件菜单
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="新建", command=self.new_file)
        file_menu.add_command(label="打开", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)
        
        # 编辑菜单
        edit_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="编辑", menu=edit_menu)
        edit_menu.add_command(label="剪切", command=self.cut)
        edit_menu.add_command(label="复制", command=self.copy)
        edit_menu.add_command(label="粘贴", command=self.paste)
        
        # 帮助菜单
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="帮助", menu=help_menu)
        help_menu.add_command(label="关于", command=self.about)
        
        # 主界面
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="图标演示程序", font=("Arial", 16, "bold")).pack(pady=20)
        ttk.Label(main_frame, text="查看窗口左上角和菜单栏的图标").pack(pady=10)
        ttk.Label(main_frame, text="by 1Plabs.pro", font=("Arial", 12)).pack(pady=10)
        
        ttk.Button(main_frame, text="测试", command=self.test).pack(pady=10)
    
    def new_file(self):
        print("新建文件")
    
    def open_file(self):
        print("打开文件")
    
    def cut(self):
        print("剪切")
    
    def copy(self):
        print("复制")
    
    def paste(self):
        print("粘贴")
    
    def about(self):
        tk.messagebox.showinfo("关于", "图标演示程序\nby 1Plabs.pro")
    
    def test(self):
        tk.messagebox.showinfo("测试", "图标显示正常！")

def main():
    root = tk.Tk()
    app = IconDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
