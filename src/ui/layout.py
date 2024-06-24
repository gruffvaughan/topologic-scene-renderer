import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from src.utils import select_color, rgb_to_hex, disableChildren, enableChildren
from src.animations import animation_functions
from src.easing import easing_functions


def create_layout(root):
    ############################################ HEADER

    frame_header = ttk.Frame(root)
    frame_header.pack(pady=(10, 10))

    original_image = Image.open("project/src/ui/images/topologicpy-logo.png")
    resized_image = original_image.resize((80, 80))
    root.logo_image = ImageTk.PhotoImage(resized_image)
    root.logo_label = ttk.Label(frame_header, image=root.logo_image)
    root.logo_label.pack(side=tk.LEFT, padx=(0, 10))

    ttk.Label(
        frame_header,
        text="TopologicPy\nAnimation\nRenderer",
        font=("TkDefaultFont", 16, "bold"),
    ).pack(side=tk.LEFT)
    ttk.Separator(root, orient="horizontal").pack(fill="x", pady=5)

    ################################ ANIMATION SETTINGS #################################

    root.frame_dropdowns = ttk.Frame(root)
    root.frame_dropdowns.pack(pady=(10, 10))

    frame_shape = ttk.Frame(root.frame_dropdowns)
    frame_shape.pack(side=tk.LEFT, pady=(0, 10), padx=(0, 20))

    frame_easing = ttk.Frame(root.frame_dropdowns)
    frame_easing.pack(side=tk.LEFT, pady=(0, 10), padx=(0, 0))

    animation_label = ttk.Label(frame_shape, text="Select Shape")
    animation_label.pack()
    root.animation_var = tk.StringVar(root)
    root.animation_dropdown = ttk.Combobox(
        frame_shape,
        textvariable=root.animation_var,
        values=list(animation_functions.keys()),
    )
    root.animation_dropdown.pack()

    easing_label = ttk.Label(frame_easing, text="Select Easing")
    easing_label.pack()
    root.easing_var = tk.StringVar(root)
    root.easing_dropdown = ttk.Combobox(
        frame_easing, textvariable=root.easing_var, values=list(easing_functions.keys())
    )
    root.easing_dropdown.pack()

    root.frame_styles = ttk.Frame(root)
    root.frame_styles.pack(fill="both", expand=True, padx=20, pady=20)

    box1 = ttk.LabelFrame(root.frame_styles, text="FACES")
    box1.pack(side="left", fill="both", padx=10)

    face_opacity_start_label = ttk.Label(box1, text="Opacity Start")
    face_opacity_start_label.pack()
    root.face_opacity_start_var = tk.DoubleVar(root, value=0.75)
    ttk.Entry(box1, textvariable=root.face_opacity_start_var).pack(
        pady=5, padx=10, fill="x"
    )

    face_opacity_end_label = ttk.Label(box1, text="Opacity End")
    face_opacity_end_label.pack()
    root.face_opacity_end_var = tk.DoubleVar(root, value=0.1)
    ttk.Entry(box1, textvariable=root.face_opacity_end_var).pack(
        pady=5, padx=10, fill="x"
    )

    frame_colorpicker = ttk.Frame(box1)
    root.face_color_sample_box = tk.Frame(
        frame_colorpicker, width=22, height=22, relief="solid", borderwidth=1
    )
    root.face_color_sample_box.pack(side=tk.LEFT)
    root.face_color_var = tk.StringVar(root, value="0, 0, 0")
    face_color_button = tk.Button(
        frame_colorpicker,
        text="Change Colour",
        command=lambda: select_color(
            root.face_color_sample_box,
            root.face_color_rgb_label,
            root.face_color_hex_label,
            root.face_color_var,
        ),
    )
    face_color_button.pack(side=tk.LEFT, fill="x")
    frame_colorpicker.pack(pady=(10, 10))

    root.face_color_rgb_label = tk.Label(box1, text="RGB: ")
    root.face_color_rgb_label.pack()
    root.face_color_hex_label = tk.Label(box1, text="HEX: ")
    root.face_color_hex_label.pack()

    root.face_color_rgb_label.config(text=f"RGB: {root.face_color_var.get()}")
    root.face_color_hex_label.config(
        text=f"HEX: {rgb_to_hex(root.face_color_var.get())}"
    )
    root.face_color_sample_box.config(bg=rgb_to_hex(root.face_color_var.get()))

    box2 = ttk.LabelFrame(root.frame_styles, text="EDGES")
    box2.pack(side="left", fill="both", padx=10)

    edge_opacity_label = ttk.Label(box2, text="Opacity")
    edge_opacity_label.pack()
    root.edge_opacity_var = tk.DoubleVar(root, value=1)
    ttk.Entry(box2, textvariable=root.edge_opacity_var).pack(pady=5, padx=10, fill="x")

    edge_width_label = ttk.Label(box2, text="Width")
    edge_width_label.pack()
    root.edge_width_var = tk.IntVar(root, value=2)
    ttk.Entry(box2, textvariable=root.edge_width_var).pack(pady=5, padx=10, fill="x")

    frame_colorpicker = ttk.Frame(box2)
    root.edge_color_sample_box = tk.Frame(
        frame_colorpicker, width=22, height=22, relief="solid", borderwidth=1
    )
    root.edge_color_sample_box.pack(side=tk.LEFT)
    root.edge_color_var = tk.StringVar(root, value="0, 0, 0")
    edge_color_button = tk.Button(
        frame_colorpicker,
        text="Change Colour",
        command=lambda: select_color(
            root.edge_color_sample_box,
            root.edge_color_rgb_label,
            root.edge_color_hex_label,
            root.edge_color_var,
        ),
    )
    edge_color_button.pack(side=tk.LEFT, fill="x")
    frame_colorpicker.pack(pady=(10, 10))

    root.edge_color_rgb_label = tk.Label(box2, text="RGB: ")
    root.edge_color_rgb_label.pack()
    root.edge_color_hex_label = tk.Label(box2, text="HEX: ")
    root.edge_color_hex_label.pack()

    root.edge_color_rgb_label.config(text=f"RGB: {root.edge_color_var.get()}")
    root.edge_color_hex_label.config(
        text=f"HEX: {rgb_to_hex(root.edge_color_var.get())}"
    )
    root.edge_color_sample_box.config(bg=rgb_to_hex(root.edge_color_var.get()))

    box3 = ttk.LabelFrame(root.frame_styles, text="VERTICES")
    box3.pack(side="left", fill="both", padx=10)

    vertex_opacity_label = ttk.Label(box3, text="Opacity")
    vertex_opacity_label.pack()
    root.vertex_opacity_var = tk.DoubleVar(root, value=1)
    ttk.Entry(box3, textvariable=root.vertex_opacity_var).pack(
        pady=5, padx=10, fill="x"
    )

    frame_colorpicker = ttk.Frame(box3)
    root.vertex_color_sample_box = tk.Frame(
        frame_colorpicker, width=22, height=22, relief="solid", borderwidth=1
    )
    root.vertex_color_sample_box.pack(side=tk.LEFT)
    root.vertex_color_var = tk.StringVar(root, value="255, 255, 255")
    vertex_color_button = tk.Button(
        frame_colorpicker,
        text="Change Colour",
        command=lambda: select_color(
            root.vertex_color_sample_box,
            root.vertex_color_rgb_label,
            root.vertex_color_hex_label,
            root.vertex_color_var,
        ),
    )
    vertex_color_button.pack(side=tk.LEFT, fill="x")
    frame_colorpicker.pack(pady=(10, 10))

    root.vertex_color_rgb_label = tk.Label(box3, text="RGB: ")
    root.vertex_color_rgb_label.pack()
    root.vertex_color_hex_label = tk.Label(box3, text="HEX: ")
    root.vertex_color_hex_label.pack()

    root.vertex_color_rgb_label.config(text=f"RGB: {root.vertex_color_var.get()}")
    root.vertex_color_hex_label.config(
        text=f"HEX: {rgb_to_hex(root.vertex_color_var.get())}"
    )
    root.vertex_color_sample_box.config(bg=rgb_to_hex(root.vertex_color_var.get()))

    box4 = ttk.LabelFrame(root.frame_styles, text="BACKGROUND")
    box4.pack(side="left", fill="both", padx=10)

    bg_opacity_label = ttk.Label(box4, text="Opacity")
    bg_opacity_label.pack()
    root.bg_opacity_var = tk.DoubleVar(root, value=1)
    ttk.Entry(box4, textvariable=root.bg_opacity_var).pack(pady=5, padx=10, fill="x")

    frame_colorpicker = ttk.Frame(box4)
    root.bg_color_sample_box = tk.Frame(
        frame_colorpicker, width=22, height=22, relief="solid", borderwidth=1
    )
    root.bg_color_sample_box.pack(side=tk.LEFT)
    root.bg_color_var = tk.StringVar(root, value="255, 255, 255")
    bg_color_button = tk.Button(
        frame_colorpicker,
        text="Change Colour",
        command=lambda: select_color(
            root.bg_color_sample_box,
            root.bg_color_rgb_label,
            root.bg_color_hex_label,
            root.bg_color_var,
        ),
    )
    bg_color_button.pack(side=tk.LEFT, fill="x")
    frame_colorpicker.pack(pady=(10, 10))

    root.bg_color_rgb_label = tk.Label(box4, text="RGB: ")
    root.bg_color_rgb_label.pack()
    root.bg_color_hex_label = tk.Label(box4, text="HEX: ")
    root.bg_color_hex_label.pack()

    root.bg_color_rgb_label.config(text=f"RGB: {root.bg_color_var.get()}")
    root.bg_color_hex_label.config(text=f"HEX: {rgb_to_hex(root.bg_color_var.get())}")
    root.bg_color_sample_box.config(bg=rgb_to_hex(root.bg_color_var.get()))

    ##################################### SEQUENCE SETTINGS #################################

    ttk.Label(root, text="Sequence Settings", font=("TkDefaultFont", 12, "bold")).pack(
        pady=(20, 5)
    )
    ttk.Separator(root, orient="horizontal").pack(fill="x", pady=5)

    root.frame_settings = ttk.Frame(root)
    root.frame_settings.pack(pady=20)

    # Sequence Name Entry
    filename_prefix_label = ttk.Label(root.frame_settings, text="File Name Prefix")
    filename_prefix_label.pack()
    root.filename_prefix_var = tk.StringVar(root)
    root.filename_prefix_entry = ttk.Entry(
        root.frame_settings,
        textvariable=root.filename_prefix_var,
        width=30,
        justify="center",
    )
    root.filename_prefix_entry.pack(pady=(0, 10))

    image_size_label = ttk.Label(
        root.frame_settings, text="Topologic Export Size (w x h):"
    )
    image_size_label.pack()

    image_size_frame = ttk.Frame(root.frame_settings)
    image_size_frame.pack(pady=(0, 10))

    root.image_width_var = tk.IntVar(root, value=3840)
    root.image_width_entry = ttk.Entry(
        image_size_frame, textvariable=root.image_width_var, width=10
    )
    root.image_width_entry.pack(side=tk.LEFT)
    ttk.Label(image_size_frame, text="x").pack(side=tk.LEFT, padx=5)
    root.image_height_var = tk.IntVar(root, value=2160)
    root.image_height_entry = ttk.Entry(
        image_size_frame, textvariable=root.image_height_var, width=10
    )
    root.image_height_entry.pack(side=tk.LEFT)

    checkboxes_frame = ttk.Frame(root.frame_settings)
    checkboxes_frame.pack(pady=(0, 10))

    root.render_video_var = tk.BooleanVar(checkboxes_frame, value=True)
    root.render_video_checkbox = ttk.Checkbutton(
        checkboxes_frame, text="Render Video?", variable=root.render_video_var
    )
    root.render_video_checkbox.pack(side=tk.LEFT, padx=10)

    root.render_reverse_var = tk.BooleanVar(checkboxes_frame, value=True)
    root.render_reverse_checkbox = ttk.Checkbutton(
        checkboxes_frame, text="Render w/ Reverse?", variable=root.render_reverse_var
    )
    root.render_reverse_checkbox.pack(side=tk.LEFT, padx=10)

    video_format_label = ttk.Label(root.frame_settings, text="Video Format:")
    video_format_label.pack(pady=(0, 0))

    radio_frame = ttk.Frame(root.frame_settings)
    radio_frame.pack(pady=(0, 10))

    root.video_format_var = tk.StringVar(radio_frame, value="mp4")
    root.radio_mp4 = ttk.Radiobutton(
        radio_frame, text="MP4", variable=root.video_format_var, value="mp4"
    )
    root.radio_mp4.pack(side=tk.LEFT, padx=10, pady=0)
    root.radio_gif = ttk.Radiobutton(
        radio_frame, text="GIF", variable=root.video_format_var, value="gif"
    )
    root.radio_gif.pack(side=tk.LEFT, padx=10, pady=0)

    style = ttk.Style()
    style.configure("Custom.TFrame", borderwidth=10, relief="groove")
    frame_MP4_settings = ttk.Frame(root.frame_settings, style="Custom.TFrame")
    frame_MP4_settings.pack(pady=(10, 10), padx=(0, 0))

    fps_label = ttk.Label(frame_MP4_settings, text="Frames per Second (FPS):")
    fps_label.pack()
    root.fps_var = tk.IntVar(root, value=25)
    root.fps_entry = ttk.Entry(frame_MP4_settings, textvariable=root.fps_var)
    root.fps_entry.pack()

    duration_label = ttk.Label(frame_MP4_settings, text="Duration (seconds):")
    duration_label.pack()
    root.duration_var = tk.IntVar(root, value=3)
    root.duration_entry = ttk.Entry(frame_MP4_settings, textvariable=root.duration_var)
    root.duration_entry.pack()

    video_size_label = ttk.Label(frame_MP4_settings, text="Video Size (w x h):")
    video_size_label.pack()
    video_size_frame = ttk.Frame(frame_MP4_settings)
    video_size_frame.pack()
    root.video_width_var = tk.IntVar(root, value=1920)
    root.video_width_entry = ttk.Entry(
        video_size_frame, textvariable=root.video_width_var, width=10
    )
    root.video_width_entry.pack(side=tk.LEFT)
    ttk.Label(video_size_frame, text="x").pack(side=tk.LEFT, padx=5)
    root.video_height_var = tk.IntVar(root, value=1080)
    root.video_height_entry = ttk.Entry(
        video_size_frame, textvariable=root.video_height_var, width=10
    )
    root.video_height_entry.pack(side=tk.LEFT)

    ##################################################### OUTPUT #####################################################

    ttk.Label(root, text="Output", font=("TkDefaultFont", 12, "bold")).pack(
        pady=(20, 5)
    )
    ttk.Separator(root, orient="horizontal").pack(fill="x", pady=5)

    root.frame_outputs = ttk.Frame(root)
    root.frame_outputs.pack(pady=(0, 10))

    output_folder_label = ttk.Label(
        root.frame_outputs, text="Select Image Sequence Folder:"
    )
    output_folder_label.pack()

    frame_image_folder = ttk.Frame(root.frame_outputs)
    frame_image_folder.pack(pady=(0, 10))

    root.output_folder_var = tk.StringVar(root)
    root.output_folder_entry = ttk.Entry(
        frame_image_folder,
        textvariable=root.output_folder_var,
        width=75,
        justify="center",
    )
    root.output_folder_entry.pack(side=tk.LEFT)
    output_folder_button = ttk.Button(
        frame_image_folder, text="Browse", command=root.select_output_folder
    )
    output_folder_button.pack(side=tk.LEFT)

    video_folder_label = ttk.Label(root.frame_outputs, text="Select Video Folder:")
    video_folder_label.pack()

    frame_video_folder = ttk.Frame(root.frame_outputs)
    frame_video_folder.pack(pady=(0, 10))

    root.video_folder_var = tk.StringVar(root)
    root.video_folder_entry = ttk.Entry(
        frame_video_folder,
        textvariable=root.video_folder_var,
        width=75,
        justify="center",
    )
    root.video_folder_entry.pack(side=tk.LEFT)
    video_folder_button = ttk.Button(
        frame_video_folder, text="Browse", command=root.select_video_folder
    )
    video_folder_button.pack(side=tk.LEFT)

    frame_render_buttons = ttk.Frame(root.frame_outputs)
    frame_render_buttons.pack(pady=10)

    root.render_button = ttk.Button(
        frame_render_buttons, text="Render", command=root.render_animation
    )
    root.render_button.pack(side=tk.LEFT, padx=10)
    root.cancel_button = ttk.Button(
        frame_render_buttons,
        text="Cancel",
        command=root.cancel_rendering,
        state="disabled",
    )
    root.cancel_button.pack(side=tk.LEFT, padx=10)

    root.frame_progress = ttk.Frame(root)
    root.frame_progress.pack(pady=(0, 0))

    root.progress = ttk.Progressbar(
        root.frame_progress, orient="horizontal", length=200, mode="determinate"
    )
    root.progress.pack()
    root.status_label = ttk.Label(
        root.frame_progress, text="Ready", font=("TkDefaultFont", 8), state="disabled"
    )
    root.status_label.pack(pady=(5, 20))


def disable_ui(root):
    disableChildren(root.frame_dropdowns)
    disableChildren(root.frame_styles)
    disableChildren(root.frame_settings)
    disableChildren(root.frame_outputs)
    root.render_button.config(state="disabled")


def enable_ui(root):
    enableChildren(root.frame_dropdowns)
    enableChildren(root.frame_styles)
    enableChildren(root.frame_settings)
    enableChildren(root.frame_outputs)
    root.render_button.config(state="normal")
