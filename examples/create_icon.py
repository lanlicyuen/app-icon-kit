#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建应用图标
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    """创建应用图标"""
    # 创建256x256的图像
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 绘制背景圆角矩形
    corner_radius = 40
    draw.rounded_rectangle(
        [(0, 0), (size, size)],
        radius=corner_radius,
        fill=(41, 128, 185, 255),  # 蓝色背景
        outline=(52, 152, 219, 255),  # 亮蓝色边框
        width=8
    )
    
    # 绘制iOS图标（简化版）
    ios_color = (255, 255, 255, 255)
    # iOS图标轮廓
    draw.ellipse([(50, 60), (110, 120)], outline=ios_color, width=4)
    # iOS图标内部
    draw.ellipse([(65, 75), (95, 105)], fill=ios_color)
    
    # 绘制Android机器人（简化版）
    android_color = (255, 255, 255, 255)
    # Android头部
    draw.ellipse([(146, 60), (206, 120)], outline=android_color, width=4)
    # Android眼睛
    draw.ellipse([(160, 75), (170, 85)], fill=android_color)
    draw.ellipse([(182, 75), (192, 85)], fill=android_color)
    # Android天线
    draw.line([(165, 60), (160, 45)], fill=android_color, width=4)
    draw.line([(187, 60), (192, 45)], fill=android_color, width=4)
    
    # 添加文字
    try:
        # 尝试使用系统字体
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        # 如果找不到字体，使用默认字体
        font = ImageFont.load_default()
    
    text = "ICON"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size - text_width) // 2
    y = size - 50
    draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)
    
    # 保存为ICO文件
    img.save('icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
    print("图标文件创建完成：icon.ico")

if __name__ == "__main__":
    create_icon()
