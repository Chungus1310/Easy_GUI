import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json
import os

class ThemeManager:
    """Manages the application's theme and color palette."""
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ThemeManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, default_theme="nordic_frost"):
        """Initializes the theme manager."""
        if hasattr(self, '_initialized'):
            return
        self._initialized = True
        # Remove tk instance since we don't need it anymore
        self.themes = {
            "ocean_ui_dark": {
                "primary": "#0d6efd",
                "secondary": "#6c757d",
                "background": "#212529",
                "foreground": "#ced4da",
                "success": "#198754",
                "info": "#0dcaf0",
                "warning": "#ffc107",
                "danger": "#dc3545",
                "light": "#f8f9fa",
                "dark": "#212529",
                "font": "Helvetica"
            },
            "flat_ui_light": {
                "primary": "#3498db",
                "secondary": "#bdc3c7",
                "background": "#ecf0f1",
                "foreground": "#2c3e50",
                "success": "#2ecc71",
                "info": "#3498db",
                "warning": "#f39c12",
                "danger": "#e74c3c",
                "light": "#ecf0f1",
                "dark": "#34495e",
                "font": "Arial"
            },
            "material_dark": {
                "primary": "#2196f3",
                "secondary": "#757575",
                "background": "#212121",
                "foreground": "#ffffff",
                "success": "#4caf50",
                "info": "#2196f3",
                "warning": "#ff9800",
                "danger": "#f44336",
                "light": "#f5f5f5",
                "dark": "#212121",
                "font": "Roboto"
            },
            "pastel_light": {
                "primary": "#83c5be",
                "secondary": "#ffddd2",
                "background": "#fdfffc",
                "foreground": "#555b6e",
                "success": "#a8dadc",
                "info": "#83c5be",
                "warning": "#ffb4a2",
                "danger": "#e5989b",
                "light": "#fdfffc",
                "dark": "#555b6e",
                "font": "Verdana"
            },
            "nordic_frost": {
            "primary": "#88C0D0",     # Frost blue - primary actions, buttons
            "secondary": "#81A1C1",   # Muted blue - secondary buttons, borders
            "background": "#2E3440",  # Dark blue-grey - main background
            "foreground": "#ECEFF4",  # Snow white - text, icons
            "success": "#A3BE8C",     # Sage green - success states
            "info": "#5E81AC",        # Deep blue - information states
            "warning": "#EBCB8B",     # Warm yellow - warnings
            "danger": "#BF616A",      # Soft red - errors, critical actions
            "light": "#E5E9F0",       # Light grey - light mode elements
            "dark": "#3B4252",        # Darker blue-grey - dark mode elements
            "font": "Inter"           # Modern, clean font
        },
        
        "forest_depths": {
            "primary": "#2D936C",     # Forest green - primary actions
            "secondary": "#69A297",   # Sage - secondary elements
            "background": "#133832",  # Deep forest - main background
            "foreground": "#E8F3F1",  # Mint white - text
            "success": "#52B788",     # Bright green - success states
            "info": "#40916C",        # Muted green - information
            "warning": "#D68C45",     # Terra cotta - warnings
            "danger": "#AE2012",      # Deep red - errors
            "light": "#F1F8F6",       # Light mint - light elements
            "dark": "#1B4332",        # Dark forest - dark elements
            "font": "Montserrat"      # Natural, organic feel
        },
        
        "cosmic_night": {
            "primary": "#7B2CBF",     # Vibrant purple - primary actions
            "secondary": "#9D4EDD",   # Light purple - secondary elements
            "background": "#10002B",  # Deep space - main background
            "foreground": "#E0AAFF",  # Soft purple - text
            "success": "#C77DFF",     # Bright purple - success states
            "info": "#9D4EDD",        # Medium purple - information
            "warning": "#FF9E00",     # Bright orange - warnings
            "danger": "#FF5400",      # Deep orange - errors
            "light": "#E0AAFF",       # Light purple - light elements
            "dark": "#240046",        # Dark purple - dark elements
            "font": "Space Grotesk"   # Modern, futuristic font
        },
        
        "desert_oasis": {
            "primary": "#E9C46A",     # Sandy gold - primary actions
            "secondary": "#F4A261",   # Coral - secondary elements
            "background": "#264653",  # Deep teal - main background
            "foreground": "#F9F7F3",  # Off-white - text
            "success": "#2A9D8F",     # Turquoise - success states
            "info": "#287271",        # Dark teal - information
            "warning": "#E76F51",     # Terracotta - warnings
            "danger": "#D62828",      # Bright red - errors
            "light": "#F9F7F3",       # Cream - light elements
            "dark": "#1D3557",        # Navy - dark elements
            "font": "Playfair Display" # Elegant, refined font
        },
        
        "ocean_breeze": {
            "primary": "#00B4D8",     # Ocean blue - primary actions
            "secondary": "#90E0EF",   # Light blue - secondary elements
            "background": "#03045E",  # Deep navy - main background
            "foreground": "#CAF0F8",  # Ice blue - text
            "success": "#48CAE4",     # Bright blue - success states
            "info": "#0077B6",        # Medium blue - information
            "warning": "#FFB703",     # Sunny yellow - warnings
            "danger": "#D62828",      # Coral red - errors
            "light": "#CAF0F8",       # Pale blue - light elements
            "dark": "#023E8A",        # Dark blue - dark elements
            "font": "Poppins"         # Clean, modern font
        }
        }

        self.current_theme = self.load_theme()
        if not self.current_theme or self.current_theme not in self.themes:
            self.current_theme = default_theme
        
        # Component Styles
        self.component_styles = {
            "button": {
                "padding": (10, 5),
                "borderwidth": 0,
                "relief": "flat",
                "hover_opacity": 0.9,
                "font": (self.themes[self.current_theme]["font"], 10)
            },
            "entry": {
                "padding": (8, 4),
                "borderwidth": 1,
                "relief": "solid",
                "font": (self.themes[self.current_theme]["font"], 10)
            },
            "label": {
                "padding": (5, 5),
                "wraplength": 300,
                "font": (self.themes[self.current_theme]["font"], 10)
            },
            "combobox": {
                "padding": (5, 4),
                "arrowsize": 12,
                "listbox_height": 5,
                "font": (self.themes[self.current_theme]["font"], 10)
            },
            "checkbutton": {
                "indicatorcolor": self.themes[self.current_theme]["background"],
                "font": (self.themes[self.current_theme]["font"], 10)
            }
        }

        # State Colors
        self.state_colors = {
            "hover": {
                "primary": self._adjust_color_brightness(self.themes[self.current_theme]["primary"], 1.1),
                "secondary": self._adjust_color_brightness(self.themes[self.current_theme]["secondary"], 1.1),
                "success": self._adjust_color_brightness(self.themes[self.current_theme]["success"], 1.1),
                "info": self._adjust_color_brightness(self.themes[self.current_theme]["info"], 1.1),
                "warning": self._adjust_color_brightness(self.themes[self.current_theme]["warning"], 1.1),
                "danger": self._adjust_color_brightness(self.themes[self.current_theme]["danger"], 1.1),
                "foreground": self.themes[self.current_theme]["foreground"]  # Added foreground
            },
            "active": {
                "primary": self._adjust_color_brightness(self.themes[self.current_theme]["primary"], 0.9),
                "secondary": self._adjust_color_brightness(self.themes[self.current_theme]["secondary"], 0.9),
                "success": self._adjust_color_brightness(self.themes[self.current_theme]["success"], 0.9),
                "info": self._adjust_color_brightness(self.themes[self.current_theme]["info"], 0.9),
                "warning": self._adjust_color_brightness(self.themes[self.current_theme]["warning"], 0.9),
                "danger": self._adjust_color_brightness(self.themes[self.current_theme]["danger"], 0.9),
                "foreground": self.themes[self.current_theme]["foreground"]  # Added foreground
            },
            "disabled": {
                "background": self._adjust_color_opacity(self.themes[self.current_theme]["background"], 0.5),
                "foreground": self._adjust_color_opacity(self.themes[self.current_theme]["foreground"], 0.5),
            }
        }

        self.apply_theme()

    def _adjust_color_brightness(self, color, factor):
        """Adjust the brightness of a color by a factor"""
        # Convert hex to RGB, adjust brightness, convert back to hex
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        
        r = min(255, int(r * factor))
        g = min(255, int(g * factor))
        b = min(255, int(b * factor))
        
        return f"#{r:02x}{g:02x}{b:02x}"

    def _adjust_color_opacity(self, color, opacity):
        """Add opacity to a color"""
        return f"{color}{int(opacity * 255):02x}"

    def load_theme(self):
        """Loads the theme from settings file."""
        settings_file = "app_settings.json"
        if os.path.exists(settings_file):
            with open(settings_file, "r") as file:
                try:
                    settings = json.load(file)
                    return settings.get("theme", None)
                except json.JSONDecodeError:
                   return None
        return None

    def save_theme(self):
        """Saves the current theme to settings file."""
        settings_file = "app_settings.json"
        with open(settings_file, "w") as file:
            json.dump({"theme": self.current_theme}, file)

    def apply_theme(self):
        """Applies the current theme to the application."""
        theme_colors = self.themes.get(self.current_theme)
        style = ttk.Style()

        # Configure fonts for all widgets
        style.configure('.', font=(theme_colors["font"], 10))
        
        # Add hover effects first
        self._add_hover_effects()

        # Button styles
        style.configure('TButton',
            foreground=theme_colors["foreground"],
            background=theme_colors["primary"],
            bordercolor=theme_colors["primary"],
            darkcolor=theme_colors["background"],
            lightcolor=theme_colors["background"],
            padding=self.component_styles["button"]["padding"],
            borderwidth=self.component_styles["button"]["borderwidth"],
            relief=self.component_styles["button"]["relief"],
            focusthickness=0,
            focuscolor=theme_colors["primary"]
        )
        style.map('TButton',
            foreground=[
                ('disabled', self.state_colors["disabled"]["foreground"]),
                ('pressed', theme_colors["foreground"]),
                ('active', theme_colors["foreground"])
            ],
            background=[
                ('disabled', self.state_colors["disabled"]["background"]),
                ('pressed', self.state_colors["active"]["primary"]),
                ('active', self.state_colors["hover"]["primary"])
            ],
            bordercolor=[
                ('disabled', self.state_colors["disabled"]["background"]),
                ('pressed', self.state_colors["active"]["primary"]),
                ('active', self.state_colors["hover"]["primary"])
            ]
        )

        # Configure other button styles (secondary, success, info, warning, danger)
        for _style in ["secondary", "success", "info", "warning", "danger"]:
            style.configure(f"{_style}.TButton",
                background=theme_colors[_style],
                foreground=theme_colors["foreground"],
                bordercolor=theme_colors[_style],
                darkcolor=theme_colors["background"],
                lightcolor=theme_colors["background"],
                padding=self.component_styles["button"]["padding"],
                borderwidth=self.component_styles["button"]["borderwidth"],
                relief=self.component_styles["button"]["relief"],
                focusthickness=0,
                focuscolor=theme_colors[_style]
            )
            style.map(f'{_style}.TButton',
                foreground=[
                    ('disabled', self.state_colors["disabled"]["foreground"]),
                    ('pressed', theme_colors["foreground"]),
                    ('active', theme_colors["foreground"])
                ],
                background=[
                    ('disabled', self.state_colors["disabled"]["background"]),
                    ('pressed', self.state_colors["active"][_style]),
                    ('active', self.state_colors["hover"][_style])
                ],
                bordercolor=[
                    ('disabled', self.state_colors["disabled"]["background"]),
                    ('pressed', self.state_colors["active"][_style]),
                    ('active', self.state_colors["hover"][_style])
                ]
            )

        # Entry styles
        style.configure('TEntry',
            foreground=theme_colors["foreground"],
            fieldbackground=theme_colors["background"],
            bordercolor=theme_colors["secondary"],
            lightcolor=theme_colors["background"],
            darkcolor=theme_colors["background"],
            padding=self.component_styles["entry"]["padding"],
            borderwidth=self.component_styles["entry"]["borderwidth"],
            relief=self.component_styles["entry"]["relief"],
            insertcolor=theme_colors["primary"]
        )
        style.map('TEntry',
            foreground=[('disabled', self.state_colors["disabled"]["foreground"])],
            fieldbackground=[('disabled', self.state_colors["disabled"]["background"])],
            bordercolor=[
                ('focus', theme_colors["primary"]),
                ('disabled', theme_colors["secondary"])
            ]
        )

        # Label styles
        style.configure('TLabel',
            foreground=theme_colors["foreground"],
            background=theme_colors["background"],
            padding=self.component_styles["label"]["padding"],
            wraplength=self.component_styles["label"]["wraplength"]
        )
        style.configure('info.TLabel',
            foreground=theme_colors["info"],
            background=theme_colors["background"]
        )

        # Combobox styles
        style.configure('TCombobox',
            foreground=theme_colors["foreground"],
            fieldbackground=theme_colors["background"],
            bordercolor=theme_colors["secondary"],
            darkcolor=theme_colors["background"],
            lightcolor=theme_colors["background"],
            arrowcolor=theme_colors["foreground"],
            padding=self.component_styles["combobox"]["padding"],
            arrowsize=self.component_styles["combobox"]["arrowsize"]
        )
        style.map('TCombobox',
            foreground=[
                ('disabled', self.state_colors["disabled"]["foreground"]),
                ('readonly', theme_colors["foreground"])
            ],
            fieldbackground=[
                ('disabled', self.state_colors["disabled"]["background"]),
                ('readonly', theme_colors["background"])
            ],
            bordercolor=[
                ('focus', theme_colors["primary"]),
                ('disabled', theme_colors["secondary"]),
                ('readonly', theme_colors["secondary"])
            ],
            arrowcolor=[
                ('disabled', self.state_colors["disabled"]["foreground"]),
                ('readonly', theme_colors["foreground"])
            ]
        )

        # Checkbutton styles
        style.configure('TCheckbutton',
            foreground=theme_colors["foreground"],
            background=theme_colors["background"],
            indicatorcolor=self.component_styles["checkbutton"]["indicatorcolor"],
            padding=self.component_styles["label"]["padding"]
        )
        style.map('TCheckbutton',
            foreground=[('disabled', self.state_colors["disabled"]["foreground"])],
            background=[('disabled', self.state_colors["disabled"]["background"])],
            indicatorcolor=[
                ('selected', theme_colors["primary"]),
                ('pressed', theme_colors["primary"]),
                ('disabled', self.state_colors["disabled"]["background"])
            ]
        )

        # Frame styles
        style.configure('TFrame', background=theme_colors["background"])
        style.configure('secondary.TFrame', background=theme_colors["secondary"])
        style.configure('light.TFrame', background=theme_colors["light"])

        # Scrollbar styles
        style.configure('Vertical.TScrollbar',
            background=theme_colors["secondary"],
            troughcolor=theme_colors["background"],
            bordercolor=theme_colors["background"],
            arrowcolor=theme_colors["foreground"],
            gripcount=0,
            relief="flat",
            borderwidth=0
        )
        style.map('Vertical.TScrollbar',
            background=[
                ('pressed', self.state_colors["active"]["secondary"]),
                ('active', self.state_colors["hover"]["secondary"])
            ],
            arrowcolor=[
                ('pressed', self.state_colors["active"]["foreground"]),
                ('active', self.state_colors["hover"]["foreground"])
            ]
        )

        # Add hover effects
        self._add_hover_effects()

    def _add_hover_effects(self):
        """Add hover effects using ttk style configuration"""
        style = ttk.Style()
        theme_colors = self.themes[self.current_theme]
        
        # Configure hover effects for buttons
        style.map('TButton',
            background=[('active', self.state_colors["hover"]["primary"])]
        )
        
        # Configure hover effects for entries
        style.map('TEntry',
            bordercolor=[('focus', theme_colors["primary"])]
        )
        
        # Configure hover effects for comboboxes
        style.map('TCombobox',
            bordercolor=[('focus', theme_colors["primary"])]
        )


    def set_theme(self, theme_name):
        """Sets the current theme and applies it."""
        if theme_name in self.themes:
            self.current_theme = theme_name
            
            # Update component styles and state colors based on the new theme
            self.component_styles["button"]["font"] = (self.themes[self.current_theme]["font"], 10)
            self.component_styles["entry"]["font"] = (self.themes[self.current_theme]["font"], 10)
            self.component_styles["label"]["font"] = (self.themes[self.current_theme]["font"], 10)
            self.component_styles["combobox"]["font"] = (self.themes[self.current_theme]["font"], 10)
            self.component_styles["checkbutton"]["indicatorcolor"] = self.themes[self.current_theme]["background"]
            self.component_styles["checkbutton"]["font"] = (self.themes[self.current_theme]["font"], 10)
            
            self.state_colors["hover"]["primary"] = self._adjust_color_brightness(self.themes[self.current_theme]["primary"], 1.1)
            self.state_colors["hover"]["secondary"] = self._adjust_color_brightness(self.themes[self.current_theme]["secondary"], 1.1)
            self.state_colors["hover"]["success"] = self._adjust_color_brightness(self.themes[self.current_theme]["success"], 1.1)
            self.state_colors["hover"]["info"] = self._adjust_color_brightness(self.themes[self.current_theme]["info"], 1.1)
            self.state_colors["hover"]["warning"] = self._adjust_color_brightness(self.themes[self.current_theme]["warning"], 1.1)
            self.state_colors["hover"]["danger"] = self._adjust_color_brightness(self.themes[self.current_theme]["danger"], 1.1)
            
            self.state_colors["active"]["primary"] = self._adjust_color_brightness(self.themes[self.current_theme]["primary"], 0.9)
            self.state_colors["active"]["secondary"] = self._adjust_color_brightness(self.themes[self.current_theme]["secondary"], 0.9)
            self.state_colors["active"]["success"] = self._adjust_color_brightness(self.themes[self.current_theme]["success"], 0.9)
            self.state_colors["active"]["info"] = self._adjust_color_brightness(self.themes[self.current_theme]["info"], 0.9)
            self.state_colors["active"]["warning"] = self._adjust_color_brightness(self.themes[self.current_theme]["warning"], 0.9)
            self.state_colors["active"]["danger"] = self._adjust_color_brightness(self.themes[self.current_theme]["danger"], 0.9)
            
            # Update foreground colors
            self.state_colors["hover"]["foreground"] = self.themes[self.current_theme]["foreground"]
            self.state_colors["active"]["foreground"] = self.themes[self.current_theme]["foreground"]
            self.state_colors["disabled"]["background"] = self._adjust_color_opacity(self.themes[self.current_theme]["background"], 0.5)
            self.state_colors["disabled"]["foreground"] = self._adjust_color_opacity(self.themes[self.current_theme]["foreground"], 0.5)

            self.apply_theme()
            self.save_theme()
        else:
            print(f"Theme '{theme_name}' not found.")

    def get_theme_colors(self):
        """Returns colors based on the current theme"""
        return self.themes.get(self.current_theme, self.themes["nordic_frost"])

    def get_current_theme(self):
        return self.current_theme

    def get_available_themes(self):
        """Returns a list of available theme names."""
        return list(self.themes.keys())

