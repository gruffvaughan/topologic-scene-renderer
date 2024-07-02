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


def disableChildren(parent):
    for child in parent.winfo_children():
        if isinstance(child, (ctk.CTkFrame)):
            disableChildren(child)
        elif isinstance(child, ctk.CTkComboBox):
            child.configure(state="readonly")
            child._state = "disabled"
            child._entry.configure(state="disabled")
        elif isinstance(child, ctk.CTkOptionMenu):
            child.configure(state="disabled")
        else:
            try:
                child.configure(state="disabled")
            except tk.TclError:
                print(f"Cannot disable {child}")


def enableChildren(parent):
    for child in parent.winfo_children():
        if isinstance(child, (ctk.CTkFrame)):
            enableChildren(child)
        elif isinstance(child, ctk.CTkComboBox):
            child.configure(state="readonly")
            child._state = "normal"
            child._entry.configure(state="normal")
        elif isinstance(child, ctk.CTkOptionMenu):
            child.configure(state="normal")
        else:
            try:
                child.configure(state="normal")
            except tk.TclError:
                print(f"Cannot enable {child}")
