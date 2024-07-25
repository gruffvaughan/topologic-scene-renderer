# topologicpy Scene Renderer

The topologicpy Scene Renderer is a python application that allows you to export animations using the [topologicpy](https://pypi.org/project/topologicpy/) library, an open-source python3 implementation of [Topologic](https://topologic.app/) which is a powerful spatial modelling and analysis software library that revolutionizes the way you design architectural spaces, buildings, and artefacts. It provides a user-friendly interface for generating various geometric shapes, applying transformations, and exporting image sequences and video files.

## Features

- Support for a wide range of geometric shapes and transformations provided by [topologicpy](https://pypi.org/project/topologicpy/)
- Choose the style of your selected topologies (colour, width, opacity)
- Configure the colour and opacity of the scene background
- Configure animation parameters (e.g., duration, frame rate, resolution)
- Export image sequences as video files in different formats (e.g., MP4, GIF)
- Renders will automatically version up when you re-render

## Installation

⚠️ Ensure that your Python environment is 3.11, as 3.12+ is not supported by `topologicpy`

1. Clone the repository:

```
https://github.com/gruffvaughan/topologic-scene-renderer
```

2. Install the required dependencies:

```
pip install -r docs/requirements.txt
```

3. You'll need to downgrade `kaleido` (required by Plotly) to version 0.1.0post1 otherwise the script [locks in an endless loop](https://github.com/plotly/Kaleido/issues/110)

```
 pip install --upgrade "kaleido==0.1.*"
```

4. Install [ffmpeg](https://www.ffmpeg.org/download.html) if it's not already on your machine


## Usage

1. Run the application:

```
python src/main.py
```

2. Use the user interface to select the desired animation type, configure the animation parameters, and customize the rendering settings.

3. Click the "Render" button to generate the animation. The rendered frames will be saved in the specified output directory.

4. Once the rendering is complete, the animation will be exported as a video file in the selected format and saved in the specified video directory.

## Configuration

When you modify the settings using the user interface and render an animation, the application will save your current settings to the `preferences.json` file for when you next open the application.

## Contributing

Contributions are welcome! If you find any bugs, have feature requests, or want to contribute improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

The topologicpy Scene Renderer is built on top of the [topologicpy](https://pypi.org/project/topologicpy/) library.

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact the developer:

Gruff Vaughan - [gruff@stormandshelter.com](gruff@stormandshelter.com) - [STORM+SHELTER](https://stormandshelter.com)
