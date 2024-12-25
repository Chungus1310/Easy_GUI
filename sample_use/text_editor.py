import tkinter as tk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from gui_lib import MainWindow, CustomCombobox, CustomLabel, CustomButton, ThemeManager
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import platform
import psutil

class TextEditorApp(MainWindow):
    def __init__(self):
        super().__init__(title="Text Editor", theme="nordic_frost")
        self.theme_manager = ThemeManager()
        self.file_path = None
        self.status_text = tk.StringVar(value="Ready")
        self._create_widgets()  
        self._create_menu()     
        self._bind_events()

    def _create_menu(self):
        # Create a menu bar
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self._new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self._open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self._save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self._save_as, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # Edit menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"), accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"), accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"), accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=lambda: self.text_area.tag_add(SEL, "1.0", END), accelerator="Ctrl+A")

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

        # Text Area
        self.text_area = tk.Text(
            self.content_frame,
            wrap=WORD,
            undo=True,
            font=self.theme_manager.component_styles["entry"]["font"]
        )
        self.text_area.pack(fill=BOTH, expand=True)
        self._update_text_area_style()

        # Status Bar
        self.status_bar = CustomLabel(self.content_frame, textvariable=self.status_text, bootstyle="info.TLabel")
        self.status_bar.pack(fill=X, side=BOTTOM)

    def _bind_events(self):
        self.text_area.bind("<Control-n>", self._new_file)
        self.text_area.bind("<Control-o>", self._open_file)
        self.text_area.bind("<Control-s>", self._save_file)
        self.text_area.bind("<Control-Shift-s>", self._save_as)
        self.text_area.bind("<Key>", self._on_key_press)

    def _on_key_press(self, event=None):
        self.update_status_bar()

    def _new_file(self, event=None):
        if self._check_unsaved_changes():
            self.text_area.delete("1.0", END)
            self.file_path = None
            self.title("Text Editor")

    def _open_file(self, event=None):
        if not self._check_unsaved_changes():
            return

        filepath = fd.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            try:
                with open(filepath, "r") as file:
                    self.text_area.delete("1.0", END)
                    self.text_area.insert("1.0", file.read())
                self.file_path = filepath
                self.title(f"Text Editor - {filepath}")
                self.update_status_bar()
            except Exception as e:
                mb.showerror("Error", f"Failed to open file: {e}")

    def _save_file(self, event=None):
        if self.file_path:
            try:
                with open(self.file_path, "w") as file:
                    file.write(self.text_area.get("1.0", END))
                self.update_status_bar()
                return True
            except Exception as e:
                mb.showerror("Error", f"Failed to save file: {e}")
                return False
        else:
            return self._save_as()

    def _save_as(self, event=None):
        filepath = fd.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            try:
                with open(filepath, "w") as file:
                    file.write(self.text_area.get("1.0", END))
                self.file_path = filepath
                self.title(f"Text Editor - {filepath}")
                self.update_status_bar()
                return True
            except Exception as e:
                mb.showerror("Error", f"Failed to save file: {e}")
                return False
        return False

    def _check_unsaved_changes(self):
        if self.text_area.edit_modified():
            response = mb.askyesnocancel("Unsaved Changes", "Do you want to save changes before closing?")
            if response is True:
                return self._save_file()
            elif response is False:
                return True
            else:
                return False
        return True

    def _on_theme_selected(self, event):
        selected_theme = self.theme_combobox.get_value()
        self.theme_manager.set_theme(selected_theme)
        self._update_text_area_style()
        self.update_ui()

    def _update_text_area_style(self):
        theme_colors = self.theme_manager.get_theme_colors()
        self.text_area.config(
            fg=theme_colors["foreground"],
            bg=theme_colors["background"],
            insertbackground=theme_colors["primary"],
            font=self.theme_manager.component_styles["entry"]["font"],
            relief="flat",
            highlightthickness=0,
            borderwidth=0,
            highlightcolor=theme_colors["primary"],
            highlightbackground=theme_colors["secondary"]
        )

    def update_status_bar(self):
        if self.file_path:
            file_name = os.path.basename(self.file_path)
            if self.text_area.edit_modified():
                file_name = "*" + file_name
            self.status_text.set(file_name)
        else:
            self.status_text.set("New File")
        self.text_area.edit_modified(False)

if __name__ == "__main__":
    app = TextEditorApp()
    app.run()