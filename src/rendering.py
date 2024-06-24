import os
import subprocess
import glob

from topologicpy.Plotly import Plotly
from topologicpy.Topology import Topology
from topologicpy.Cluster import Cluster
from topologicpy.CellComplex import CellComplex
from topologicpy.Cell import Cell
from topologicpy.Graph import Graph


def render_frames(
    folder,
    version,
    filename_prefix,
    width,
    height,
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
):

    for i in range(total_frames):
        if update_progress(i + 1):  # Check if we should continue rendering
            os.makedirs(folder, exist_ok=True)  # Create the folder if it doesn't exist

            t = i / (total_frames - 1)  # Normalize time between 0 and 1
            eased_t = easing_function(t)
            face_opacity = (
                face_opacity_start + (face_opacity_end - face_opacity_start) * eased_t
            )

            # Parse the edge_color string into RGB values
            edge_r, edge_g, edge_b = map(int, edge_color.split(","))
            edge_style = f"rgba({edge_r}, {edge_g}, {edge_b}, {edge_opacity})"

            # Parse the face_color string into RGB values
            face_r, face_g, face_b = map(int, face_color.split(","))
            face_style = f"rgba({face_r}, {face_g}, {face_b}, {face_opacity})"

            topologies, bounding_box = animation_function(eased_t)
            corners = Cluster.ByTopologies(Topology.Vertices(bounding_box))

            if isinstance(topologies, tuple):
                if (
                    len(topologies) == 2
                    and isinstance(topologies[0][0], CellComplex)
                    and isinstance(topologies[1], Cell)
                ):
                    c = topologies[0]
                    bounding_box = topologies[1]
                    graph = Graph.ByTopology(c)
                    graph_top = Cluster.SelfMerge(Graph.Topology(graph))
                    data01 = Plotly.DataByTopology(
                        corners,
                        vertexColor=f"rgba({vertex_color},{vertex_opacity})",
                        edgeColor=edge_style,
                        edgeWidth=edge_width,
                    )
                    data02 = Plotly.DataByTopology(c, faceOpacity=0.1)
                    data03 = Plotly.DataByTopology(
                        graph_top, vertexSize=5, edgeWidth=3, edgeColor="red"
                    )
                    figure = Plotly.FigureByData(
                        data01 + data02 + data03,
                        backgroundColor=f"rgba({bg_color},{bg_opacity})",
                    )
                elif (
                    len(topologies) == 2
                    and isinstance(topologies[0], Topology)
                    and isinstance(topologies[1], Cell)
                ):
                    rotated_c, boundingBox = topologies
                    data01 = Plotly.DataByTopology(
                        corners,
                        vertexColor=f"rgba({vertex_color},{vertex_opacity})",
                        edgeColor=edge_style,
                        edgeWidth=edge_width,
                    )
                    data02 = Plotly.DataByTopology(rotated_c, faceColor=face_style)
                    data03 = Plotly.DataByTopology(boundingBox)
                    figure = Plotly.FigureByData(
                        data01 + data02 + data03,
                        backgroundColor=f"rgba({bg_color},{bg_opacity})",
                    )
                else:
                    raise ValueError("Invalid topologies tuple")
            else:
                data01 = Plotly.DataByTopology(
                    corners,
                    vertexColor=f"rgba({vertex_color},{vertex_opacity})",
                    edgeColor=edge_style,
                    edgeWidth=edge_width,
                )
                data02 = Plotly.DataByTopology(
                    topologies,
                    edgeColor=edge_style,
                    edgeWidth=edge_width,
                    faceColor=face_style,
                )
                figure = Plotly.FigureByData(
                    data01 + data02,
                    backgroundColor=f"rgba({bg_color},{bg_opacity})",
                )

            # Check if filename_prefix is not empty
            if filename_prefix:
                prefix = f"{filename_prefix}_"
            else:
                prefix = ""

            # Construct the file path
            file_path = os.path.join(
                folder, f"{prefix}{selected_animation}_v{version:03d}_{i+1:04d}.png"
            )
            Plotly.FigureExportToPNG(
                figure, file_path, width=width, height=height, overwrite=True
            )
            print(f"Frame {i+1}/{total_frames} exported: {file_path}")
            update_progress(i + 1)

        else:
            print(f"Render cancelled by user.")
            return  # Exit early due to cancellation
    return True


def create_video_from_images(
    image_folder,
    video_folder,
    version,
    filename_prefix,
    fps,
    width,
    height,
    render_reverse,
    video_format,
    selected_animation,
):

    input_files = glob.glob(os.path.join(image_folder, "*.png"))

    if render_reverse:
        reverse_files = list(reversed(input_files))
        input_files = input_files + reverse_files

    if not os.path.exists(video_folder):
        os.makedirs(video_folder)

    # Check if filename_prefix is not empty
    if filename_prefix:
        prefix = f"{filename_prefix}_"
    else:
        prefix = ""

    if video_format == "mp4":
        output_file = os.path.join(
            video_folder, f"{prefix}{selected_animation}_v{version:03d}.mp4"
        )
        ffmpeg_command = [
            "ffmpeg",
            "-framerate",
            str(fps),
            "-i",
            "concat:" + "|".join(input_files),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-vf",
            f"scale={width}:{height}",
            output_file,
        ]
    elif video_format == "gif":
        output_file = os.path.join(
            video_folder, f"{prefix}{selected_animation}_v{version:03d}.gif"
        )
        ffmpeg_command = [
            "ffmpeg",
            "-framerate",
            str(fps),
            "-i",
            "concat:" + "|".join(input_files),
            "-vf",
            f"scale={width}:{height}",
            "-loop",
            "0",  # Set to loop indefinitely
            output_file,
        ]

    try:
        if not input_files:
            raise FileNotFoundError(
                f"No PNG images found in the directory: {image_folder}"
            )

        result = subprocess.run(
            ffmpeg_command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        print(f"Video created: {output_file}")
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
        raise
    except subprocess.CalledProcessError as e:
        print(f"Error creating video: {str(e)}")
        print(f"FFmpeg output: {e.output}")
        print(f"FFmpeg error: {e.stderr}")
        raise
