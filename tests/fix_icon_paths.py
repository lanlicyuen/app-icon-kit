#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复图标路径问题
解决打包后图标不显示的问题
"""

import os
import sys
import subprocess
import shutil
import time

def get_resource_path(relative_path):
    """获取资源文件的绝对路径（兼容打包后的exe）"""
    try:
        # PyInstaller创建的临时文件夹
        base_path = sys._MEIPASS
    except Exception:
        # 正常的Python环境
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def create_fixed_source():
    """创建修复路径问题的源代码"""
    print("🔧 创建修复路径问题的源代码...")
    
    try:
        # 读取原始源代码
        with open('stable_icon_generator_with_icons.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 添加资源路径函数
        resource_function = '''
def get_resource_path(relative_path):
    """获取资源文件的绝对路径（兼容打包后的exe）"""
    try:
        # PyInstaller创建的临时文件夹
        base_path = sys._MEIPASS
    except Exception:
        # 正常的Python环境
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)
'''
        
        # 替换图标设置代码
        old_icon_code = '''        # 设置窗口图标
        try:
            if os.path.exists('assets/window_icon.ico'):
                self.root.iconbitmap('assets/window_icon.ico')
        except:
            pass  # 如果图标文件不存在，忽略错误'''
        
        new_icon_code = '''        # 设置窗口图标
        try:
            icon_path = get_resource_path('assets/window_icon.ico')
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except:
            pass  # 如果图标文件不存在，忽略错误'''
        
        # 添加资源路径函数到文件开头
        import_pos = content.find('import os')
        if import_pos != -1:
            insert_pos = content.find('\n', import_pos) + 1
            content = content[:insert_pos] + resource_function + content[insert_pos:]
        
        # 替换图标设置代码
        content = content.replace(old_icon_code, new_icon_code)
        
        # 保存修复后的代码
        with open('icon_generator_fixed.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ 修复后的源代码已创建: icon_generator_fixed.py")
        return True
        
    except Exception as e:
        print(f"❌ 创建修复源代码失败: {e}")
        return False

def build_fixed_exe():
    """构建修复版exe"""
    print("\n🔨 构建修复版exe...")
    
    # 清理构建文件夹
    print("🧹 清理构建文件...")
    for folder in ['build', 'dist']:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"✅ 清理文件夹: {folder}")
            except:
                pass
    
    # 删除旧的spec文件
    spec_files = [f for f in os.listdir('.') if f.endswith('.spec')]
    for spec_file in spec_files:
        try:
            os.remove(spec_file)
            print(f"✅ 删除: {spec_file}")
        except:
            pass
    
    # 构建命令
    cmd = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        '--name=IconGenerator_Fixed',
        '--clean',
        '--noconfirm',
        '--icon=assets/app_icon.ico',
        '--add-data=assets/window_icon.ico;assets',
        '--add-data=assets/menu_icons;assets/menu_icons',
        '--hidden-import=os'
    ]
    
    # 添加主文件
    cmd.append('icon_generator_fixed.py')
    
    print("\n📋 构建命令:")
    print(' '.join(cmd))
    print()
    
    try:
        # 执行构建
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        
        if result.returncode == 0:
            print("✅ 构建成功！")
            
            # 检查输出文件
            exe_path = 'dist/IconGenerator_Fixed.exe'
            if os.path.exists(exe_path):
                file_size = os.path.getsize(exe_path) / (1024*1024)  # MB
                print(f"📦 文件大小: {file_size:.1f} MB")
                
                # 复制到根目录
                shutil.copy2(exe_path, 'IconGenerator_Fixed.exe')
                print("📋 已复制到项目根目录")
                
                return True
            else:
                print("❌ 未找到生成的exe文件")
                return False
        else:
            print("❌ 构建失败")
            print("错误输出:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ 构建异常: {e}")
        return False

def test_fixed_exe():
    """测试修复版exe"""
    print("\n🧪 测试修复版exe...")
    
    exe_path = 'IconGenerator_Fixed.exe'
    if not os.path.exists(exe_path):
        print("❌ exe文件不存在")
        return False
    
    try:
        # 启动进程测试
        process = subprocess.Popen([exe_path], shell=True)
        time.sleep(3)  # 等待启动
        
        if process.poll() is None:
            print("✅ exe文件启动成功")
            print("💡 请检查:")
            print("   - 窗口左上角是否显示您的自定义图标")
            print("   - exe文件是否显示自定义图标")
            process.terminate()  # 关闭测试进程
            return True
        else:
            print("❌ exe文件启动失败")
            return False
            
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False

def create_icon_test():
    """创建图标测试程序"""
    test_code = '''#!/usr/bin/env python3
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
'''
    
    try:
        with open('icon_test.py', 'w', encoding='utf-8') as f:
            f.write(test_code)
        print("✅ 图标测试程序已创建: icon_test.py")
        return True
    except Exception as e:
        print(f"❌ 创建测试程序失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("🔧 图标路径修复工具")
    print("   解决打包后图标不显示的问题")
    print("   by 1Plabs.pro")
    print("=" * 60)
    
    # 检查必要文件
    required_files = [
        'stable_icon_generator_with_icons.py',
        'assets/window_icon.ico',
        'assets/app_icon.ico'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ 缺少必要文件:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return
    
    print("✅ 所有必要文件都存在")
    
    # 创建修复后的源代码
    if not create_fixed_source():
        return
    
    # 创建测试程序
    if not create_icon_test():
        return
    
    # 构建修复版exe
    if build_fixed_exe():
        print("\n🎉 修复版exe构建完成！")
        
        # 测试exe
        if test_fixed_exe():
            print("\n✅ 所有测试通过！")
            
            print("\n📦 生成的文件:")
            print("   - IconGenerator_Fixed.exe (修复版主程序)")
            print("   - dist/IconGenerator_Fixed.exe (备份)")
            print("   - icon_generator_fixed.py (修复版源码)")
            print("   - icon_test.py (图标测试程序)")
            
            print("\n🔧 修复内容:")
            print("   ✅ 修复了打包后图标路径问题")
            print("   ✅ 使用get_resource_path()函数获取正确路径")
            print("   ✅ 兼容开发环境和打包环境")
            print("   ✅ 包含完整的图标资源")
            
            print("\n🚀 使用方法:")
            print("   1. 测试图标: python icon_test.py")
            print("   2. 使用修复版: IconGenerator_Fixed.exe")
            print("   3. 检查窗口左上角的图标显示")
            
            print("\n💡 如果图标仍然不显示:")
            print("   - 检查assets/window_icon.ico文件格式")
            print("   - 确保图标文件是32x32的ICO格式")
            print("   - 尝试重新生成图标文件")
            
        else:
            print("\n⚠️  exe文件测试失败，但构建成功")
    else:
        print("\n❌ 构建失败")

if __name__ == "__main__":
    main()
