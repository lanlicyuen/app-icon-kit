import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk
import os
import shutil
import locale
import json
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    DRAG_DROP_ENABLED = True
except ImportError:
    DRAG_DROP_ENABLED = False

class LanguageManager:
    """语言管理器"""
    def __init__(self):
        self.current_language = self.detect_system_language()
        self.translations = {
            'zh_CN': {
                'title': 'iOS & Android & Windows 图标生成器 by 1Plabs.pro',
                'select_image': '选择源图片:',
                'please_select_image': '请选择一张正方形图片',
                'select_image_btn': '选择图片',
                'clear_image_btn': '清除图片',
                'select_platform': '选择平台:',
                'ios': 'iOS',
                'android': 'Android',
                'windows': 'Windows',
                'generate_xml': '生成Android XML文件',
                'style_settings': '样式设置:',
                'enable_corner': '启用圆角',
                'corner_radius': '圆角半径:',
                'enable_border': '启用边框',
                'border_width': '边框宽度:',
                'border_color': '边框颜色:',
                'output_dir': '输出目录:',
                'browse': '浏览',
                'generate_icons': '生成图标',
                'ready': '就绪',
                'generating': '正在生成图标...',
                'completed': '完成！已生成 {} 个图标',
                'failed': '生成失败',
                'image_loaded': '图片已加载',
                'error': '错误',
                'success': '成功',
                'select_image_first': '请先选择源图片',
                'select_platform_first': '请至少选择一个平台',
                'cannot_load_image': '无法加载图片: {}',
                'generation_complete': '图标生成完成！\n共生成 {} 个图标\n保存在: {}',
                'generation_error': '生成图标时出错: {}',
                'border_color_error': '边框颜色格式错误，请使用十六进制格式如 #000000',
                'language': '语言',
                'chinese': '简体中文',
                'english': 'English',
                'scale': '缩放',
                'scale_100': '100%',
                'scale_125': '100%+25%',
                'scale_150': '100%+50%',
                'scale_175': '100%+75%'
            },
            'en': {
                'title': 'iOS & Android & Windows Icon Generator by 1Plabs.pro',
                'select_image': 'Select Source Image:',
                'please_select_image': 'Please select a square image',
                'select_image_btn': 'Select Image',
                'clear_image_btn': 'Clear Image',
                'select_platform': 'Select Platform:',
                'ios': 'iOS',
                'android': 'Android',
                'windows': 'Windows',
                'generate_xml': 'Generate Android XML Files',
                'style_settings': 'Style Settings:',
                'enable_corner': 'Enable Corner Radius',
                'corner_radius': 'Corner Radius:',
                'enable_border': 'Enable Border',
                'border_width': 'Border Width:',
                'border_color': 'Border Color:',
                'output_dir': 'Output Directory:',
                'browse': 'Browse',
                'generate_icons': 'Generate Icons',
                'ready': 'Ready',
                'generating': 'Generating icons...',
                'completed': 'Completed! Generated {} icons',
                'failed': 'Generation Failed',
                'image_loaded': 'Image loaded',
                'error': 'Error',
                'success': 'Success',
                'select_image_first': 'Please select an image first',
                'select_platform_first': 'Please select at least one platform',
                'cannot_load_image': 'Cannot load image: {}',
                'generation_complete': 'Icon generation completed!\nGenerated {} icons\nSaved to: {}',
                'generation_error': 'Error generating icons: {}',
                'border_color_error': 'Border color format error, please use hexadecimal format like #000000',
                'language': 'Language',
                'chinese': '简体中文',
                'english': 'English',
                'scale': 'Scale',
                'scale_100': '100%',
                'scale_125': '100%+25%',
                'scale_150': '100%+50%',
                'scale_175': '100%+75%'
            }
        }
    
    def detect_system_language(self):
        """检测系统语言"""
        try:
            system_lang = locale.getdefaultlocale()[0]
            if system_lang and system_lang.startswith('zh'):
                return 'zh_CN'
            else:
                return 'en'
        except:
            return 'en'
    
    def get_text(self, key):
        """获取当前语言的文本"""
        return self.translations.get(self.current_language, {}).get(key, key)
    
    def switch_language(self, lang_code):
        """切换语言"""
        if lang_code in self.translations:
            self.current_language = lang_code
            return True
        return False