class MainWindow(ttk.Window):
    """
    Manages the main application window.

    Attributes:
        menu_frame (ttk.Frame): Frame for the left-side menu.
        content_frame (ttk.Frame): Frame for the main content.
    """
    def __init__(self, title="GUI Library", theme="nordic_frost", **kwargs):
        """
        Initializes the main window.

        Args:
            title (str): Title of the window.
            theme (str): Custom theme name (will be applied after initialization).
            **kwargs: Additional keyword arguments for ttk.Window.
        """
        # Store custom theme name
        self._custom_theme = theme
        
        # Initialize with a valid ttkbootstrap theme
        super().__init__(title=title, themename="darkly", **kwargs)
        self.title(title)
        self.geometry("800x600")
        self.resizable(True, True)
        self.menu_frame = None
        self.content_frame = None
        self.theme_manager = ThemeManager()
        
        # Apply our custom theme
        if self._custom_theme:
            self.theme_manager.set_theme(self._custom_theme)
            
        self._setup_layout()

    def _setup_layout(self):
        """Sets up the layout of the main window."""
        self.menu_frame = ttk.Frame(self, width=200, bootstyle=SECONDARY)
        self.menu_frame.pack(side=LEFT, fill=Y, padx=5, pady=5)

        self.content_frame = ttk.Frame(self, bootstyle=LIGHT)
        self.content_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)

    def add_theme_selector(self, menu_frame):
        """Adds a theme selector to the menu."""
        theme_selector = CustomCombobox(menu_frame, values=self.theme_manager.get_available_themes(), bootstyle=INFO)
        theme_selector.set_value(self.theme_manager.get_current_theme())
        theme_selector.bind("<<ComboboxSelected>>", self._on_theme_selected)
        theme_selector.pack(fill=X, pady=5)

    def _on_theme_selected(self, event):
        """Handles theme selection."""
        selected_theme = event.widget.get()
        self.theme_manager.set_theme(selected_theme)
        self.update_ui()

    def update_ui(self):
        """Updates the UI elements after a theme change."""
        for child in self.content_frame.winfo_children():
            if isinstance(child, CustomElement):
                child.update_styles()

    def get_menu_frame(self):
        """Returns the menu frame."""
        return self.menu_frame

    def get_content_frame(self):
        """Returns the content frame."""
        return self.content_frame

    def run(self):
        """Runs the main loop of the application."""
        self.mainloop()


