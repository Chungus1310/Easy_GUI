import platform
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import psutil
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from gui_lib import MainWindow, CustomCombobox, CustomLabel, ThemeManager

class SystemInfoApp(MainWindow):
    def __init__(self):
        super().__init__(title="System Information", theme="nordic_frost")
        self.theme_manager = ThemeManager()
        self._create_widgets()

    def _create_widgets(self):
        # Theme Switcher
        theme_frame = ttk.Frame(self.menu_frame)
        theme_frame.pack(fill=X, padx=5, pady=5)

        theme_label = CustomLabel(theme_frame, text="Theme:")
        theme_label.pack(side=LEFT)

        self.theme_combobox = CustomCombobox(
            theme_frame,
            values=self.theme_manager.get_available_themes(),
            bootstyle=INFO
        )
        self.theme_combobox.set_value(self.theme_manager.get_current_theme())
        self.theme_combobox.bind("<<ComboboxSelected>>", self._on_theme_selected)
        self.theme_combobox.pack(side=LEFT, padx=(5, 0))

        # System Information Frame
        info_frame = ttk.Frame(self.content_frame)
        info_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # OS
        os_label = CustomLabel(info_frame, text=f"OS: {platform.system()} {platform.release()}")
        os_label.pack(fill=X)

        # Processor
        processor_label = CustomLabel(info_frame, text=f"Processor: {platform.processor()}")
        processor_label.pack(fill=X)

        # Architecture
        arch_label = CustomLabel(info_frame, text=f"Architecture: {platform.machine()}")
        arch_label.pack(fill=X)

        # RAM
        mem = psutil.virtual_memory()
        mem_total = round(mem.total / (1024.0 ** 3), 2)
        mem_available = round(mem.available / (1024.0 ** 3), 2)
        mem_used = round(mem.used / (1024.0 ** 3), 2)
        mem_percent = mem.percent
        ram_label = CustomLabel(info_frame, text=f"RAM: {mem_used} GB / {mem_total} GB ({mem_percent}%)")
        ram_label.pack(fill=X)

        # Disk Usage
        disk = psutil.disk_usage('/')
        disk_total = round(disk.total / (1024.0 ** 3), 2)
        disk_used = round(disk.used / (1024.0 ** 3), 2)
        disk_free = round(disk.free / (1024.0 ** 3), 2)
        disk_percent = disk.percent
        disk_label = CustomLabel(info_frame, text=f"Disk: {disk_used} GB / {disk_total} GB ({disk_percent}%)")
        disk_label.pack(fill=X)

        # CPU Usage
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        cpu_label = CustomLabel(info_frame, text="CPU Usage:")
        cpu_label.pack(fill=X)

        # Initialize as a list
        self.cpu_labels = []
        for i, percent in enumerate(cpu_percent):
            label = CustomLabel(info_frame, text=f"  Core {i+1}: {percent}%")
            label.pack(fill=X)
            self.cpu_labels.append(label)  # Append to list

        self.update_cpu_usage()  # Start updating CPU usage

    def _on_theme_selected(self, event):
        selected_theme = self.theme_combobox.get_value()
        self.theme_manager.set_theme(selected_theme)
        self.update_ui()

    def update_cpu_usage(self):
        """Updates CPU usage information."""
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        for i, percent in enumerate(cpu_percent):
            # Use configure instead of config
            self.cpu_labels[i].element.configure(text=f"  Core {i+1}: {percent}%")
        self.after(1000, self.update_cpu_usage)

if __name__ == "__main__":
    app = SystemInfoApp()
    app.run()