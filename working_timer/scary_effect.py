import tkinter as tk
from PIL import Image, ImageTk
import threading

class ScaryEffect:
    def __init__(self, image_path, sound_path):
        self.image_path = image_path
        self.sound_path = sound_path
        self.window = None
        self.label = None
        self.original_image = None
        self.zoom_step = 0.05
        self.zoom_delay = 20
        self.max_scale = 1.5
        self.current_scale = 0.1
        self.transparent_color = '#010101'   # رنگ اختصاصی برای شفافیت

    def show(self):
        self.window = tk.Toplevel()
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        # تنظیم شفافیت با رنگ مشخص
        self.window.configure(bg=self.transparent_color)
        self.window.attributes('-transparentcolor', self.transparent_color)

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_height}+0+0')

        self.label = tk.Label(self.window, bg=self.transparent_color)
        self.label.pack(expand=True)

        try:
            # بارگذاری تصویر با حفظ شفافیت (RGBA)
            self.original_image = Image.open(self.image_path).convert("RGBA")
        except Exception as e:
            print(f"Error loading image: {e}")
            self.window.destroy()
            return

        self.animate_zoom()
        threading.Thread(target=self.play_sound, daemon=True).start()
        self.window.bind('<Button-1>', lambda e: self.close())
        self.window.after(3000, self.close)   # بسته شدن خودکار بعد ۳ ثانیه

    def animate_zoom(self):
        if not self.window or not self.label:
            return
        if self.current_scale >= self.max_scale:
            self.current_scale = self.max_scale

        if self.original_image:
            img_width, img_height = self.original_image.size
            new_width = int(img_width * self.current_scale)
            new_height = int(img_height * self.current_scale)
            # محدود کردن به اندازه صفحه
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()
            if new_width > screen_width:
                new_width = screen_width
                new_height = int(img_height * (screen_width / img_width))
            if new_height > screen_height:
                new_height = screen_height
                new_width = int(img_width * (screen_height / img_height))
            # رزایز با حفظ کانال آلفا
            resized = self.original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(resized)
            self.label.config(image=photo)
            self.label.image = photo

        if self.current_scale < self.max_scale:
            self.current_scale += self.zoom_step
            if self.current_scale > self.max_scale:
                self.current_scale = self.max_scale
            self.window.after(self.zoom_delay, self.animate_zoom)

    def play_sound(self):
        try:
            from playsound import playsound
            playsound(self.sound_path)
        except ImportError:
            try:
                import pygame
                pygame.mixer.init()
                pygame.mixer.music.load(self.sound_path)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    threading.Event().wait(0.1)
            except Exception as e:
                print(f"Sound error: {e}")
        except Exception as e:
            print(f"Sound error: {e}")

    def close(self):
        if self.window:
            self.window.destroy()
            self.window = None

def show_scary_effect(image_path='scary.png', sound_path='scary.wav'):
    effect = ScaryEffect(image_path, sound_path)
    effect.show()