class LeftMenu:
    """
    Creates and manages the left-side menu.

    Attributes:
        menu_items (list): List of menu items.
        menu_frame (ttk.Frame): Frame for the menu.
    """
    def __init__(self, parent, **kwargs):
        """
        Initializes the left menu.

        Args:
            parent (ttk.Frame): Parent frame for the menu.
            **kwargs: Additional keyword arguments for ttk.Frame.
        """
        self.parent = parent
        self.menu_items = []
        self.menu_frame = ttk.Frame(self.parent, **kwargs)
        self.menu_frame.pack(side=LEFT, fill=Y, padx=5, pady=5)

    def add_menu_item(self, text, command, bootstyle=PRIMARY):
        """
        Adds a menu item to the menu.

        Args:
            text (str): Text of the menu item.
            command (function): Command to execute when the item is clicked.
            bootstyle (str): ttkbootstrap style for the button.
        """
        try:
            menu_item = CustomButton(self.menu_frame, text=text, command=command, bootstyle=bootstyle)
            menu_item.pack(fill=X, pady=5)
            self.menu_items.append(menu_item)
        except Exception as e:
            print(f"Error adding menu item: {e}")

    def get_menu_frame(self):
        """Returns the menu frame."""
        return self.menu_frame



class CustomElement:
    """
    Base class for customizable GUI elements.

    Attributes:
        element (ttk.Widget): The actual GUI element.
        config (dict): Configuration settings for the element.
    """
    def __init__(self, parent, **kwargs):
        """
        Initializes the custom element.

        Args:
            parent (ttk.Frame): Parent frame for the element.
            **kwargs: Initial configuration settings for the element.
        """
        self.parent = parent
        self.element = None
        self.config = kwargs
        self.theme_manager = ThemeManager()

    def set_config(self, **kwargs):
        """
        Sets or updates the configuration of the element.

        Args:
            **kwargs: Configuration settings to update.
        """
        self.config.update(kwargs)
        if self.element:
            self._apply_config()

    def _apply_config(self):
        """Applies the configuration to the element."""
        try:
            self.element.config(**self.config)
        except Exception as e:
            print(f"Error applying config: {e}")

    def _apply_styles(self, styles):
        """Applies the given styles to the element."""
        try:
            self.element.config(**styles)
        except Exception as e:
            print(f"Error applying styles: {e}")

    def update_styles(self):
        """Updates the styles of the element based on the current theme."""
        theme_colors = self.theme_manager.get_theme_colors()
        button_style = self.config.get('bootstyle', 'primary')
        
        # Correct mapping of bootstyle to theme colors
        if button_style in ["primary", "secondary", "success", "info", "warning", "danger"]:
            bg_color = theme_colors.get(button_style)
        else:
            bg_color = theme_colors.get("primary")

        self._apply_styles({
            "background": bg_color,
            "foreground": theme_colors.get("foreground")
        })


    def get_element(self):
        """Returns the GUI element."""
        return self.element

    def pack(self, **kwargs):
        """Packs the element into the parent frame."""
        if self.element:
            self.element.pack(**kwargs)

    def place(self, **kwargs):
        """Places the element into the parent frame."""
        if self.element:
            self.element.place(**kwargs)

    def grid(self, **kwargs):
        """Grids the element into the parent frame."""
        if self.element:
            self.element.grid(**kwargs)


