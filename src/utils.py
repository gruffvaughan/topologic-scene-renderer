import os
import tkinter as tk
from tkinter import colorchooser
import customtkinter as ctk


def get_next_version(folder, filename_prefix, selected_animation):
    version = 1

    # Check if filename_prefix is not empty
    if filename_prefix:
        prefix = f"{filename_prefix}_"
    else:
        prefix = ""

    while True:
        version_folder = f"{prefix}{selected_animation}_v{version:03d}"
        full_path = os.path.join(folder, version_folder)
        if not os.path.exists(full_path):
            return full_path, version
        version += 1


def select_color(sample_box, color_rgb_label, color_hex_label, color_var):
    color = colorchooser.askcolor()
    if color[0]:
        color_rgb = f"{int(color[0][0])}, {int(color[0][1])}, {int(color[0][2])}"
        color_hex = color[1]
        if color_rgb_label:
            color_rgb_label.configure(text=f"RGB: {color_rgb}")
        if color_hex_label:
            color_hex_label.configure(text=f"HEX: {color_hex}")
        sample_box.configure(fg_color=color_hex)
        color_var.set(color_rgb)


def rgb_to_hex(rgb_color):
    rgb_values = [int(x.strip()) for x in rgb_color.split(",")]
    return f"#{rgb_values[0]:02x}{rgb_values[1]:02x}{rgb_values[2]:02x}"


def _set_widget_state(widget, state):
    try:
        if isinstance(widget, ctk.CTkLabel):
            # For labels, we'll change the text color instead of the state
            text_color = "gray" if state == "disabled" else ("gray10", "gray90")
            widget.configure(text_color=text_color)
        elif isinstance(widget, ctk.CTkFrame):
            # For frames, we need to recurse into their children
            for child in widget.winfo_children():
                _set_widget_state(child, state)
        elif isinstance(widget, ctk.CTkComboBox):
            if state == "disabled":
                widget.configure(
                    state="disabled",
                    button_color="gray",
                    button_hover_color="gray",
                    border_color="gray",
                    text_color="gray",
                )
            else:
                widget.configure(
                    state="normal",
                    button_color=("gray75", "gray25"),  # default colors
                    button_hover_color=("gray70", "gray30"),  # default colors
                    border_color=("gray40", "gray60"),  # default colors
                    text_color=("gray10", "gray90"),  # default colors
                )
        elif isinstance(widget, ctk.CTkEntry):
            # For Entry widgets, we'll change both the state and the text color
            text_color = "gray" if state == "disabled" else ("gray10", "gray90")
            widget.configure(state=state, text_color=text_color)
        else:
            # For most widgets, we can simply set the state
            widget.configure(state=state)
    except Exception as e:
        print(f"Cannot {'disable' if state == 'disabled' else 'enable'} {widget}: {e}")


def disableChildren(parent):
    _set_widget_state(parent, "disabled")


def enableChildren(parent):
    _set_widget_state(parent, "normal")
