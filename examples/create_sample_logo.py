#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建示例Logo图片
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_sample_logo():
    """创建一个示例Logo"""
    # 创建1024x1024的图像
    size = 1024
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 绘制背景圆
    margin = 100
    draw.ellipse(
        [(margin, margin), (size - margin, size - margin)],
        fill=(52, 152, 219, 255),  # 蓝色背景
        outline=(41, 128, 185, 255),  # 深蓝色边框
        width=20
    )
    
    # 绘制图标符号（简化的"i"字母设计）
    center = size // 2
    
    # 绘制圆点
    dot_size = 120
    dot_y = center - 100
    draw.ellipse(
        [(center - dot_size//2, dot_y - dot_size//2), 
         (center + dot_size//2, dot_y + dot_size//2)],
        fill=(255, 255, 255, 255)
    )
    
    # 绘制竖线
    line_width = 80
    line_height = 300
    line_y = dot_y + dot_size//2 + 50
    draw.rectangle(
        [(center - line_width//2, line_y), 
         (center + line_width//2, line_y + line_height)],
        fill=(255, 255, 255, 255)
    )
    
    # 添加文字（可选）
    try:
        # 尝试使用系统字体
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        # 如果找不到字体，使用默认字体
        font = ImageFont.load_default()
    
    text = "ICON"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size - text_width) // 2
    y = size - 150
    draw.text((x, y), text, fill=(255, 255, 255, 200), font=font)
    
    # 保存文件
    img.save('sample_logo_1024x1024.png', 'PNG')
    print("示例Logo已创建：sample_logo_1024x1024.png")
    
    # 创建小尺寸预览
    preview_sizes = [512, 256, 128, 64, 32]
    for preview_size in preview_sizes:
        preview = img.resize((preview_size, preview_size), Image.Resampling.LANCZOS)
        preview.save(f'sample_logo_{preview_size}x{preview_size}.png', 'PNG')
        print(f"预览图已创建：sample_logo_{preview_size}x{preview_size}.png")

if __name__ == "__main__":
    create_sample_logo()