class CustomButton(CustomElement):
    """
    Customizable button element.

    Inherits from CustomElement.
    """
    def __init__(self, parent, text, command, **kwargs):
        """
        Initializes the custom button.

        Args:
            parent (ttk.Frame): Parent frame for the button.
            text (str): Text of the button.
            command (function): Command to execute when the button is clicked.
            **kwargs: Additional configuration settings for the button.
        """
        super().__init__(parent, **kwargs)
        self.config.setdefault('bootstyle', 'primary')

        # Add ripple effect canvas
        self.ripple_canvas = tk.Canvas(self.parent, width=0, height=0, highlightthickness=0)
        self.ripple_canvas.place(x=0, y=0)  # Initial position doesn't matter

        try:
            self.element = ttk.Button(self.parent, text=text, command=lambda: self._on_click(command), **self.config)
            self._bind_hover_events()
        except Exception as e:
            print(f"Error creating button: {e}")

        self._apply_config()

    def _on_click(self, command):
        """Handles button click, creates ripple, and executes command."""
        self._create_ripple()
        if command:
            command()

    def _create_ripple(self):
        """Creates a ripple effect on the button."""
        theme_colors = self.theme_manager.get_theme_colors()
        x = self.element.winfo_width() // 2
        y = self.element.winfo_height() // 2
        max_radius = max(x, y)
        
        ripple_color = self._adjust_color_opacity(theme_colors.get("foreground"), 0.3)

        for i in range(max_radius):
            self.ripple_canvas.after(i * 20, lambda radius=i: self._draw_ripple(x, y, radius, ripple_color))

    def _draw_ripple(self, x, y, radius, color):
        """Draws a single frame of the ripple animation."""
        try:
            # Update canvas size and position
            self.ripple_canvas.config(width=self.element.winfo_width(), height=self.element.winfo_height())
            self.ripple_canvas.place(x=self.element.winfo_x(), y=self.element.winfo_y())
            
            # Create ripple circle with transparency
            oval_id = self.ripple_canvas.create_oval(
                x - radius, y - radius, 
                x + radius, y + radius, 
                outline="", 
                fill=color,
                stipple="gray50"  # This creates a transparency effect
            )
            
            # Schedule cleanup of the ripple
            self.ripple_canvas.after(500, lambda: self.ripple_canvas.delete(oval_id))
        except Exception as e:
            print(f"Error in ripple effect: {e}")

    def _bind_hover_events(self):
        """Add hover state handling"""
        self.element.bind('<Enter>', lambda e: self._on_hover(True))
        self.element.bind('<Leave>', lambda e: self._on_hover(False))
        self.element.bind("<ButtonPress-1>", lambda event: self._on_button_press())

    def _on_hover(self, is_hovering):
        """Handles hover events."""
        if is_hovering:
            self.element.config(cursor="hand2")
        else:
            self.element.config(cursor="")

    def _on_button_press(self):
        self._create_ripple()

    def update_styles(self):
        """Updates the styles of the label based on the current theme."""
        super().update_styles()
        theme_colors = self.theme_manager.get_theme_colors()
        
        label_style = self.config.get('bootstyle', None) # Get bootstyle if specified, otherwise none

        if label_style and "." in label_style:
             label_style = label_style.split(".")[0]
        
        if label_style in ["primary", "secondary", "success", "info", "warning", "danger"]:
            fg_color = theme_colors.get(label_style)
        elif label_style == "info":
            fg_color = theme_colors.get("info")
        else:
           fg_color = theme_colors.get("foreground")

        self._apply_styles({
            "background": theme_colors.get("background"),
             "foreground": fg_color
        })

    def _adjust_color_opacity(self, color, opacity):
        """Add opacity to a color (used for ripple effect)."""
        # Convert hex to RGB
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        
        # Return color with opacity as a valid Tkinter color
        return f'#{r:02x}{g:02x}{b:02x}'


