#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试exe文件是否正常工作
"""

import subprocess
import os
import time

def test_exe(exe_name):
    """测试指定的exe文件"""
    print(f"正在测试 {exe_name}...")
    
    if not os.path.exists(exe_name):
        print(f"  ❌ 文件不存在: {exe_name}")
        return False
    
    try:
        # 启动exe文件
        process = subprocess.Popen([exe_name], shell=True)
        
        # 等待3秒
        time.sleep(3)
        
        # 检查进程是否还在运行
        if process.poll() is None:
            print(f"  ✅ {exe_name} 启动成功，正在运行")
            # 终止进程
            process.terminate()
            return True
        else:
            print(f"  ❌ {exe_name} 启动失败或已退出")
            return False
            
    except Exception as e:
        print(f"  ❌ {exe_name} 测试失败: {e}")
        return False

def main():
    """主函数"""
    print("=== EXE文件测试 ===")
    print()
    
    exe_files = [
        "iOS_Android_Icon_Generator.exe",
        "iOS_Android_Icon_Generator_Fixed.exe", 
        "iOS_Android_Icon_Generator_Simple.exe"
    ]
    
    results = {}
    
    for exe in exe_files:
        results[exe] = test_exe(exe)
        print()
    
    print("=== 测试结果 ===")
    for exe, success in results.items():
        status = "✅ 成功" if success else "❌ 失败"
        print(f"{exe}: {status}")
    
    print()
    print("推荐使用：")
    if results.get("iOS_Android_Icon_Generator_Simple.exe"):
        print("🎯 iOS_Android_Icon_Generator_Simple.exe (稳定版，无拖拽功能)")
    elif results.get("iOS_Android_Icon_Generator_Fixed.exe"):
        print("🎯 iOS_Android_Icon_Generator_Fixed.exe (修复版)")
    elif results.get("iOS_Android_Icon_Generator.exe"):
        print("🎯 iOS_Android_Icon_Generator.exe (原版)")
    else:
        print("❌ 所有版本都有问题")

if __name__ == "__main__":
    main()
