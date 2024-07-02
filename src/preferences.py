import json
import os

from src.utils import rgb_to_hex


def save_preferences(root):
    preferences = {
        "animation": root.animation_var.get(),
        "easing": root.easing_var.get(),
        "filename_prefix": root.filename_prefix_var.get(),
        "output_folder": root.output_folder_var.get(),
        "video_folder": root.video_folder_var.get(),
        "fps": root.fps_var.get(),
        "duration": root.duration_var.get(),
        "image_width": root.image_width_var.get(),
        "image_height": root.image_height_var.get(),
        "render_video": root.render_video_var.get(),
        "render_reverse": root.render_reverse_var.get(),
        "video_format": root.video_format_var.get(),
        "video_width": root.video_width_var.get(),
        "video_height": root.video_height_var.get(),
        "face_opacity_start": root.face_opacity_start_var.get(),
        "face_opacity_end": root.face_opacity_end_var.get(),
        "face_color": root.face_color_var.get(),
        "edge_color": root.edge_color_var.get(),
        "edge_opacity": root.edge_opacity_var.get(),
        "edge_width": root.edge_width_var.get(),
        "vertex_color": root.vertex_color_var.get(),
        "vertex_opacity": root.vertex_opacity_var.get(),
        "bg_color": root.bg_color_var.get(),
        "bg_opacity": root.bg_opacity_var.get(),
    }
    with open("settings/preferences.json", "w") as file:
        json.dump(preferences, file)


def load_preferences(root):
    default_preferences = {
        "animation": "Twist",
        "easing": "Ease In & Out, Cubic",
        "filename_prefix": "",
        "output_folder": "",
        "video_folder": "",
        "fps": 25,
        "duration": 2,
        "image_width": 1080,
        "image_height": 1080,
        "render_video": True,
        "render_reverse": True,
        "video_format": "mp4",
        "video_width": 1080,
        "video_height": 1080,
        "face_opacity_start": 0.75,
        "face_opacity_end": 0.1,
        "face_color": "128, 255, 255",
        "edge_color": "0, 0, 0",
        "edge_opacity": 1.0,
        "edge_width": 2,
        "vertex_color": "255, 255, 255",
        "vertex_opacity": 0.0,
        "bg_color": "255, 255, 255",
        "bg_opacity": 1.0,
    }

    preferences_file = "settings/preferences.json"

    if os.path.exists(preferences_file):
        with open(preferences_file, "r") as f:
            preferences = json.load(f)
    else:
        preferences = default_preferences

    root.animation_var.set(preferences["animation"])
    root.easing_var.set(preferences["easing"])
    root.filename_prefix_var.set(preferences["filename_prefix"])
    root.output_folder_var.set(preferences["output_folder"])
    root.video_folder_var.set(preferences["video_folder"])
    root.fps_var.set(preferences["fps"])
    root.duration_var.set(preferences["duration"])
    root.image_width_var.set(preferences["image_width"])
    root.image_height_var.set(preferences["image_height"])
    root.render_video_var.set(preferences["render_video"])
    root.render_reverse_var.set(preferences["render_reverse"])
    root.video_format_var.set(preferences["video_format"])
    root.video_width_var.set(preferences["video_width"])
    root.video_height_var.set(preferences["video_height"])
    root.face_opacity_start_var.set(preferences["face_opacity_start"])
    root.face_opacity_end_var.set(preferences["face_opacity_end"])
    root.face_color_var.set(preferences["face_color"])
    root.edge_color_var.set(preferences["edge_color"])
    root.edge_opacity_var.set(preferences["edge_opacity"])
    root.edge_width_var.set(preferences["edge_width"])
    root.vertex_color_var.set(preferences["vertex_color"])
    root.vertex_opacity_var.set(preferences["vertex_opacity"])
    root.bg_color_var.set(preferences["bg_color"])
    root.bg_opacity_var.set(preferences["bg_opacity"])

    root.face_color_rgb_label.config(text=f"RGB: {root.face_color_var.get()}")
    root.face_color_hex_label.config(
        text=f"HEX: {rgb_to_hex(root.face_color_var.get())}"
    )
    root.face_color_sample_box.config(bg=rgb_to_hex(root.face_color_var.get()))
    root.edge_color_rgb_label.config(text=f"RGB: {root.edge_color_var.get()}")
    root.edge_color_hex_label.config(
        text=f"HEX: {rgb_to_hex(root.edge_color_var.get())}"
    )
    root.edge_color_sample_box.config(bg=rgb_to_hex(root.edge_color_var.get()))
    root.vertex_color_rgb_label.config(text=f"RGB: {root.vertex_color_var.get()}")
    root.vertex_color_hex_label.config(
        text=f"HEX: {rgb_to_hex(root.vertex_color_var.get())}"
    )
    root.vertex_color_sample_box.config(bg=rgb_to_hex(root.vertex_color_var.get()))
    root.bg_color_rgb_label.config(text=f"RGB: {root.bg_color_var.get()}")
    root.bg_color_hex_label.config(text=f"HEX: {rgb_to_hex(root.bg_color_var.get())}")
    root.bg_color_sample_box.config(bg=rgb_to_hex(root.bg_color_var.get()))
