#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图标测试程序 - 验证图标是否正确显示
"""

import tkinter as tk
from tkinter import ttk
import os
import sys

def get_resource_path(relative_path):
    """获取资源文件的绝对路径（兼容打包后的exe）"""
    try:
        # PyInstaller创建的临时文件夹
        base_path = sys._MEIPASS
    except Exception:
        # 正常的Python环境
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

class IconTest:
    def __init__(self, root):
        self.root = root
        self.root.title("图标测试 - by 1Plabs.pro")
        self.root.geometry("500x400")
        
        # 设置窗口图标
        try:
            icon_path = get_resource_path('assets/window_icon.ico')
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
                print(f"✅ 窗口图标设置成功: {icon_path}")
            else:
                print(f"❌ 窗口图标文件不存在: {icon_path}")
        except Exception as e:
            print(f"❌ 设置窗口图标失败: {e}")
        
        # 主界面
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(main_frame, text="图标测试程序", font=("Arial", 16, "bold")).pack(pady=20)
        
        # 显示图标路径信息
        info_frame = ttk.LabelFrame(main_frame, text="图标信息", padding="10")
        info_frame.pack(fill=tk.X, pady=20)
        
        window_icon_path = get_resource_path('assets/window_icon.ico')
        exe_icon_path = get_resource_path('assets/app_icon.ico')
        
        ttk.Label(info_frame, text=f"窗口图标路径: {window_icon_path}").pack(anchor=tk.W, pady=5)
        ttk.Label(info_frame, text=f"窗口图标存在: {os.path.exists(window_icon_path)}").pack(anchor=tk.W, pady=5)
        ttk.Label(info_frame, text=f"exe图标路径: {exe_icon_path}").pack(anchor=tk.W, pady=5)
        ttk.Label(info_frame, text=f"exe图标存在: {os.path.exists(exe_icon_path)}").pack(anchor=tk.W, pady=5)
        
        # 测试按钮
        test_frame = ttk.Frame(main_frame)
        test_frame.pack(pady=20)
        
        ttk.Button(test_frame, text="测试窗口图标", command=self.test_window_icon).pack(side=tk.LEFT, padx=5)
        ttk.Button(test_frame, text="重新加载图标", command=self.reload_icon).pack(side=tk.LEFT, padx=5)
        
        # 状态标签
        self.status_label = ttk.Label(main_frame, text="就绪", foreground="green")
        self.status_label.pack(pady=10)
        
        print("🎯 图标测试程序启动")
        print("📍 查看窗口左上角是否显示图标")
    
    def test_window_icon(self):
        """测试窗口图标"""
        try:
            icon_path = get_resource_path('assets/window_icon.ico')
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
                self.status_label.configure(text="窗口图标重新设置成功", foreground="green")
                print(f"✅ 窗口图标重新设置: {icon_path}")
            else:
                self.status_label.configure(text="窗口图标文件不存在", foreground="red")
                print(f"❌ 窗口图标文件不存在: {icon_path}")
        except Exception as e:
            self.status_label.configure(text=f"设置窗口图标失败", foreground="red")
            print(f"❌ 设置窗口图标失败: {e}")
    
    def reload_icon(self):
        """重新加载图标"""
        self.test_window_icon()

def main():
    root = tk.Tk()
    app = IconTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()
