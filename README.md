# Easy GUI 🎨

Welcome to **Easy GUI**, your go-to Python library for creating beautiful, themeable, and easy-to-use graphical user interfaces (GUIs) with **Tkinter** and **ttkbootstrap**! Whether you're building a simple calculator, a system info tool, or a full-fledged text editor, Easy GUI has got you covered. Let's dive in and see what this library can do for you!

---

## 🌟 Features

### 1. **Themes Galore 🎨**
   - Choose from a variety of pre-built themes like **Nordic Frost**, **Ocean Breeze**, **Cosmic Night**, and more!
   - Switch themes dynamically at runtime with just a few lines of code.
   - Customize your own themes and make your app look exactly how you want.

### 2. **Custom Widgets 🛠️**
   - **CustomButton**: Buttons with ripple effects, hover states, and theme-aware styling.
   - **CustomLabel**: Labels that automatically update with the current theme.
   - **CustomEntry**: Stylish input fields with focus effects.
   - **CustomCombobox**: Dropdown menus that look great in any theme.
   - **CustomCheckbutton**: Checkboxes that fit seamlessly into your design.

### 3. **Dynamic UI Updates 🔄**
   - Automatically update your UI when switching themes.
   - Real-time updates for dynamic content (e.g., CPU usage in the system info app).

### 4. **Easy to Use 🚀**
   - Simple and intuitive API for creating and managing GUI elements.
   - No need to worry about complex Tkinter configurations—Easy GUI handles it all for you.

### 5. **Sample Applications 🖥️**
   - **Simple Calculator**: A basic calculator app to get you started.
   - **System Info**: Display real-time system information like CPU, RAM, and disk usage.
   - **Text Editor**: A fully functional text editor with file management capabilities.

---

## 🚀 Getting Started

### Installation
First, make sure you have Python installed. Then, install the required dependencies:

```bash
pip install tkinter ttkbootstrap psutil
```

### Clone the Repository
Clone the Easy GUI repository to your local machine:

```bash
git clone https://github.com/Chungus1310/Easy_GUI.git
cd Easy_GUI
```

### Running the Sample Apps
The `sample_use` folder contains three sample applications to help you get started:

1. **Simple Calculator**:
   ```bash
   python sample_use/simple_calculator.py
   ```

2. **System Info**:
   ```bash
   python sample_use/system_info.py
   ```

3. **Text Editor**:
   ```bash
   python sample_use/text_editor.py
   ```

---

## 📚 Documentation

### 1. **Creating a Main Window**
To create a main window for your application, use the `MainWindow` class:

```python
from gui_lib import MainWindow

app = MainWindow(title="My Awesome App", theme="nordic_frost")
app.run()
```

### 2. **Adding a Theme Switcher**
You can add a theme switcher to your app using the `CustomCombobox` widget:

```python
from gui_lib import CustomCombobox, ThemeManager

theme_manager = ThemeManager()
theme_combobox = CustomCombobox(
    parent_frame,
    values=theme_manager.get_available_themes(),
    bootstyle="info"
)
theme_combobox.set_value(theme_manager.get_current_theme())
theme_combobox.bind("<<ComboboxSelected>>", lambda event: theme_manager.set_theme(theme_combobox.get_value()))
```

### 3. **Using Custom Widgets**
Here’s how you can use some of the custom widgets:

#### **CustomButton**
```python
from gui_lib import CustomButton

button = CustomButton(
    parent_frame,
    text="Click Me",
    command=lambda: print("Button Clicked!"),
    bootstyle="success"
)
button.pack()
```

#### **CustomLabel**
```python
from gui_lib import CustomLabel

label = CustomLabel(
    parent_frame,
    text="Hello, World!",
    font=("Arial", 16),
    bootstyle="info.TLabel"
)
label.pack()
```

#### **CustomEntry**
```python
from gui_lib import CustomEntry

entry = CustomEntry(
    parent_frame,
    width=30,
    bootstyle="primary"
)
entry.pack()
```

### 4. **Updating the UI**
When you change the theme, you can update the UI dynamically:

```python
def update_ui():
    for widget in parent_frame.winfo_children():
        if isinstance(widget, CustomElement):
            widget.update_styles()

theme_manager.set_theme("new_theme")
update_ui()
```

---

## 🛠️ Customizing Themes

You can easily add your own themes to the `ThemeManager`. Here’s how:

1. Open `gui_lib.py`.
2. Add your theme to the `themes` dictionary in the `ThemeManager` class:

```python
themes = {
    "my_custom_theme": {
        "primary": "#FF5733",
        "secondary": "#33FF57",
        "background": "#2E3440",
        "foreground": "#FFFFFF",
        "success": "#00FF00",
        "info": "#0000FF",
        "warning": "#FFFF00",
        "danger": "#FF0000",
        "light": "#F8F9FA",
        "dark": "#212529",
        "font": "Helvetica"
    }
}
```

3. Use your new theme in your app:

```python
app = MainWindow(title="My App", theme="my_custom_theme")
```

---

## 🤝 Contributing

I’d love for you to contribute to Easy GUI! Whether it’s fixing bugs, adding new features, or improving the documentation, your help is always welcome. Here’s how you can get started:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them.
4. Submit a pull request.

---

## 📜 License

Easy GUI is licensed under the **MIT License**. Feel free to use, modify, and distribute it as you see fit.

---

## 📬 Contact

Got questions, suggestions, or just want to say hi? Feel free to reach out to me:

- **GitHub**: [Chungus1310](https://github.com/Chungus1310)
  
---

## 🎉 Happy Coding!

That’s it! You’re all set to start building amazing GUIs with Easy GUI. Whether you’re a beginner or a seasoned developer, this library is designed to make your life easier. So go ahead, create something awesome, and don’t forget to share it with the world!

🌟 **Star this repo** if you find it useful, and happy coding! 🚀

--- 

**Easy GUI** – Making GUI development easy, one widget at a time. 🎨✨