class CustomLabel(CustomElement):
    """
    Customizable label element.

    Inherits from CustomElement.
    """
    def __init__(self, parent, text="", **kwargs):
        """
        Initializes the custom label.

        Args:
            parent (ttk.Frame): Parent frame for the label.
            text (str, optional): Text of the label. Defaults to empty if textvariable is provided.
            **kwargs: Additional configuration settings for the label.
        """
        super().__init__(parent, **kwargs)
        try:
            self.element = ttk.Label(self.parent, text=text, **self.config)
        except Exception as e:
            print(f"Error creating label: {e}")
        self._apply_config()




class CustomEntry(CustomElement):
    """
    Customizable entry element.

    Inherits from CustomElement.
    """
    def __init__(self, parent, **kwargs):
        """
        Initializes the custom entry.

        Args:
            parent (ttk.Frame): Parent frame for the entry.
            **kwargs: Additional configuration settings for the entry.
        """
        super().__init__(parent, **kwargs)
        
        try:
            # Create the entry element first
            self.element = ttk.Entry(self.parent)
            
            # Apply configuration
            self._apply_config()
            
            # Bind events after element is created and configured
            if self.element:
                self.element.bind("<FocusIn>", self._on_focus_in)
                self.element.bind("<FocusOut>", self._on_focus_out)
        except Exception as e:
            print(f"Error creating entry: {e}")
            self.element = None

    def _on_focus_in(self, event):
        """Handles focus in event."""
        theme_colors = self.theme_manager.get_theme_colors()
        self.element.config(insertcolor=theme_colors["primary"])  # Cursor color
        style = ttk.Style()
        style.map('TEntry',
            bordercolor=[('focus', theme_colors["primary"])]
        )

    def _on_focus_out(self, event):
        """Handles focus out event."""
        theme_colors = self.theme_manager.get_theme_colors()
        style = ttk.Style()
        style.map('TEntry',
            bordercolor=[('focus', theme_colors["primary"])]
        )

    def get_text(self):
        """Returns the text entered in the entry."""
        try:
            return self.element.get()
        except Exception as e:
            print(f"Error getting text: {e}")
            return ""


