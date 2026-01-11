# iOS & Android 图标生成器

一个简单易用的Python工具，用于生成iOS和Android应用所需的各种尺寸图标。

## 功能特点

- 🎯 **一键生成**：自动生成iOS和Android平台所需的所有图标尺寸
- 🎨 **圆角设置**：可自定义圆角半径（0-50%）
- 🖼️ **边框设置**：可添加自定义颜色和宽度的边框
- 📱 **平台支持**：同时支持iOS和Android图标规范
- 📄 **XML生成**：自动生成Android adaptive icon XML文件
- 🌍 **多语言支持**：自动检测系统语言，支持简体中文和英文
- 🖥️ **图形界面**：直观的GUI界面，操作简单
- 📁 **自动分类**：生成的图标按平台自动分类保存

## 安装要求

- Python 3.7+
- Pillow 10.0.1

## 安装步骤

1. 克隆或下载本项目
2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 运行程序：
```bash
python icon_generator.py
```

2. **选择源图片**：
   - 点击"选择图片"按钮选择一张正方形图片作为图标源
   - 支持格式：PNG、JPG、JPEG、GIF、BMP

3. **选择平台**：
   - 勾选需要生成的平台（iOS、Android）
   - 可以同时选择两个平台

4. **设置样式**：
   - **圆角**：勾选"启用圆角"，调整圆角半径百分比
   - **边框**：勾选"启用边框"，设置边框宽度和颜色

5. **Android XML选项**：
   - 勾选"生成Android XML文件"可自动生成adaptive icon所需的XML文件

6. **选择输出目录**：
   - 默认输出到当前目录下的 `generated_icons` 文件夹
   - 可以点击"浏览"选择其他目录

7. **生成图标**：
   - 点击"生成图标"按钮
   - 等待处理完成

## 语言支持

### 自动语言检测
- 程序启动时会自动检测系统语言
- 简体中文系统显示中文界面
- 其他语言系统显示英文界面

### 手动切换语言
- 点击菜单栏的"语言"选项
- 选择"简体中文"或"English"切换界面语言
- 切换后界面会立即刷新

## 生成的图标尺寸

### iOS图标
- iPhone App (60pt): 120x120, 180x180
- iPad App (76pt): 152x152, 167x167
- iPad Pro App (83.5pt): 167x167
- Settings (29pt): 58x58, 87x87
- Spotlight (40pt): 80x80, 120x120
- App Store (1024pt): 1024x1024

### Android图标
- mipmap-mdpi: 48x48
- mipmap-hdpi: 72x72
- mipmap-xhdpi: 96x96
- mipmap-xxhdpi: 144x144
- mipmap-xxxhdpi: 192x192
- Google Play: 512x512

### Android XML文件
如果勾选"生成Android XML文件"选项，还会生成：
- `mipmap-anydpi-v26/ic_launcher.xml`
- `mipmap-anydpi-v26/ic_launcher_round.xml`

这些XML文件用于Android 8.0+的adaptive icon功能。

## 输出结构

```
generated_icons/
├── iOS/
│   ├── iPhone App (60pt)_120x120.png
│   ├── iPhone App (60pt)_180x180.png
│   ├── iPad App (76pt)_152x152.png
│   └── ...
└── Android/
    ├── mipmap-mdpi_48x48.png
    ├── mipmap-hdpi_72x72.png
    ├── mipmap-xhdpi_96x96.png
    ├── mipmap-xxhdpi_144x144.png
    ├── mipmap-xxxhdpi_192x192.png
    ├── Google Play_512x512.png
    └── mipmap-anydpi-v26/
        ├── ic_launcher.xml
        └── ic_launcher_round.xml
```

## 注意事项

- 建议使用高分辨率的正方形图片作为源图片
- 源图片会自动裁剪为正方形
- 生成的图标均为PNG格式，支持透明背景
- 边框颜色使用十六进制格式，如 #000000
- Android XML文件适用于Android 8.0+的adaptive icon功能
- XML文件引用的`ic_launcher_background`和`ic_launcher_foreground`需要另外准备

## 常见问题

**Q: 为什么生成的图标模糊？**
A: 请使用高分辨率的源图片，建议至少1024x1024像素。

**Q: 可以批量处理多张图片吗？**
A: 当前版本一次只能处理一张图片，需要多次运行程序。

**Q: 支持哪些图片格式？**
A: 支持PNG、JPG、JPEG、GIF、BMP格式。

**Q: Android XML文件有什么用？**
A: XML文件用于Android 8.0+的adaptive icon功能，可以让图标在不同设备上显示效果更好。

**Q: 生成的XML文件可以直接使用吗？**
A: XML文件是模板文件，引用了`ic_launcher_background`和`ic_launcher_foreground`，您需要根据实际项目调整这些引用。

**Q: 如何切换界面语言？**
A: 点击菜单栏的"语言"选项，选择"简体中文"或"English"即可切换。

**Q: 程序支持哪些语言？**
A: 目前支持简体中文和英文。程序会自动检测系统语言，中文系统显示中文，其他系统显示英文。

## 许可证

MIT License
