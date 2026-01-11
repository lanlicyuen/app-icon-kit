# 构建EXE文件说明

## 方法一：快速构建（推荐）

1. 运行快速构建脚本：
```bash
python quick_build.py
```

2. 构建完成后，exe文件将生成在：
   - 项目根目录：`iOS_Android_Icon_Generator.exe`
   - dist目录：`dist/iOS_Android_Icon_Generator.exe`

## 方法二：完整构建

1. 创建应用图标（可选）：
```bash
python create_icon.py
```

2. 运行完整构建脚本：
```bash
python build_exe.py
```

## 方法三：手动构建

1. 安装依赖：
```bash
pip install pyinstaller pillow tkinterdnd2
```

2. 构建exe：
```bash
pyinstaller --onefile --windowed --name=iOS_Android_Icon_Generator icon_generator.py
```

## 构建参数说明

- `--onefile`: 打包成单个exe文件
- `--windowed`: 不显示控制台窗口
- `--name`: 指定exe文件名
- `--icon`: 指定图标文件（可选）

## 注意事项

1. **首次构建**：可能需要下载依赖，请确保网络连接正常
2. **杀毒软件**：某些杀毒软件可能误报，请添加信任
3. **文件大小**：exe文件约20-30MB，这是正常的
4. **运行环境**：生成的exe可在Windows 7+系统运行

## 故障排除

### 问题1：找不到模块
```
解决方案：在构建命令中添加 --hidden-import=模块名
```

### 问题2：tkinterdnd2相关错误
```
解决方案：确保已安装tkinterdnd2
pip install tkinterdnd2
```

### 问题3：构建失败
```
解决方案：清理构建缓存
rmdir /s build dist spec
然后重新构建
```

## 分发说明

构建完成后，您会得到：
- `iOS_Android_Icon_Generator.exe` - 主程序
- 可直接分发给用户使用，无需安装Python环境

## 更新版本

修改代码后，重新运行构建脚本即可生成新版本。
