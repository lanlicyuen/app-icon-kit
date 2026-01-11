#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图标配置设置脚本
设置菜单图标和窗口左上角图标
"""

import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

def create_window_icon():
    """创建窗口左上角图标"""
    print("🪟 创建窗口图标...")
    
    # 检查源图标
    source_icon = "assets/app_icon.png"
    if not os.path.exists(source_icon):
        print(f"❌ 源图标不存在: {source_icon}")
        return False
    
    try:
        # 打开并调整图标
        img = Image.open(source_icon)
        
        # 确保是正方形
        if img.size[0] != img.size[1]:
            size = min(img.size)
            left = (img.size[0] - size) // 2
            top = (img.size[1] - size) // 2
            img = img.crop((left, top, left + size, top + size))
        
        # 调整到32x32（窗口图标标准尺寸）
        img = img.resize((32, 32), Image.Resampling.LANCZOS)
        
        # 保存为ICO
        window_icon_path = "assets/window_icon.ico"
        img.save(window_icon_path, format='ICO')
        
        print(f"✅ 窗口图标已创建: {window_icon_path}")
        return True
        
    except Exception as e:
        print(f"❌ 创建窗口图标失败: {e}")
        return False

def create_menu_icons():
    """创建菜单图标"""
    print("📋 创建菜单图标...")
    
    # 创建菜单图标文件夹
    menu_dir = "assets/menu_icons"
    os.makedirs(menu_dir, exist_ok=True)
    
    try:
        # 从主图标创建菜单图标
        source_icon = "assets/app_icon.png"
        if not os.path.exists(source_icon):
            print(f"❌ 源图标不存在: {source_icon}")
            return False
        
        img = Image.open(source_icon)
        
        # 确保是正方形
        if img.size[0] != img.size[1]:
            size = min(img.size)
            left = (img.size[0] - size) // 2
            top = (img.size[1] - size) // 2
            img = img.crop((left, top, left + size, top + size))
        
        # 创建不同尺寸的菜单图标
        sizes = [16, 24, 32]
        
        for size in sizes:
            resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
            icon_path = os.path.join(menu_dir, f"menu_icon_{size}x{size}.png")
            resized_img.save(icon_path, "PNG")
            print(f"✅ 菜单图标已创建: {icon_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ 创建菜单图标失败: {e}")
        return False

def update_source_code():
    """更新源代码以使用图标"""
    print("📝 更新源代码...")
    
    try:
        # 读取稳定版源代码
        with open('stable_icon_generator.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 添加窗口图标设置
        icon_code = '''
        # 设置窗口图标
        try:
            if os.path.exists('assets/window_icon.ico'):
                self.root.iconbitmap('assets/window_icon.ico')
        except:
            pass  # 如果图标文件不存在，忽略错误
'''
        
        # 在__init__方法中添加图标设置
        init_pos = content.find('self.center_window()')
        if init_pos != -1:
            insert_pos = content.find('\n', init_pos) + 1
            content = content[:insert_pos] + icon_code + content[insert_pos:]
        
        # 保存更新后的代码
        with open('stable_icon_generator_with_icons.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ 源代码已更新: stable_icon_generator_with_icons.py")
        return True
        
    except Exception as e:
        print(f"❌ 更新源代码失败: {e}")
        return False

def create_icon_demo():
    """创建图标演示程序"""
    print("🎨 创建图标演示...")
    
    demo_code = '''#!/usr/bin/env python3
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
        tk.messagebox.showinfo("关于", "图标演示程序\\nby 1Plabs.pro")
    
    def test(self):
        tk.messagebox.showinfo("测试", "图标显示正常！")

def main():
    root = tk.Tk()
    app = IconDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
'''
    
    try:
        with open('icon_demo.py', 'w', encoding='utf-8') as f:
            f.write(demo_code)
        print("✅ 图标演示程序已创建: icon_demo.py")
        return True
    except Exception as e:
        print(f"❌ 创建演示程序失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("🎯 图标配置设置工具")
    print("   设置窗口图标和菜单图标")
    print("   by 1Plabs.pro")
    print("=" * 60)
    
    # 检查assets文件夹
    if not os.path.exists('assets'):
        print("📁 创建assets文件夹...")
        os.makedirs('assets')
    
    # 检查主图标
    main_icon = "assets/app_icon.png"
    if not os.path.exists(main_icon):
        print(f"❌ 主图标不存在: {main_icon}")
        print("请先将1024x1024的PNG图标命名为app_icon.png放入assets文件夹")
        return
    
    print(f"✅ 找到主图标: {main_icon}")
    
    # 创建各种图标
    success = True
    
    if not create_window_icon():
        success = False
    
    if not create_menu_icons():
        success = False
    
    if not update_source_code():
        success = False
    
    if not create_icon_demo():
        success = False
    
    if success:
        print("\n🎉 图标配置完成！")
        print("\n📁 生成的文件:")
        print("   - assets/window_icon.ico (窗口图标)")
        print("   - assets/menu_icons/ (菜单图标文件夹)")
        print("   - stable_icon_generator_with_icons.py (带图标的源码)")
        print("   - icon_demo.py (图标演示程序)")
        
        print("\n🚀 使用方法:")
        print("   1. 测试图标: python icon_demo.py")
        print("   2. 构建exe: 使用stable_icon_generator_with_icons.py构建")
        print("   3. 图标位置:")
        print("      - 窗口左上角: assets/window_icon.ico")
        print("      - exe文件图标: assets/app_icon.ico")
        
        print("\n💡 图标说明:")
        print("   - window_icon.ico: 32x32，用于窗口左上角显示")
        print("   - app_icon.ico: 多尺寸，用于exe文件图标")
        print("   - menu_icons: 16x16, 24x32, 32x32，用于菜单显示")
        
    else:
        print("\n❌ 图标配置失败，请检查错误信息")

if __name__ == "__main__":
    main()
