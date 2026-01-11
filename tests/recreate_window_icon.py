#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重新创建窗口图标
确保图标格式正确
"""

import os
from PIL import Image, ImageDraw

def create_window_icon():
    """创建高质量的窗口图标"""
    print("🎨 创建高质量窗口图标...")
    
    # 检查源图标
    source_icon = "assets/app_icon.png"
    if not os.path.exists(source_icon):
        print(f"❌ 源图标不存在: {source_icon}")
        return False
    
    try:
        # 打开源图标
        img = Image.open(source_icon)
        
        # 确保是正方形
        if img.size[0] != img.size[1]:
            size = min(img.size)
            left = (img.size[0] - size) // 2
            top = (img.size[1] - size) // 2
            img = img.crop((left, top, left + size, top + size))
        
        # 创建多个尺寸的图标
        sizes = [16, 32, 48, 64, 128, 256]
        icons = []
        
        for size in sizes:
            # 调整尺寸
            resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
            icons.append(resized_img)
            print(f"✅ 创建 {size}x{size} 图标")
        
        # 保存为ICO文件
        ico_path = "assets/window_icon.ico"
        icons[1].save(ico_path, format='ICO', sizes=[(size, size) for size in sizes])
        
        print(f"✅ 窗口图标已保存: {ico_path}")
        print(f"📏 包含尺寸: {sizes}")
        
        # 验证文件
        file_size = os.path.getsize(ico_path)
        print(f"📦 文件大小: {file_size} 字节")
        
        return True
        
    except Exception as e:
        print(f"❌ 创建窗口图标失败: {e}")
        return False

def create_simple_icon():
    """创建简单的测试图标"""
    print("🎨 创建简单测试图标...")
    
    try:
        # 创建32x32的简单图标
        size = 32
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # 绘制蓝色背景
        margin = 4
        draw.rectangle([margin, margin, size-margin, size-margin], 
                      fill=(52, 152, 219, 255), outline=(41, 128, 185, 255))
        
        # 绘制简单的"i"字母
        center = size // 2
        
        # 圆点
        dot_size = 4
        dot_y = center - 4
        draw.ellipse([center-dot_size//2, dot_y-dot_size//2, 
                     center+dot_size//2, dot_y+dot_size//2], 
                    fill=(255, 255, 255, 255))
        
        # 竖线
        line_width = 2
        line_height = 8
        line_y = dot_y + dot_size//2 + 2
        draw.rectangle([center-line_width//2, line_y, 
                      center+line_width//2, line_y+line_height], 
                     fill=(255, 255, 255, 255))
        
        # 保存ICO文件
        ico_path = "assets/window_icon_simple.ico"
        img.save(ico_path, format='ICO')
        
        print(f"✅ 简单窗口图标已创建: {ico_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ 创建简单图标失败: {e}")
        return False

def test_icon_file():
    """测试图标文件"""
    print("\n🧪 测试图标文件...")
    
    icon_files = [
        "assets/window_icon.ico",
        "assets/window_icon_simple.ico"
    ]
    
    for icon_file in icon_files:
        if os.path.exists(icon_file):
            try:
                img = Image.open(icon_file)
                print(f"✅ {icon_file}: 格式正确，尺寸: {img.size}")
            except Exception as e:
                print(f"❌ {icon_file}: 格式错误 - {e}")
        else:
            print(f"❌ {icon_file}: 文件不存在")

def main():
    """主函数"""
    print("=" * 50)
    print("🎨 窗口图标重新创建工具")
    print("   by 1Plabs.pro")
    print("=" * 50)
    
    # 创建高质量图标
    if create_window_icon():
        print("\n✅ 高质量窗口图标创建成功")
    
    # 创建简单测试图标
    if create_simple_icon():
        print("✅ 简单测试图标创建成功")
    
    # 测试图标文件
    test_icon_file()
    
    print("\n🎯 图标创建完成！")
    print("\n📁 生成的文件:")
    print("   - assets/window_icon.ico (高质量)")
    print("   - assets/window_icon_simple.ico (简单测试)")
    
    print("\n💡 使用方法:")
    print("   1. 测试图标: python icon_test.py")
    print("   2. 如果高质量图标不显示，尝试简单图标")
    print("   3. 重新构建exe: python fix_icon_paths.py")

if __name__ == "__main__":
    main()