class IconGenerator:
    def __init__(self, root):
        self.root = root
        self.lang_manager = LanguageManager()
        
        # 如果支持拖拽，则设置拖拽
        if DRAG_DROP_ENABLED:
            # 创建菜单栏
            self.create_menu()
            
            self.root.title(self.lang_manager.get_text('title'))
            self.root.resizable(True, True)  # 允许调整窗口大小
            self.root.minsize(700, 800)  # 设置最小尺寸
            self.root.maxsize(1700, 1800)  # 设置最大尺寸
            self.current_scale_factor = 1.0  # 初始化缩放因子
            self.base_width = 700
            self.base_height = 800
            # 启动时使用最小尺寸
            self.root.geometry(f"{self.base_width}x{self.base_height}")
            self.center_window()
        else:
            # 创建菜单栏
            self.create_menu()
            
            self.root.title(self.lang_manager.get_text('title'))
            self.root.resizable(True, True)  # 允许调整窗口大小
            self.root.minsize(700, 800)  # 设置最小尺寸
            self.root.maxsize(1700, 1800)  # 设置最大尺寸
            self.current_scale_factor = 1.0  # 初始化缩放因子
            self.base_width = 700
            self.base_height = 800
            # 启动时使用最小尺寸
            self.root.geometry(f"{self.base_width}x{self.base_height}")
            self.center_window()
        
        self.source_image = None
        self.source_image_path = None
        
        # iOS图标尺寸规范
        self.ios_sizes = {
            "iPhone App (60pt)": [120, 180],
            "iPad App (76pt)": [152, 167],
            "iPad Pro App (83.5pt)": [167],
            "Settings (29pt)": [58, 87],
            "Spotlight (40pt)": [80, 120],
            "App Store (1024pt)": [1024]
        }
        
        # Android图标尺寸规范
        self.android_sizes = {
            "mipmap-mdpi": [48],
            "mipmap-hdpi": [72],
            "mipmap-xhdpi": [96],
            "mipmap-xxhdpi": [144],
            "mipmap-xxxhdpi": [192],
            "Google Play": [512]
        }
        
        # Windows图标尺寸规范
        self.windows_sizes = {
            "Small (16x16)": [16],
            "Medium (32x32)": [32],
            "Large (48x48)": [48],
            "Extra Large (64x64)": [64],
            "Very Large (96x96)": [96],
            "Extra Very Large (128x128)": [128],
            "Huge (256x256)": [256],
            "Extra Huge (512x512)": [512]
        }
        
        # XML生成选项
        self.generate_xml = tk.BooleanVar(value=True)
        
        self.setup_ui()
    
    def center_window(self):
        """将窗口居中显示在屏幕上"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_menu(self):
        """创建菜单栏"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # 语言菜单
        language_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.lang_manager.get_text('language'), menu=language_menu)
        
        # 中文选项
        language_menu.add_command(
            label=self.lang_manager.get_text('chinese'),
            command=lambda: self.switch_language('zh_CN')
        )
        
        # 英文选项
        language_menu.add_command(
            label=self.lang_manager.get_text('english'),
            command=lambda: self.switch_language('en')
        )
        
        # 缩放菜单
        scale_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.lang_manager.get_text('scale'), menu=scale_menu)
        
        # 缩放选项
        scale_menu.add_command(
            label=self.lang_manager.get_text('scale_100'),
            command=lambda: self.apply_scale(1.0)
        )
        scale_menu.add_command(
            label=self.lang_manager.get_text('scale_125'),
            command=lambda: self.apply_scale(1.25)
        )
        scale_menu.add_command(
            label=self.lang_manager.get_text('scale_150'),
            command=lambda: self.apply_scale(1.5)
        )
        scale_menu.add_command(
            label=self.lang_manager.get_text('scale_175'),
            command=lambda: self.apply_scale(1.75)
        )
    
    def switch_language(self, lang_code):
        """切换语言并刷新界面"""
        if self.lang_manager.switch_language(lang_code):
            # 清除当前界面
            for widget in self.root.winfo_children():
                if not isinstance(widget, tk.Menu):
                    widget.destroy()
            
            # 重新创建菜单和界面
            self.create_menu()
            self.root.title(self.lang_manager.get_text('title'))
            self.setup_ui()
    
    def apply_scale(self, scale_factor):
        """应用缩放因子"""
        self.current_scale_factor = scale_factor
        
        # 计算新的窗口尺寸
        new_width = int(self.base_width * scale_factor)
        new_height = int(self.base_height * scale_factor)
        
        # 应用新的窗口尺寸
        self.root.geometry(f"{new_width}x{new_height}")
        
        # 重新居中窗口
        self.center_window()
        
        # 重新构建界面以应用新的字体大小
        self.rebuild_ui()
    
    def rebuild_ui(self):
        """重新构建界面以应用缩放"""
        # 清除当前界面（保留菜单）
        for widget in self.root.winfo_children():
            if not isinstance(widget, tk.Menu):
                widget.destroy()
        
        # 重新构建界面
        self.setup_ui()
    
    def get_scaled_font_size(self, base_size):
        """获取缩放后的字体大小"""
        return int(base_size * self.current_scale_factor)
    
    def update_ui_text(self):
        """更新界面文本"""
        self.root.title(self.lang_manager.get_text('title'))
        # 这里可以添加更多需要更新的文本元素
    
    def setup_ui(self):
        # 配置窗口权重
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # 主容器
        main_container = ttk.Frame(self.root)
        main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        
        # 可滚动内容区域
        canvas = tk.Canvas(main_container)
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # 配置滚动区域
        canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        main_container.grid_columnconfigure(0, weight=1)
        main_container.grid_rowconfigure(0, weight=1)
        
        # 配置scrollable_frame的列权重
        scrollable_frame.grid_columnconfigure(0, weight=1)
        scrollable_frame.grid_columnconfigure(1, weight=1)
        
        # 源图片选择
        ttk.Label(scrollable_frame, text=self.lang_manager.get_text('select_image'), font=("Arial", self.get_scaled_font_size(12), "bold")).grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        self.image_frame = ttk.Frame(scrollable_frame, relief=tk.SUNKEN, borderwidth=2)
        self.image_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
        
        self.image_label = ttk.Label(self.image_frame, text=self.lang_manager.get_text('please_select_image'), width=50, padding="30", anchor="center")
        self.image_label.pack(expand=True, fill=tk.BOTH)
        
        # 添加拖拽功能
        if DRAG_DROP_ENABLED:
            self.image_label.drop_target_register(DND_FILES)
            self.image_label.dnd_bind('<<Drop>>', self.on_drop)
        
        ttk.Button(scrollable_frame, text=self.lang_manager.get_text('select_image_btn'), command=self.select_image).grid(row=2, column=0, pady=5, sticky=tk.W, padx=5)
        ttk.Button(scrollable_frame, text=self.lang_manager.get_text('clear_image_btn'), command=self.clear_image).grid(row=2, column=1, pady=5, sticky=tk.E, padx=5)
        
        # 分隔线
        ttk.Separator(scrollable_frame, orient=tk.HORIZONTAL).grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # 平台选择
        ttk.Label(scrollable_frame, text=self.lang_manager.get_text('select_platform'), font=("Arial", self.get_scaled_font_size(12), "bold")).grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        self.platform_frame = ttk.Frame(scrollable_frame)
        self.platform_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
        
        self.ios_var = tk.BooleanVar(value=True)
        self.android_var = tk.BooleanVar(value=True)
        self.windows_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(self.platform_frame, text=self.lang_manager.get_text('ios'), variable=self.ios_var).pack(side=tk.LEFT, padx=10)
        ttk.Checkbutton(self.platform_frame, text=self.lang_manager.get_text('android'), variable=self.android_var).pack(side=tk.LEFT, padx=10)
        ttk.Checkbutton(self.platform_frame, text=self.lang_manager.get_text('windows'), variable=self.windows_var).pack(side=tk.LEFT, padx=10)
        
        # Android XML选项
        self.xml_frame = ttk.Frame(scrollable_frame)
        self.xml_frame.grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=5)
        ttk.Checkbutton(self.xml_frame, text=self.lang_manager.get_text('generate_xml'), variable=self.generate_xml).pack(side=tk.LEFT, padx=10)
        
        # 样式设置
        ttk.Separator(scrollable_frame, orient=tk.HORIZONTAL).grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(scrollable_frame, text=self.lang_manager.get_text('style_settings'), font=("Arial", 12, "bold")).grid(row=8, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        # 圆角设置
        self.corner_enabled = tk.BooleanVar(value=False)
        ttk.Checkbutton(scrollable_frame, text=self.lang_manager.get_text('enable_corner'), variable=self.corner_enabled, command=self.update_corner_controls).grid(row=9, column=0, columnspan=2, sticky=tk.W)
        
        self.corner_frame = ttk.Frame(scrollable_frame)
        self.corner_frame.grid(row=10, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(self.corner_frame, text=self.lang_manager.get_text('corner_radius')).pack(side=tk.LEFT, padx=5)
        self.corner_radius = tk.DoubleVar(value=0.2)
        self.corner_scale = ttk.Scale(self.corner_frame, from_=0, to=0.5, variable=self.corner_radius, orient=tk.HORIZONTAL, length=200)
        self.corner_scale.pack(side=tk.LEFT, padx=5)
        self.corner_label = ttk.Label(self.corner_frame, text="20%")
        self.corner_label.pack(side=tk.LEFT, padx=5)
        self.corner_scale.configure(command=lambda x: self.corner_label.config(text=f"{int(float(x)*100)}%"))
        
        # 边框设置
        self.border_enabled = tk.BooleanVar(value=False)
        ttk.Checkbutton(scrollable_frame, text=self.lang_manager.get_text('enable_border'), variable=self.border_enabled, command=self.update_border_controls).grid(row=11, column=0, columnspan=2, sticky=tk.W)
        
        self.border_frame = ttk.Frame(scrollable_frame)
        self.border_frame.grid(row=12, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(self.border_frame, text=self.lang_manager.get_text('border_width')).pack(side=tk.LEFT, padx=5)
        self.border_width = tk.DoubleVar(value=0.05)
        self.border_scale = ttk.Scale(self.border_frame, from_=0.01, to=0.2, variable=self.border_width, orient=tk.HORIZONTAL, length=200)
        self.border_scale.pack(side=tk.LEFT, padx=5)
        self.border_label = ttk.Label(self.border_frame, text="5%")
        self.border_label.pack(side=tk.LEFT, padx=5)
        self.border_scale.configure(command=lambda x: self.border_label.config(text=f"{int(float(x)*100)}%"))
        
        # 边框颜色
        ttk.Label(self.border_frame, text=self.lang_manager.get_text('border_color')).pack(side=tk.LEFT, padx=20)
        self.border_color = tk.StringVar(value="#000000")
        self.border_color_entry = ttk.Entry(self.border_frame, textvariable=self.border_color, width=10)
        self.border_color_entry.pack(side=tk.LEFT, padx=5)
        
        # 输出目录
        ttk.Separator(scrollable_frame, orient=tk.HORIZONTAL).grid(row=13, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(scrollable_frame, text=self.lang_manager.get_text('output_dir'), font=("Arial", 12, "bold")).grid(row=14, column=0, columnspan=2, pady=10, sticky=tk.W)
        
        self.output_dir = tk.StringVar(value=os.path.join(os.getcwd(), "generated_icons"))
        output_frame = ttk.Frame(scrollable_frame)
        output_frame.grid(row=15, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        output_frame.grid_columnconfigure(0, weight=1)
        
        ttk.Entry(output_frame, textvariable=self.output_dir).grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(output_frame, text=self.lang_manager.get_text('browse'), command=self.select_output_dir).grid(row=0, column=1, padx=5)
        
        # 固定底部区域
        bottom_frame = ttk.Frame(main_container)
        bottom_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 20))
        bottom_frame.grid_columnconfigure(0, weight=1)
        
        # 生成按钮
        generate_btn = ttk.Button(bottom_frame, text=self.lang_manager.get_text('generate_icons'), command=self.generate_icons, style="Accent.TButton")
        generate_btn.grid(row=0, column=0, pady=10, sticky=(tk.W, tk.E))
        
        # 进度条
        self.progress = ttk.Progressbar(bottom_frame, mode='indeterminate')
        self.progress.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # 状态标签
        self.status_label = ttk.Label(bottom_frame, text=self.lang_manager.get_text('ready'), foreground="green")
        self.status_label.grid(row=2, column=0, pady=5)
        
        # 绑定鼠标滚轮
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind("<MouseWheel>", _on_mousewheel)
        
        # 初始化控件状态
        self.update_corner_controls()
        self.update_border_controls()
    
    def update_corner_controls(self):
        state = 'normal' if self.corner_enabled.get() else 'disabled'
        for child in self.corner_frame.winfo_children():
            if isinstance(child, (ttk.Scale, ttk.Label)):
                child.configure(state=state)
    
    def update_border_controls(self):
        state = 'normal' if self.border_enabled.get() else 'disabled'
        for child in self.border_frame.winfo_children():
            if isinstance(child, (ttk.Scale, ttk.Label, ttk.Entry)):
                child.configure(state=state)
    
    def on_drop(self, event):
        """处理拖拽文件"""
        file_path = event.data
        if file_path:
            # 移除文件路径中的大括号和可能的空格
            file_path = file_path.replace("{", "").replace("}", "").strip()
            if os.path.isfile(file_path):
                self.load_image_from_path(file_path)
            else:
                messagebox.showerror(self.lang_manager.get_text('error'), "Invalid file path")
    
    def load_image_from_path(self, file_path):
        """从指定路径加载图片"""
        try:
            self.source_image_path = file_path
            self.source_image = Image.open(file_path)
            
            # 显示图片预览
            display_image = self.source_image.copy()
            display_image.thumbnail((300, 300))  # 增大预览尺寸
            photo = ImageTk.PhotoImage(display_image)
            
            self.image_label.configure(image=photo, text="", anchor="center")
            self.image_label.image = photo  # 保持引用
            
            self.status_label.configure(text=self.lang_manager.get_text('image_loaded'), foreground="green")
            
        except Exception as e:
            messagebox.showerror(self.lang_manager.get_text('error'), self.lang_manager.get_text('cannot_load_image').format(str(e)))
    
    def select_image(self):
        file_path = filedialog.askopenfilename(
            title=self.lang_manager.get_text('select_image_btn'),
            filetypes=[("图片文件", "*.png *.jpg *.jpeg *.gif *.bmp"), ("所有文件", "*.*")]
        )
        
        if file_path:
            self.load_image_from_path(file_path)
    
    def clear_image(self):
        self.source_image = None
        self.source_image_path = None
        self.image_label.configure(image="", text=self.lang_manager.get_text('please_select_image'), anchor="center")
        self.status_label.configure(text=self.lang_manager.get_text('ready'), foreground="green")
    
    def select_output_dir(self):
        directory = filedialog.askdirectory(title=self.lang_manager.get_text('browse'))
        if directory:
            self.output_dir.set(directory)
    
    def apply_corner_radius(self, image, radius_ratio):
        width, height = image.size
        radius = int(min(width, height) * radius_ratio)
        
        # 创建圆角蒙版
        mask = Image.new('L', (width, height), 0)
        draw = ImageDraw.Draw(mask)
        
        # 绘制圆角矩形
        draw.rounded_rectangle([(0, 0), (width, height)], radius=radius, fill=255)
        
        # 应用蒙版
        result = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        result.paste(image, (0, 0), mask)
        
        return result
    
    def apply_border(self, image, border_ratio, border_color):
        width, height = image.size
        border_width = int(min(width, height) * border_ratio)
        
        # 创建带边框的图片
        result = Image.new('RGBA', (width, height), border_color)
        
        # 计算内部区域
        inner_left = border_width
        inner_top = border_width
        inner_right = width - border_width
        inner_bottom = height - border_width
        
        # 如果原图有透明通道，保留透明度
        if image.mode == 'RGBA':
            result.paste(image, (0, 0), image)
            # 重新绘制边框
            draw = ImageDraw.Draw(result)
            draw.rectangle([(0, 0), (width-1, height-1)], outline=border_color, width=border_width)
        else:
            # 粘贴原图到中心
            result.paste(image, (border_width, border_width))
        
        return result
    
    def generate_android_xml(self, output_path):
        """生成Android XML文件"""
        xml_dir = os.path.join(output_path, "Android", "mipmap-anydpi-v26")
        os.makedirs(xml_dir, exist_ok=True)
        
        # ic_launcher.xml
        ic_launcher_xml = '''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@mipmap/ic_launcher_background"/>
    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
</adaptive-icon>'''
        
        # ic_launcher_round.xml
        ic_launcher_round_xml = '''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@mipmap/ic_launcher_background"/>
    <foreground android:drawable="@mipmap/ic_launcher_foreground"/>
</adaptive-icon>'''
        
        # 写入XML文件
        with open(os.path.join(xml_dir, "ic_launcher.xml"), "w", encoding="utf-8") as f:
            f.write(ic_launcher_xml)
            
        with open(os.path.join(xml_dir, "ic_launcher_round.xml"), "w", encoding="utf-8") as f:
            f.write(ic_launcher_round_xml)
    
    def generate_icons(self):
        if not self.source_image:
            messagebox.showerror(self.lang_manager.get_text('error'), self.lang_manager.get_text('select_image_first'))
            return
        
        if not self.ios_var.get() and not self.android_var.get() and not self.windows_var.get():
            messagebox.showerror(self.lang_manager.get_text('error'), self.lang_manager.get_text('select_platform_first'))
            return
        
        # 开始生成
        self.progress.start()
        self.status_label.configure(text=self.lang_manager.get_text('generating'), foreground="blue")
        self.root.update()
        
        try:
            output_path = self.output_dir.get()
            
            # 确保源图片是正方形
            source_img = self.source_image.copy()
            if source_img.size[0] != source_img.size[1]:
                # 裁剪为正方形
                size = min(source_img.size)
                left = (source_img.size[0] - size) // 2
                top = (source_img.size[1] - size) // 2
                source_img = source_img.crop((left, top, left + size, top + size))
            
            # 应用样式
            if self.corner_enabled.get():
                source_img = self.apply_corner_radius(source_img, self.corner_radius.get())
            
            if self.border_enabled.get():
                try:
                    border_color = self.border_color.get()
                    source_img = self.apply_border(source_img, self.border_width.get(), border_color)
                except ValueError:
                    messagebox.showerror(self.lang_manager.get_text('error'), self.lang_manager.get_text('border_color_error'))
                    return
            
            generated_count = 0
            
            # 生成iOS图标
            if self.ios_var.get():
                ios_path = os.path.join(output_path, "iOS")
                os.makedirs(ios_path, exist_ok=True)
                
                for name, sizes in self.ios_sizes.items():
                    for size in sizes:
                        resized_img = source_img.resize((size, size), Image.Resampling.LANCZOS)
                        filename = f"{name}_{size}x{size}.png"
                        filepath = os.path.join(ios_path, filename)
                        resized_img.save(filepath, "PNG")
                        generated_count += 1
            
            # 生成Android图标
            if self.android_var.get():
                android_path = os.path.join(output_path, "Android")
                os.makedirs(android_path, exist_ok=True)
                
                for name, sizes in self.android_sizes.items():
                    for size in sizes:
                        resized_img = source_img.resize((size, size), Image.Resampling.LANCZOS)
                        filename = f"{name}_{size}x{size}.png"
                        filepath = os.path.join(android_path, filename)
                        resized_img.save(filepath, "PNG")
                        generated_count += 1
                
                # 生成XML文件
                if self.generate_xml.get():
                    self.generate_android_xml(output_path)
                    generated_count += 2  # ic_launcher.xml 和 ic_launcher_round.xml
            
            # 生成Windows图标
            if self.windows_var.get():
                windows_path = os.path.join(output_path, "Windows")
                os.makedirs(windows_path, exist_ok=True)
                
                for name, sizes in self.windows_sizes.items():
                    for size in sizes:
                        resized_img = source_img.resize((size, size), Image.Resampling.LANCZOS)
                        filename = f"{name}_{size}x{size}.png"
                        filepath = os.path.join(windows_path, filename)
                        resized_img.save(filepath, "PNG")
                        generated_count += 1
                
                # 生成Windows ICO文件（包含所有尺寸）
                self.generate_windows_ico(windows_path, source_img)
                generated_count += 1
            
            self.progress.stop()
            self.status_label.configure(text=self.lang_manager.get_text('completed').format(generated_count), foreground="green")
            messagebox.showinfo(self.lang_manager.get_text('success'), self.lang_manager.get_text('generation_complete').format(generated_count, output_path))
            
        except Exception as e:
            self.progress.stop()
            self.status_label.configure(text=self.lang_manager.get_text('failed'), foreground="red")
            messagebox.showerror(self.lang_manager.get_text('error'), self.lang_manager.get_text('generation_error').format(str(e)))

    def generate_windows_ico(self, windows_path, source_img):
        """生成Windows ICO文件"""
        # ICO文件需要的尺寸
        ico_sizes = [16, 32, 48, 64, 128, 256]
        
        # 创建不同尺寸的图像列表
        img_list = []
        for size in ico_sizes:
            resized_img = source_img.resize((size, size), Image.Resampling.LANCZOS)
            img_list.append(resized_img)
        
        # 保存ICO文件
        ico_path = os.path.join(windows_path, "app_icon.ico")
        img_list[0].save(ico_path, format='ICO', sizes=[(size, size) for size in ico_sizes])

def main():
    if DRAG_DROP_ENABLED:
        root = TkinterDnD.Tk()
    else:
        root = tk.Tk()
    app = IconGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