class CustomCombobox(CustomElement):
    """
    Customizable combobox element.

    Inherits from CustomElement.
    """
    def __init__(self, parent, values, **kwargs):
        """
        Initializes the custom combobox.

        Args:
            parent (ttk.Frame): Parent frame for the combobox.
            values (list): List of values for the combobox.
            **kwargs: Additional configuration settings for the combobox.
        """
        super().__init__(parent, **kwargs)
        try:
            self.element = ttk.Combobox(self.parent, values=values, state="readonly", **self.config)
            self.element.set(values[0])
        except Exception as e:
            print(f"Error creating combobox: {e}")
        self._apply_config()

    def get_value(self):
        """Returns the current value of the combobox."""
        try:
            return self.element.get()
        except Exception as e:
            print(f"Error getting value: {e}")
            return ""

    def set_value(self, value):
        """Sets the value of the combobox."""
        try:
            self.element.set(value)
        except Exception as e:
            print(f"Error setting value: {e}")

    def bind(self, sequence=None, func=None, add=None):
        """Binds an event to the combobox."""
        self.element.bind(sequence, func, add)



class CustomCheckbutton(CustomElement):
    """Customizable checkbutton element."""

    def __init__(self, parent, text, **kwargs):
        """
        Initializes the custom checkbutton.

        Args:
            parent (ttk.Frame): Parent frame for the checkbutton.
            text (str): Text of the checkbutton.
            **kwargs: Additional configuration settings for the checkbutton.
        """
        super().__init__(parent, **kwargs)
        self.var = tk.BooleanVar()
        try:
            self.element = ttk.Checkbutton(self.parent, text=text, variable=self.var, **self.config)
        except Exception as e:
            print(f"Error creating checkbutton: {e}")
        self._apply_config()

    def get_value(self):
        """Returns the current value (True/False) of the checkbutton."""
        return self.var.get()








