#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
准备源代码包
整理项目文件，准备上传到GitHub
"""

import os
import shutil
import zipfile
from datetime import datetime

def create_source_structure():
    """创建源代码目录结构"""
    print("📁 创建源代码目录结构...")
    
    # 创建源代码目录
    source_dir = "app-icon-kit-source"
    if os.path.exists(source_dir):
        shutil.rmtree(source_dir)
    
    os.makedirs(source_dir)
    
    # 创建子目录
    subdirs = [
        "src",
        "assets",
        "build",
        "docs",
        "examples",
        "tests"
    ]
    
    for subdir in subdirs:
        os.makedirs(os.path.join(source_dir, subdir))
    
    print(f"✅ 源代码目录已创建: {source_dir}")
    return source_dir

def copy_source_files(source_dir):
    """复制源代码文件"""
    print("📋 复制源代码文件...")
    
    # 主要源代码文件
    source_files = {
        "src/": [
            "icon_generator.py",
            "stable_icon_generator.py", 
            "stable_icon_generator_with_icons.py",
            "icon_generator_fixed.py",
            "icon_generator_final.py"
        ],
        "build/": [
            "build_exe.py",
            "build_with_icon.py",
            "build_stable.py",
            "build_with_icons.py",
            "build_final_icon.py",
            "rebuild_exe.py",
            "quick_build.py",
            "fixed_build.py",
            "simple_build.py"
        ],
        "docs/": [
            "README.md",
            "FINAL_GUIDE.md",
            "PROJECT_COMPLETE.md",
            "STABLE_VERSION_GUIDE.md",
            "ICON_COMPLETE.md",
            "ICON_GUIDE.md",
            "FINAL_ICON_SOLUTION.md",
            "WINDOWS_ICO_GUIDE.md",
            "BUILD_README.md"
        ],
        "examples/": [
            "create_icon.py",
            "create_sample_logo.py",
            "icon_demo.py",
            "icon_test.py",
            "test_exe.py"
        ],
        "tests/": [
            "recreate_window_icon.py",
            "fix_icon_paths.py",
            "final_icon_solution.py",
            "icon_setup.py",
            "prepare_source.py"
        ]
    }
    
    # 复制文件
    for target_dir, files in source_files.items():
        full_target_dir = os.path.join(source_dir, target_dir)
        for file in files:
            if os.path.exists(file):
                shutil.copy2(file, os.path.join(full_target_dir, file))
                print(f"✅ 复制: {file} -> {target_dir}")
            else:
                print(f"⚠️  文件不存在: {file}")
    
    # 复制assets目录
    if os.path.exists("assets"):
        target_assets = os.path.join(source_dir, "assets")
        for item in os.listdir("assets"):
            s = os.path.join("assets", item)
            d = os.path.join(target_assets, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)
        print("✅ 复制: assets/ 目录")

def create_readme(source_dir):
    """创建README文件"""
    print("📝 创建README文件...")
    
    readme_content = '''# App Icon Kit

一个专业的iOS、Android、Windows图标生成工具

## 🎯 功能特点

- ✅ **三平台支持**: iOS、Android、Windows图标一键生成
- ✅ **自定义图标**: 支持自定义应用图标
- ✅ **界面优化**: 底部控件固定，布局合理
- ✅ **拖拽上传**: 支持图片拖拽功能（部分版本）
- ✅ **多语言**: 中文/英文界面切换
- ✅ **界面缩放**: 4种界面缩放比例
- ✅ **样式定制**: 圆角、边框、颜色设置

## 📦 项目结构

```
app-icon-kit/
├── src/                    # 源代码
│   ├── icon_generator.py           # 主程序（带拖拽）
│   ├── stable_icon_generator.py    # 稳定版本（无拖拽）
│   └── icon_generator_fixed.py     # 修复版本
├── build/                  # 构建脚本
│   ├── build_with_icons.py         # 带图标构建
│   ├── build_stable.py             # 稳定版构建
│   └── rebuild_exe.py              # 重新构建
├── assets/                 # 图标资源
│   ├── app_icon.ico               # exe文件图标
│   ├── window_icon.ico            # 窗口图标
│   └── menu_icons/                # 菜单图标
├── docs/                   # 文档
│   ├── README.md                  # 项目说明
│   ├── FINAL_GUIDE.md             # 使用指南
│   └── ICON_COMPLETE.md           # 图标配置
├── examples/               # 示例和测试
│   ├── create_sample_logo.py      # 创建示例图标
│   └── icon_demo.py               # 图标演示
└── tests/                  # 测试和工具
    ├── icon_setup.py              # 图标配置
    └── recreate_window_icon.py    # 重新创建图标
```

## 🚀 快速开始

### 方法一：使用预构建版本

1. 下载最新的exe文件
2. 双击运行 `IconGenerator_FinalIcon.exe`
3. 选择图片，选择平台，生成图标

### 方法二：从源代码构建

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 配置图标：
```bash
python tests/icon_setup.py
```

3. 构建exe：
```bash
python build/build_with_icons.py
```

## 🎨 图标配置

### 准备图标文件
- 将您的1024x1024 PNG图标命名为 `app_icon.png`
- 放入 `assets/` 文件夹

### 自动配置
```bash
python tests/icon_setup.py
```

### 手动配置
```
assets/
├── app_icon.png          # 主图标(1024x1024)
├── app_icon.ico          # exe文件图标
├── window_icon.ico       # 窗口图标
└── menu_icons/           # 菜单图标
    ├── menu_icon_16x16.png
    ├── menu_icon_24x24.png
    └── menu_icon_32x32.png
```

## 📱 支持的平台

### iOS
- iPhone App (60pt): 120x120, 180x180
- iPad App (76pt): 152x152, 167x167
- iPad Pro App (83.5pt): 167x167
- Settings (29pt): 58x58, 87x87
- Spotlight (40pt): 80x80, 120x120
- App Store (1024pt): 1024x1024

### Android
- mipmap-mdpi: 48x48
- mipmap-hdpi: 72x72
- mipmap-xhdpi: 96x96
- mipmap-xxhdpi: 144x144
- mipmap-xxxhdpi: 192x192
- Google Play: 512x512

### Windows
- Small (16x16): 16x16
- Medium (32x32): 32x32
- Large (48x48): 48x48
- Extra Large (64x64): 64x64
- Very Large (96x96): 96x96
- Extra Very Large (128x128): 128x128
- Huge (256x256): 256x256
- Extra Huge (512x512): 512x512

## 🔧 系统要求

- **操作系统**: Windows 7及以上
- **Python**: 3.8及以上（构建时需要）
- **依赖库**: 
  - tkinter（Python内置）
  - Pillow
  - PyInstaller（构建时需要）

## 📋 版本说明

| 版本 | 文件名 | 特点 | 推荐度 |
|------|--------|------|--------|
| 🏆 **最终版** | IconGenerator_FinalIcon.exe | 完整图标，路径修复 | ⭐⭐⭐⭐⭐ |
| 🛡️ 稳定版 | IconGenerator_Stable.exe | 无拖拽，最稳定 | ⭐⭐⭐⭐⭐ |
| 🔄 完整版 | IconGenerator_Complete.exe | 功能完整 | ⭐⭐⭐ |
| 📱 简化版 | iOS_Android_Icon_Generator_Simple.exe | 基础功能 | ⭐⭐⭐ |

## 🎯 使用方法

1. **启动程序**: 双击exe文件
2. **选择图片**: 点击"选择图片"或拖拽图片
3. **选择平台**: 勾选需要生成的平台
4. **设置样式**: 调整圆角和边框（可选）
5. **生成图标**: 点击"生成图标"按钮

## ⚠️ 注意事项

- 使用1024x1024高分辨率图片获得最佳效果
- 确保有足够的磁盘空间存储生成的图标
- 首次运行可能需要防病毒软件添加信任

## 🆘 故障排除

### 常见问题

**Q: 程序无法启动？**
A: 检查防病毒软件设置，添加到信任列表

**Q: 图标不显示？**
A: 运行 `python tests/icon_setup.py` 重新配置图标

**Q: 生成的图标模糊？**
A: 使用1024x1024高分辨率源图片

**Q: 拖拽功能不工作？**
A: 使用稳定版本 `IconGenerator_Stable.exe`

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 👨‍💻 作者

**1Plabs.pro** - 专业的软件开发工具提供商

---

**技术支持: 1Plabs.pro**  
**最后更新: 2026年1月11日**
'''
    
    with open(os.path.join(source_dir, "README.md"), 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("✅ README.md 已创建")

def create_requirements(source_dir):
    """创建requirements.txt"""
    print("📦 创建requirements.txt...")
    
    requirements = '''# App Icon Kit - 依赖库

# 图像处理
Pillow>=10.0.0

# GUI界面（Python内置，无需安装）
# tkinter

# 打包工具
PyInstaller>=6.0.0

# 可选：拖拽支持
# tkinterdnd2>=0.3.0  # 可选，可能有兼容性问题

# 开发工具（可选）
# pytest>=7.0.0      # 测试框架
# black>=23.0.0       # 代码格式化
# flake8>=6.0.0       # 代码检查
'''
    
    with open(os.path.join(source_dir, "requirements.txt"), 'w', encoding='utf-8') as f:
        f.write(requirements)
    
    print("✅ requirements.txt 已创建")

def create_gitignore(source_dir):
    """创建.gitignore文件"""
    print("📝 创建.gitignore...")
    
    gitignore_content = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# 单元测试
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# 环境变量
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# 操作系统
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# 项目特定
generated_icons/
*.exe
build/
dist/

# 临时文件
*.tmp
*.temp
*.log
'''
    
    with open(os.path.join(source_dir, ".gitignore"), 'w', encoding='utf-8') as f:
        f.write(gitignore_content)
    
    print("✅ .gitignore 已创建")

def create_license(source_dir):
    """创建许可证文件"""
    print("📄 创建许可证...")
    
    license_content = '''MIT License

Copyright (c) 2026 1Plabs.pro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
    
    with open(os.path.join(source_dir, "LICENSE"), 'w', encoding='utf-8') as f:
        f.write(license_content)
    
    print("✅ LICENSE 已创建")

def create_source_zip(source_dir):
    """创建源代码zip文件"""
    print("📦 创建源代码zip文件...")
    
    # 创建zip文件
    zip_filename = f"app-icon-kit-source-{datetime.now().strftime('%Y%m%d-%H%M%S')}.zip"
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
    
    file_size = os.path.getsize(zip_filename) / (1024*1024)  # MB
    print(f"✅ 源代码zip已创建: {zip_filename}")
    print(f"📦 文件大小: {file_size:.1f} MB")
    
    return zip_filename

def main():
    """主函数"""
    print("=" * 60)
    print("📦 App Icon Kit - 源代码整理工具")
    print("   准备上传到GitHub")
    print("   by 1Plabs.pro")
    print("=" * 60)
    
    # 创建源代码目录结构
    source_dir = create_source_structure()
    
    # 复制源代码文件
    copy_source_files(source_dir)
    
    # 创建项目文件
    create_readme(source_dir)
    create_requirements(source_dir)
    create_gitignore(source_dir)
    create_license(source_dir)
    
    # 创建zip文件
    zip_file = create_source_zip(source_dir)
    
    print("\n🎉 源代码整理完成！")
    print("\n📁 生成的文件:")
    print(f"   📂 {source_dir}/ - 源代码目录")
    print(f"   📦 {zip_file} - 源代码zip文件")
    
    print("\n📋 目录结构:")
    print("   app-icon-kit-source/")
    print("   ├── src/           # 源代码")
    print("   ├── build/         # 构建脚本")
    print("   ├── assets/        # 图标资源")
    print("   ├── docs/          # 文档")
    print("   ├── examples/      # 示例")
    print("   ├── tests/         # 测试工具")
    print("   ├── README.md      # 项目说明")
    print("   ├── requirements.txt # 依赖列表")
    print("   ├── .gitignore     # Git忽略文件")
    print("   └── LICENSE        # 许可证")
    
    print("\n🚀 GitHub上传步骤:")
    print("   1. cd app-icon-kit-source")
    print("   2. git init")
    print("   3. git add .")
    print("   4. git commit -m 'Initial commit'")
    print("   5. git branch -M main")
    print("   6. git remote add origin https://github.com/lanlicyuen/app-icon-kit.git")
    print("   7. git push -u origin main")
    
    print("\n💡 提示:")
    print("   - 源代码已整理成标准项目结构")
    print("   - 包含完整的文档和示例")
    print("   - 可以直接上传到GitHub")
    print("   - zip文件可用于备份或分享")

if __name__ == "__main__":
    main()
