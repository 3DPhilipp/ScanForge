# ScanForge

A tool for automated 3D model processing using Houdini and Marmoset Toolbag.

## Features
- LOD Generation (LOD0-LOD4)
- Automated UV unwrapping
- Map baking in Marmoset Toolbag
- Support for custom cage meshes

## Requirements
- Python 3.x
- PySide6
- Houdini Indie
- Marmoset Toolbag

## Installation
1. Clone the repository
```git clone https://github.com/3DPhilipp/ScanForge.git```

2. Install requirements
```pip install -r requirements.txt```

## Usage
Run the main script:
```python src/main.py```

## About
ScanForge is a tool designed to streamline the process of preparing 3D scans for real-time applications. It automates the workflow of LOD creation, UV unwrapping, and texture baking.

## Links
- [The Triangle Forge](https://thetriangleforge.de)
```

2. **Projektstruktur organisieren**
Für die nächsten Änderungen auf Ihrem lokalen Computer:

```bash
cd C:\Users\phili\Documents\pipelinetest

# Erstellen Sie die Ordnerstruktur
mkdir -p src/ui src/utils

# Verschieben Sie die Dateien in die entsprechenden Ordner
git mv main.py src/
git mv *.png src/ui/

# Commit die Änderungen
git add .
git commit -m "Organize project structure"
git push origin main
```

Möchten Sie diese Änderungen vornehmen? Ich kann Sie durch jeden Schritt führen.
