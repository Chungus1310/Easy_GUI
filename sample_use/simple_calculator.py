import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sys
import os

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from gui_lib import MainWindow, CustomButton, CustomLabel, ThemeManager, CustomCombobox

class CalculatorApp(MainWindow):
    def __init__(self):
        super().__init__(title="Calculator", theme="nordic_frost")
        self.theme_manager = ThemeManager()
        self.result_string = tk.StringVar(value="0")
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

        # Display Label
        display_label = CustomLabel(self.content_frame, textvariable=self.result_string, font=("Arial", 24), anchor="e", padding=10)
        display_label.pack(fill=X)

        # Button Frame
        button_frame = ttk.Frame(self.content_frame)
        button_frame.pack(fill=BOTH, expand=True)

        button_layout = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", "C", "=", "+")
        ]
        
        button_styles = {
            "/": PRIMARY,
            "*": PRIMARY,
            "-": PRIMARY,
            "+": PRIMARY,
            "=": SUCCESS,
            "C": WARNING
        }

        for row_index, row in enumerate(button_layout):
            for col_index, text in enumerate(row):
                style = button_styles.get(text, SECONDARY)
                button = CustomButton(
                    button_frame,
                    text=text,
                    command=lambda t=text: self._button_click(t),
                    bootstyle=style,
                    width=5 # Set a fixed width for each button
                )
                button.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")

        # Configure grid weights to make buttons expand
        for i in range(4):
            button_frame.rowconfigure(i, weight=1)
            button_frame.columnconfigure(i, weight=1)

    def _button_click(self, char):
        if char == "=":
            try:
                # Evaluate the expression and update the result
                result = str(eval(self.result_string.get()))
                self.result_string.set(result)
            except:
                self.result_string.set("Error")
        elif char == "C":
            self.result_string.set("0")
        else:
            if self.result_string.get() == "0" or self.result_string.get() == "Error":
                self.result_string.set(char)
            else:
                self.result_string.set(self.result_string.get() + char)

def _on_theme_selected(self, event):
    """Handles theme selection."""
    selected_theme = self.theme_combobox.get_value()
    self.theme_manager.set_theme(selected_theme)
    self.update_ui()

app = CalculatorApp()
app.run()