if __name__ == '__main__':
    app = MainWindow(title="Styled GUI Library")  # Set initial theme here
    menu = LeftMenu(app.get_menu_frame(), bootstyle=SECONDARY)
    app.add_theme_selector(menu.get_menu_frame())
    menu.add_menu_item("Menu Item 1", lambda: print("Menu Item 1 Clicked"))
    menu.add_menu_item("Menu Item 2", lambda: print("Menu Item 2 Clicked"), bootstyle=SUCCESS)

    content_frame = app.get_content_frame()

    # Button Example
    button = CustomButton(content_frame, text="Click Me", command=lambda: print("Button Clicked"), bootstyle=SUCCESS, width=20)
    button.pack(pady=20)

    # Label Example
    label = CustomLabel(content_frame, text="This is a Label", font=("Arial", 16), bootstyle="info.TLabel", padding=10)
    label.pack(pady=20)

    # Entry Example
    entry = CustomEntry(content_frame, width=30, padding=10, bootstyle=PRIMARY)
    entry.pack(pady=20)

    def get_entry_text():
        print(f"Entry text: {entry.get_text()}")

    get_text_button = CustomButton(content_frame, text="Get Text", command=get_entry_text, bootstyle=SUCCESS)
    get_text_button.pack()

    # Combobox Example
    combo = CustomCombobox(content_frame, values=["Option 1", "Option 2", "Option 3"], width=20)
    combo.pack(pady=20)

    def get_combo_value():
      print(f"Combo value: {combo.get_value()}")

    get_combo_button = CustomButton(content_frame, text="Get Combo Value", command=get_combo_value, bootstyle=SUCCESS)
    get_combo_button.pack()

    # Checkbutton Example
    checkbutton = CustomCheckbutton(content_frame, text="Check me")
    checkbutton.pack(pady=20)

    def get_checkbutton_value():
        print(f"Checkbutton value: {checkbutton.get_value()}")

    get_checkbutton = CustomButton(content_frame, text="Get Check Value", command=get_checkbutton_value, bootstyle=SUCCESS)
    get_checkbutton.pack()

    app.run()