import threading

import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

from src.animations import animation_functions
from src.easing import easing_functions
from src.rendering import render_frames, create_video_from_images
from src.utils import get_next_version
from src.preferences import save_preferences, load_preferences
from src.ui.layout import create_layout, enable_ui, disable_ui


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.cancel_render = False  # Flag to control rendering cancellation
        self.title("topologicpy Scene Renderer")
        self.geometry("700x1180+2140+0")
        self.iconbitmap("src/ui/images/icon.ico")

        create_layout(self)
        load_preferences(self)

    def select_output_folder(self):
        self.output_folder = ctk.filedialog.askdirectory()
        self.output_folder_var.set(self.output_folder)
        save_preferences(self)

    def select_video_folder(self):
        self.video_folder = ctk.filedialog.askdirectory()
        self.video_folder_var.set(self.video_folder)
        save_preferences(self)

    def render_animation(self):
        filename_prefix = self.filename_prefix_var.get()
        selected_animation = self.animation_var.get()
        selected_easing = self.easing_var.get()
        fps = self.fps_var.get()
        duration = self.duration_var.get()
        total_frames = fps * duration
        image_width = self.image_width_var.get()
        image_height = self.image_height_var.get()
        render_video = self.render_video_var.get()
        render_reverse = self.render_reverse_var.get()
        video_format = self.video_format_var.get()
        video_width = self.video_width_var.get()
        video_height = self.video_height_var.get()
        face_opacity_start = self.face_opacity_start_var.get()
        face_opacity_end = self.face_opacity_end_var.get()
        face_color = self.face_color_var.get()
        edge_color = self.edge_color_var.get()
        edge_opacity = self.edge_opacity_var.get()
        edge_width = self.edge_width_var.get()
        vertex_color = self.vertex_color_var.get()
        vertex_opacity = self.vertex_opacity_var.get()
        bg_color = self.bg_color_var.get()
        bg_opacity = self.bg_opacity_var.get()

        save_preferences(self)

        if not selected_animation or not selected_easing:
            print(
                "Please select an animation and easing function, and enter a sequence name."
            )
            return

        output_folder = self.output_folder_var.get()
        video_folder = self.video_folder_var.get()

        if not output_folder or not video_folder:
            print("Please select output and video folders.")
            return

        # Get the animation and easing functions
        animation_function = animation_functions[selected_animation]
        easing_function = easing_functions[selected_easing]

        folder, version = get_next_version(
            output_folder, filename_prefix, selected_animation
        )

        # Prepare the thread for rendering
        render_thread = threading.Thread(
            target=self.render_sequence,
            args=(
                folder,
                version,
                filename_prefix,
                image_width,
                image_height,
                animation_function,
                easing_function,
                total_frames,
                render_video,
                fps,
                video_width,
                video_height,
                render_reverse,
                video_format,
                face_opacity_start,
                face_opacity_end,
                face_color,
                edge_color,
                edge_opacity,
                edge_width,
                vertex_color,
                vertex_opacity,
                bg_color,
                bg_opacity,
                video_folder,
                selected_animation,
            ),
        )
        render_thread.start()

    def render_sequence(
        self,
        folder,
        version,
        filename_prefix,
        image_width,
        image_height,
        animation_function,
        easing_function,
        total_frames,
        render_video,
        fps,
        video_width,
        video_height,
        render_reverse,
        video_format,
        face_opacity_start,
        face_opacity_end,
        face_color,
        edge_color,
        edge_opacity,
        edge_width,
        vertex_color,
        vertex_opacity,
        bg_color,
        bg_opacity,
        video_folder,
        selected_animation,
    ):
        disable_ui(self)  # Disable UI at the start of rendering
        self.cancel_button.configure(state="normal")  # Enable the cancel button
        self.status_label.configure(state="normal")

        # Call render_frames with a callback to update_progress
        def update_progress(frame_number):
            self.progress["value"] = (frame_number / total_frames) * 100
            self.update_idletasks()  # Make sure UI updates
            if self.cancel_render:
                self.status_label.configure(text="Render cancelled.")
                self.progress["value"] = 0
                return False  # Indicate that rendering should be stopped
            self.status_label.configure(
                text=f"Rendering frame {frame_number}/{total_frames}"
            )
            return True

        try:
            render_result = render_frames(
                folder,
                version,
                filename_prefix,
                image_width,
                image_height,
                animation_function,
                easing_function,
                total_frames,
                update_progress,
                face_opacity_start,
                face_opacity_end,
                face_color,
                edge_color,
                edge_opacity,
                edge_width,
                vertex_color,
                vertex_opacity,
                bg_color,
                bg_opacity,
                selected_animation,
            )

            if not render_result:
                print("Rendering cancelled")
                enable_ui(self)  # Re-enable UI after rendering is cancelled
                self.cancel_button.configure(state="disabled")
                self.progress["value"] = 0
                self.status_label.configure(state="disabled")
                self.cancel_render = False  # Reset the cancel flag
                return  # Exit as the render was cancelled

            if render_video:
                self.status_label.configure(text="Saving video file...")
                create_video_from_images(
                    folder,
                    video_folder,
                    version,
                    filename_prefix,
                    fps,
                    video_width,
                    video_height,
                    render_reverse,
                    video_format,
                    selected_animation,
                )
                self.status_label.configure(
                    text="Video file has been saved successfully."
                )
            else:
                print("Rendering completed without creating video")
                self.status_label.configure(
                    text="Image sequence has been rendered successfully."
                )
        except Exception as e:
            print(f"Exception occurred: {str(e)}")
            self.status_label.configure(text=f"An error occurred: {str(e)}")
            print(e)

        finally:
            enable_ui(self)  # Re-enable UI after rendering is complete
            self.cancel_button.configure(state="disabled")
            self.status_label.configure(state="disabled")
            self.cancel_render = False  # Reset the cancel flag

    def cancel_rendering(self):
        self.cancel_render = True  # Set the flag to cancel rendering
        self.status_label.configure(text="Cancellation requested. Please wait...")


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
