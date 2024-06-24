import os
from tkinter import colorchooser


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
            color_rgb_label.config(text=f"RGB: {color_rgb}")
        if color_hex_label:
            color_hex_label.config(text=f"HEX: {color_hex}")
        sample_box.config(bg=color_hex)
        color_var.set(color_rgb)


def rgb_to_hex(rgb_color):
    rgb_values = [int(x.strip()) for x in rgb_color.split(",")]
    return f"#{rgb_values[0]:02x}{rgb_values[1]:02x}{rgb_values[2]:02x}"


def disableChildren(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        if wtype not in ("Frame", "Labelframe", "TFrame", "TLabelframe"):
            child.configure(state="disable")
        else:
            disableChildren(child)


def enableChildren(parent):
    for child in parent.winfo_children():
        wtype = child.winfo_class()
        if wtype == "OptionMenu":
            child.configure(state="readonly")
        elif wtype == "TCombobox":
            child.configure(state="readonly")
        elif wtype not in ("Frame", "Labelframe", "TFrame", "TLabelframe"):
            child.configure(state="normal")
        else:
            enableChildren(child)
