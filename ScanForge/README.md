# ScanForge

A powerful Python tool for processing 3D scans using Houdini and Marmoset Toolbag.

## Features

- Import high-poly FBX scans into Houdini
- Automatic mesh decimation and cleaning
- LOD generation (LOD0-4)
- UV creation
- Map baking in Marmoset Toolbag with support for:
  - Normal maps
  - Height maps
  - Ambient Occlusion
  - Curvature maps
  - Position maps
  - Thickness maps
  - ID maps
  - Bent Normal maps
- Modern UI with dark theme
- Configuration saving/loading

## Requirements

- Python 3.8+
- PySide6
- Houdini
- Marmoset Toolbag

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ScanForge.git
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. Configure the application paths in the Settings tab:
   - Set Houdini executable path
   - Set Marmoset Toolbag executable path
   - (Optional) Set Python environment path
   - (Optional) Set license file path

## Usage

1. Launch the application:
```bash
python -m src.main
```

2. Select your input FBX file
3. Configure LOD settings
4. Select maps to bake and their settings
5. Configure cage settings
6. Click "Process Model" to start the pipeline

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created by The Triangle Forge (https://thetriangleforge.de)