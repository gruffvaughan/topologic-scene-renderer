import customtkinter as ctk
from PIL import Image, ImageTk

from src.utils import select_color, rgb_to_hex, disableChildren, enableChildren
from src.animations import animation_functions
from src.easing import easing_functions


def create_layout(root):
    ############################################ HEADER

    frame_header = ctk.CTkFrame(root, fg_color="transparent")
    frame_header.pack(pady=(10, 10))

    light_image = Image.open("src/ui/images/topologicpy-logo.png")
    dark_image = Image.open("src/ui/images/topologicpy-logo-dark.png")
    root.logo_image = ctk.CTkImage(
        light_image=light_image, dark_image=dark_image, size=(80, 80)
    )
    root.logo_label = ctk.CTkLabel(
        frame_header, image=root.logo_image, text="", compound="left"
    )
    root.logo_label.pack(side=ctk.LEFT, padx=(0, 10))

    ctk.CTkLabel(
        frame_header,
        text="topologicpy\nScene\nRenderer",
        font=("TkDefaultFont", 16, "bold"),
        justify="left",
        height=80,
        anchor="center",
    ).pack()

    ################################ ANIMATION SETTINGS #################################

    ctk.CTkLabel(root, text="Scene Settings", font=("", 14, "bold")).pack(pady=(20, 0))

    root.frame_dropdowns = ctk.CTkFrame(root, fg_color="transparent")
    root.frame_dropdowns.pack(pady=(10, 10))

    frame_shape = ctk.CTkFrame(root.frame_dropdowns)
    frame_shape.pack(side=ctk.LEFT, pady=(0, 5), padx=(0, 20))

    frame_easing = ctk.CTkFrame(root.frame_dropdowns)
    frame_easing.pack(side=ctk.LEFT, pady=(0, 5), padx=(0, 0))

    animation_label = ctk.CTkLabel(
        frame_shape, text="Select Shape", fg_color="transparent"
    )
    animation_label.pack()
    root.animation_var = ctk.StringVar(root)
    root.animation_dropdown = ctk.CTkComboBox(
        frame_shape,
        variable=root.animation_var,
        values=list(animation_functions.keys()),
        width=300,
    )
    root.animation_dropdown.pack()

    easing_label = ctk.CTkLabel(
        frame_easing, text="Select Easing", fg_color="transparent"
    )
    easing_label.pack()
    root.easing_var = ctk.StringVar(root)
    root.easing_dropdown = ctk.CTkComboBox(
        frame_easing,
        variable=root.easing_var,
        values=list(easing_functions.keys()),
        width=300,
    )
    root.easing_dropdown.pack()

    root.frame_styles = ctk.CTkFrame(root, fg_color="transparent")
    root.frame_styles.pack(fill="both", padx=20, pady=(10, 0))

    # FACES
    box1 = ctk.CTkFrame(root.frame_styles)
    box1.pack(side="left", fill="both", padx=10, pady=0)

    ctk.CTkLabel(
        box1,
        text="FACES",
        text_color="#808080",
        justify="center",
        fg_color="transparent",
    ).grid(column=0, row=0, columnspan=2, pady=(0, 0))

    ctk.CTkLabel(
        box1, pady=3, text="Opacity\nStart", justify="center", font=("", 12)
    ).grid(column=0, row=1)
    ctk.CTkLabel(
        box1, pady=3, text="Opacity\nEnd", justify="center", font=("", 12)
    ).grid(column=1, row=1)
    root.face_opacity_start_var = ctk.DoubleVar(root, value=0.75)
    ctk.CTkEntry(
        box1, width=60, justify="center", textvariable=root.face_opacity_start_var
    ).grid(column=0, row=2, pady=(0, 10), padx=(10, 0))
    root.face_opacity_end_var = ctk.DoubleVar(root, value=0.10)
    ctk.CTkEntry(
        box1, width=60, justify="center", textvariable=root.face_opacity_end_var
    ).grid(column=1, row=2, pady=(0, 10), padx=(5, 10))

    frame_colorpicker1 = ctk.CTkFrame(box1)
    frame_colorpicker1.grid(
        column=0, row=3, columnspan=2, sticky="ew", padx=10, pady=(0, 10)
    )
    frame_colorpicker1.grid_columnconfigure(1, weight=1)

    root.face_color_sample_box = ctk.CTkFrame(
        frame_colorpicker1, width=22, height=22, border_width=1
    )
    root.face_color_sample_box.grid(column=0, row=0)

    root.face_color_var = ctk.StringVar(root, value="0, 0, 0")
    ctk.CTkButton(
        frame_colorpicker1,
        text="Change Colour",
        command=lambda: select_color(
            root.face_color_sample_box,
            root.face_color_rgb_label,
            root.face_color_hex_label,
            root.face_color_var,
        ),
        height=15,
        width=20,
    ).grid(column=1, row=0, sticky="ew")

    root.face_color_rgb_label = ctk.CTkLabel(
        box1, text="RGB: ", text_color="#808080", anchor="w", height=3
    )
    root.face_color_rgb_label.grid(column=0, row=4, columnspan=2, sticky="w", padx=10)
    root.face_color_hex_label = ctk.CTkLabel(
        box1, text="HEX: ", text_color="#808080", anchor="w", height=3
    )
    root.face_color_hex_label.grid(
        column=0, row=5, columnspan=2, sticky="w", padx=10, pady=(0, 10)
    )

    # EDGES
    box2 = ctk.CTkFrame(root.frame_styles)
    box2.pack(side="left", fill="both", padx=10)

    ctk.CTkLabel(
        box2,
        text="EDGES",
        text_color="#808080",
        justify="center",
        fg_color="transparent",
    ).grid(column=0, row=0, columnspan=2, pady=(0, 5))

    ctk.CTkLabel(box2, text="Opacity", justify="center", font=("", 12)).grid(
        column=0, row=1
    )
    ctk.CTkLabel(box2, text="Width", justify="center", font=("", 12)).grid(
        column=1, row=1
    )
    root.edge_opacity_var = ctk.DoubleVar(root, value=1.0)
    ctk.CTkEntry(
        box2, width=60, justify="center", textvariable=root.edge_opacity_var
    ).grid(column=0, row=2, pady=(0, 10), padx=(10, 5))
    root.edge_width_var = ctk.DoubleVar(root, value=2)
    ctk.CTkEntry(
        box2, width=60, justify="center", textvariable=root.edge_width_var
    ).grid(column=1, row=2, pady=(0, 10), padx=(5, 10))

    frame_colorpicker2 = ctk.CTkFrame(box2)
    frame_colorpicker2.grid(
        column=0, row=3, columnspan=2, sticky="ew", padx=10, pady=(0, 10)
    )
    frame_colorpicker2.grid_columnconfigure(1, weight=1)

    root.edge_color_sample_box = ctk.CTkFrame(
        frame_colorpicker2, width=22, height=22, border_width=1
    )
    root.edge_color_sample_box.grid(column=0, row=0)

    root.edge_color_var = ctk.StringVar(root, value="0, 0, 0")
    ctk.CTkButton(
        frame_colorpicker2,
        text="Change Colour",
        command=lambda: select_color(
            root.edge_color_sample_box,
            root.edge_color_rgb_label,
            root.edge_color_hex_label,
            root.edge_color_var,
        ),
        height=15,
        width=20,
    ).grid(column=1, row=0, sticky="ew")

    root.edge_color_rgb_label = ctk.CTkLabel(
        box2, text="RGB: ", text_color="#808080", anchor="w", height=3
    )
    root.edge_color_rgb_label.grid(column=0, row=4, columnspan=2, sticky="w", padx=10)
    root.edge_color_hex_label = ctk.CTkLabel(
        box2, text="HEX: ", text_color="#808080", anchor="w", height=3
    )
    root.edge_color_hex_label.grid(
        column=0, row=5, columnspan=2, sticky="w", padx=10, pady=(0, 10)
    )

    # VERTICES
    box3 = ctk.CTkFrame(root.frame_styles)
    box3.pack(side="left", fill="both", padx=10)

    ctk.CTkLabel(
        box3,
        text="VERTICES",
        text_color="#808080",
        justify="center",
        fg_color="transparent",
    ).grid(column=0, row=0, columnspan=2, pady=(0, 5))

    ctk.CTkLabel(box3, text="Opacity", justify="center", font=("", 12)).grid(
        column=0, row=1, columnspan=2
    )
    root.vertex_opacity_var = ctk.DoubleVar(root, value=1.0)
    ctk.CTkEntry(
        box3, width=60, justify="center", textvariable=root.vertex_opacity_var
    ).grid(column=0, row=2, columnspan=2, pady=(0, 10), padx=(10, 5))

    frame_colorpicker3 = ctk.CTkFrame(box3)
    frame_colorpicker3.grid(
        column=0, row=3, columnspan=2, sticky="ew", padx=10, pady=(0, 10)
    )
    frame_colorpicker3.grid_columnconfigure(1, weight=1)

    root.vertex_color_sample_box = ctk.CTkFrame(
        frame_colorpicker3, width=22, height=22, border_width=1
    )
    root.vertex_color_sample_box.grid(column=0, row=0)

    root.vertex_color_var = ctk.StringVar(root, value="0, 0, 0")
    ctk.CTkButton(
        frame_colorpicker3,
        text="Change Colour",
        command=lambda: select_color(
            root.vertex_color_sample_box,
            root.vertex_color_rgb_label,
            root.vertex_color_hex_label,
            root.vertex_color_var,
        ),
        height=15,
        width=20,
    ).grid(column=1, row=0, sticky="ew")

    root.vertex_color_rgb_label = ctk.CTkLabel(
        box3, text="RGB: ", text_color="#808080", anchor="w", height=3
    )
    root.vertex_color_rgb_label.grid(column=0, row=4, columnspan=2, sticky="w", padx=10)
    root.vertex_color_hex_label = ctk.CTkLabel(
        box3, text="HEX: ", text_color="#808080", anchor="w", height=3
    )
    root.vertex_color_hex_label.grid(
        column=0, row=5, columnspan=2, sticky="w", padx=10, pady=(0, 10)
    )

    # BACKGROUND
    box4 = ctk.CTkFrame(root.frame_styles)
    box4.pack(side="left", fill="both", padx=10)

    ctk.CTkLabel(
        box4,
        text="BACKGROUND",
        text_color="#808080",
        justify="center",
        fg_color="transparent",
    ).grid(column=0, row=0, columnspan=2, pady=(0, 5))

    ctk.CTkLabel(box4, text="Opacity", justify="center", font=("", 12)).grid(
        column=0, row=1, columnspan=2
    )
    root.bg_opacity_var = ctk.DoubleVar(root, value=1.0)
    ctk.CTkEntry(
        box4, width=60, justify="center", textvariable=root.bg_opacity_var
    ).grid(column=0, row=2, columnspan=2, pady=(0, 10), padx=(10, 5))

    frame_colorpicker4 = ctk.CTkFrame(box4)
    frame_colorpicker4.grid(
        column=0, row=3, columnspan=2, sticky="ew", padx=10, pady=(0, 10)
    )
    frame_colorpicker4.grid_columnconfigure(1, weight=1)

    root.bg_color_sample_box = ctk.CTkFrame(
        frame_colorpicker4, width=22, height=22, border_width=1
    )
    root.bg_color_sample_box.grid(column=0, row=0)

    root.bg_color_var = ctk.StringVar(root, value="0, 0, 0")
    ctk.CTkButton(
        frame_colorpicker4,
        text="Change Colour",
        command=lambda: select_color(
            root.bg_color_sample_box,
            root.bg_color_rgb_label,
            root.bg_color_hex_label,
            root.bg_color_var,
        ),
        height=15,
        width=20,
    ).grid(column=1, row=0, sticky="ew")

    root.bg_color_rgb_label = ctk.CTkLabel(
        box4, text="RGB: ", text_color="#808080", anchor="w", height=3
    )
    root.bg_color_rgb_label.grid(column=0, row=4, columnspan=2, sticky="w", padx=10)
    root.bg_color_hex_label = ctk.CTkLabel(
        box4, text="HEX: ", text_color="#808080", anchor="w", height=3
    )
    root.bg_color_hex_label.grid(
        column=0, row=5, columnspan=2, sticky="w", padx=10, pady=(0, 10)
    )

    ##################################### SEQUENCE SETTINGS #################################

    ctk.CTkLabel(root, text="Sequence Settings", font=("", 14, "bold")).pack(
        pady=(20, 5)
    )

    root.frame_settings = ctk.CTkFrame(root)
    root.frame_settings.pack(pady=(0, 0))

    # Sequence Name Entry
    filename_prefix_label = ctk.CTkLabel(
        root.frame_settings, text="File Name Prefix (Optional)", font=("", 12)
    )
    filename_prefix_label.pack()
    root.filename_prefix_var = ctk.StringVar(root)
    root.filename_prefix_entry = ctk.CTkEntry(
        root.frame_settings,
        textvariable=root.filename_prefix_var,
        width=220,
        justify="center",
    )
    root.filename_prefix_entry.pack(pady=(0, 10), padx=30)

    image_size_label = ctk.CTkLabel(
        root.frame_settings, text="Topologic Export Size (w x h):", font=("", 12)
    )
    image_size_label.pack()

    image_size_frame = ctk.CTkFrame(root.frame_settings, fg_color="transparent")
    image_size_frame.pack(pady=(0, 10))

    root.image_width_var = ctk.IntVar(root, value=3840)
    root.image_width_entry = ctk.CTkEntry(
        image_size_frame, textvariable=root.image_width_var, width=100, justify="center"
    )
    root.image_width_entry.pack(side=ctk.LEFT)
    ctk.CTkLabel(image_size_frame, text="x").pack(side=ctk.LEFT, padx=5)
    root.image_height_var = ctk.IntVar(root, value=2160)
    root.image_height_entry = ctk.CTkEntry(
        image_size_frame,
        textvariable=root.image_height_var,
        width=100,
        justify="center",
    )
    root.image_height_entry.pack(side=ctk.LEFT)

    checkboxes_frame = ctk.CTkFrame(root.frame_settings, fg_color="transparent")
    checkboxes_frame.pack(pady=(0, 10))

    root.render_video_var = ctk.BooleanVar(checkboxes_frame, value=True)
    root.render_video_checkbox = ctk.CTkCheckBox(
        checkboxes_frame,
        text="Render Video?",
        font=("", 12),
        variable=root.render_video_var,
    )
    root.render_video_checkbox.pack(side=ctk.LEFT, padx=10)

    root.render_reverse_var = ctk.BooleanVar(checkboxes_frame, value=True)
    root.render_reverse_checkbox = ctk.CTkCheckBox(
        checkboxes_frame,
        text="Render w/ Reverse?",
        font=("", 12),
        variable=root.render_reverse_var,
    )
    root.render_reverse_checkbox.pack(side=ctk.LEFT, padx=10)

    video_format_label = ctk.CTkLabel(
        root.frame_settings, text="Video Format:", font=("", 12)
    )
    video_format_label.pack(pady=(0, 0))

    radio_frame = ctk.CTkFrame(root.frame_settings, fg_color="transparent")
    radio_frame.pack(pady=(0, 10))

    root.video_format_var = ctk.StringVar(radio_frame, value="mp4")
    root.radio_mp4 = ctk.CTkRadioButton(
        radio_frame, text="MP4", variable=root.video_format_var, value="mp4"
    )
    root.radio_mp4.pack(side=ctk.LEFT, padx=10, pady=0)
    root.radio_gif = ctk.CTkRadioButton(
        radio_frame, text="GIF", variable=root.video_format_var, value="gif"
    )
    root.radio_gif.pack(side=ctk.LEFT, padx=10, pady=0)

    frame_MP4_settings = ctk.CTkFrame(root.frame_settings, fg_color="transparent")
    frame_MP4_settings.pack(pady=(10, 10), padx=(0, 0))

    fps_label = ctk.CTkLabel(
        frame_MP4_settings, text="Frames per Second (FPS):", font=("", 12)
    )
    fps_label.pack()
    root.fps_var = ctk.IntVar(root, value=25)
    root.fps_entry = ctk.CTkEntry(
        frame_MP4_settings, textvariable=root.fps_var, justify="center"
    )
    root.fps_entry.pack()

    duration_label = ctk.CTkLabel(
        frame_MP4_settings, text="Duration (seconds):", font=("", 12)
    )
    duration_label.pack()
    root.duration_var = ctk.IntVar(root, value=3)
    root.duration_entry = ctk.CTkEntry(
        frame_MP4_settings, textvariable=root.duration_var, justify="center"
    )
    root.duration_entry.pack()

    video_size_label = ctk.CTkLabel(
        frame_MP4_settings, text="Video Size (w x h):", font=("", 12)
    )
    video_size_label.pack()
    video_size_frame = ctk.CTkFrame(frame_MP4_settings, fg_color="transparent")
    video_size_frame.pack()
    root.video_width_var = ctk.IntVar(root, value=1920)
    root.video_width_entry = ctk.CTkEntry(
        video_size_frame, textvariable=root.video_width_var, width=100, justify="center"
    )
    root.video_width_entry.pack(side=ctk.LEFT)
    ctk.CTkLabel(video_size_frame, text="x").pack(side=ctk.LEFT, padx=5)
    root.video_height_var = ctk.IntVar(root, value=1080)
    root.video_height_entry = ctk.CTkEntry(
        video_size_frame,
        textvariable=root.video_height_var,
        width=100,
        justify="center",
    )
    root.video_height_entry.pack(side=ctk.LEFT)

    ##################################################### OUTPUT #####################################################

    ctk.CTkLabel(root, text="Output Settings", font=("", 14, "bold")).pack(pady=(20, 0))

    root.frame_outputs = ctk.CTkFrame(root, fg_color="transparent")
    root.frame_outputs.pack(pady=(0, 10))

    output_folder_label = ctk.CTkLabel(
        root.frame_outputs, text="Select Image Sequence Folder:", font=("", 12)
    )
    output_folder_label.pack()

    frame_image_folder = ctk.CTkFrame(root.frame_outputs)
    frame_image_folder.pack(pady=(0, 10))

    root.output_folder_var = ctk.StringVar(root)
    root.output_folder_entry = ctk.CTkEntry(
        frame_image_folder,
        textvariable=root.output_folder_var,
        width=400,
        justify="left",
    )
    root.output_folder_entry.pack(side=ctk.LEFT)
    output_folder_button = ctk.CTkButton(
        frame_image_folder, text="Browse", width=80, command=root.select_output_folder
    )
    output_folder_button.pack(side=ctk.LEFT)

    video_folder_label = ctk.CTkLabel(
        root.frame_outputs, text="Select Video Folder:", font=("", 12)
    )
    video_folder_label.pack()

    frame_video_folder = ctk.CTkFrame(root.frame_outputs)
    frame_video_folder.pack(pady=(0, 10))

    root.video_folder_var = ctk.StringVar(root)
    root.video_folder_entry = ctk.CTkEntry(
        frame_video_folder,
        textvariable=root.video_folder_var,
        width=400,
        justify="left",
    )
    root.video_folder_entry.pack(side=ctk.LEFT)
    video_folder_button = ctk.CTkButton(
        frame_video_folder, text="Browse", width=80, command=root.select_video_folder
    )
    video_folder_button.pack(side=ctk.LEFT)

    frame_render_buttons = ctk.CTkFrame(root.frame_outputs, fg_color="transparent")
    frame_render_buttons.pack(pady=10)

    root.render_button = ctk.CTkButton(
        frame_render_buttons, text="Render", command=root.render_animation
    )
    root.render_button.pack(side=ctk.LEFT, padx=10)
    root.cancel_button = ctk.CTkButton(
        frame_render_buttons,
        text="Cancel",
        command=root.cancel_rendering,
        state="disabled",
    )
    root.cancel_button.pack(side=ctk.LEFT, padx=10)

    root.frame_progress = ctk.CTkFrame(root, fg_color="transparent")
    root.frame_progress.pack(pady=(0, 0))

    root.progress = ctk.CTkProgressBar(
        root.frame_progress, orientation="horizontal", width=200, mode="determinate"
    )
    root.progress.set(0)
    root.progress.pack()
    root.status_label = ctk.CTkLabel(
        root.frame_progress, text="Ready", font=("TkDefaultFont", 8), state="disabled"
    )
    root.status_label.pack(pady=(5, 20))


def disable_ui(root):
    disableChildren(root.frame_dropdowns)
    disableChildren(root.frame_styles)
    disableChildren(root.frame_settings)
    disableChildren(root.frame_outputs)
    root.render_button.configure(state="disabled")
    root.cancel_button.configure(state="normal")


def enable_ui(root):
    enableChildren(root.frame_dropdowns)
    enableChildren(root.frame_styles)
    enableChildren(root.frame_settings)
    enableChildren(root.frame_outputs)
    root.render_button.configure(state="normal")
    root.cancel_button.configure(state="disabled")
