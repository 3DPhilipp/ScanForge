import sys
from pathlib import Path
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QFileDialog, QSpinBox,
                             QCheckBox, QProgressBar, QGroupBox, QApplication,
                             QComboBox, QRadioButton, QButtonGroup, QLineEdit,
                             QMessageBox, QTabWidget, QScrollArea, QGridLayout,
                             QSizePolicy, QFrame, QDoubleSpinBox, QTextEdit)
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtGui import QPalette, QColor, QPixmap, QPainter, QPainterPath
from config import Config
import json

DARK_THEME_STYLE = """
QMainWindow, QWidget {
    background-color: #2b2b2b;
    color: #ffffff;
}

QLabel {
    color: #ffffff;
}

QPushButton {
    background-color: #3a3a3a;
    border: none;
    color: #ffffff;
    padding: 8px 16px;
    border-radius: 4px;
}

QPushButton:hover {
    background-color: #454545;
}

QPushButton:pressed {
    background-color: #505050;
}

QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox {
    background-color: #3a3a3a;
    color: #ffffff;
    border: none;
    padding: 6px;
    border-radius: 4px;
}

QGroupBox {
    border: 1px solid #3a3a3a;
    border-radius: 6px;
    margin-top: 12px;
    padding-top: 12px;
}

QGroupBox::title {
    color: #ffffff;
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
}

QCheckBox {
    color: #ffffff;
    spacing: 8px;
}

/* Standard Checkbox Style */
QCheckBox::indicator {
    width: 13px;
    height: 13px;
}

QComboBox {
    background-color: #3a3a3a;
    color: #ffffff;
    border: none;
    padding: 6px;
    padding-right: 20px;
    border-radius: 4px;
    min-width: 6em;
}

QComboBox::drop-down {
    border: none;
    width: 20px;
    subcontrol-origin: padding;
    subcontrol-position: right center;
}

QComboBox::down-arrow {
    width: 12px;
    height: 12px;
    background: transparent;
    image: url(down_arrow.png);  /* Wir müssen diese Datei erstellen */
}

QComboBox:hover {
    background-color: #454545;
}

QComboBox:on {
    background-color: #505050;
}

QComboBox QAbstractItemView {
    background-color: #2b2b2b;
    color: #ffffff;
    selection-background-color: #505050;
    selection-color: #ffffff;
    border: none;
    outline: none;
}

QScrollBar:vertical {
    border: none;
    background: #2b2b2b;
    width: 12px;
    margin: 0;
}

QScrollBar::handle:vertical {
    background: #3a3a3a;
    min-height: 20px;
    border-radius: 6px;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}

QTabWidget::pane {
    border: 1px solid #3a3a3a;
    border-radius: 4px;
}

QTabBar::tab {
    background-color: #2b2b2b;
    color: #ffffff;
    padding: 8px 16px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
}

QTabBar::tab:selected {
    background-color: #3a3a3a;
}

QTabBar::tab:hover {
    background-color: #454545;
}

/* Styling für die Spin-Boxen */
QSpinBox, QDoubleSpinBox {
    background-color: #3a3a3a;
    color: #ffffff;
    border: none;
    padding: 6px;
    padding-right: 20px;
    border-radius: 4px;
}

QSpinBox::up-button, QDoubleSpinBox::up-button,
QSpinBox::down-button, QDoubleSpinBox::down-button {
    width: 20px;
    border: none;
    background-color: transparent;
}

QSpinBox::up-button, QDoubleSpinBox::up-button {
    subcontrol-origin: padding;
    subcontrol-position: right top;
}

QSpinBox::down-button, QDoubleSpinBox::down-button {
    subcontrol-origin: padding;
    subcontrol-position: right bottom;
}

QSpinBox::up-arrow, QDoubleSpinBox::up-arrow {
    width: 12px;
    height: 12px;
    background: transparent;
    image: url(up_arrow.png);
}

QSpinBox::down-arrow, QDoubleSpinBox::down-arrow {
    width: 12px;
    height: 12px;
    background: transparent;
    image: url(down_arrow.png);
}

QSpinBox::up-button:hover, QDoubleSpinBox::up-button:hover,
QSpinBox::down-button:hover, QDoubleSpinBox::down-button:hover {
    background-color: #454545;
}

QSpinBox::up-button:pressed, QDoubleSpinBox::up-button:pressed,
QSpinBox::down-button:pressed, QDoubleSpinBox::down-button:pressed {
    background-color: #505050;
}
"""

# Pfeil-Icons erstellen und speichern
def create_arrow_icons():
    # Down Arrow (bereits vorhanden)
    arrow_down = QPixmap(12, 12)
    arrow_down.fill(Qt.transparent)
    painter = QPainter(arrow_down)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setPen(Qt.NoPen)
    painter.setBrush(QColor('#ffffff'))
    
    # Zeichne Pfeil nach unten
    path = QPainterPath()
    path.moveTo(2, 4)
    path.lineTo(10, 4)
    path.lineTo(6, 8)
    path.lineTo(2, 4)
    painter.drawPath(path)
    painter.end()
    arrow_down.save('down_arrow.png')
    
    # Up Arrow
    arrow_up = QPixmap(12, 12)
    arrow_up.fill(Qt.transparent)
    painter = QPainter(arrow_up)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setPen(Qt.NoPen)
    painter.setBrush(QColor('#ffffff'))
    
    # Zeichne Pfeil nach oben
    path = QPainterPath()
    path.moveTo(2, 8)
    path.lineTo(10, 8)
    path.lineTo(6, 4)
    path.lineTo(2, 8)
    painter.drawPath(path)
    painter.end()
    arrow_up.save('up_arrow.png')

def set_dark_theme(app):
    """Set dark theme for the application"""
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(35, 35, 35))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
    app.setPalette(palette)
    
    # Set stylesheet for specific widgets
    app.setStyleSheet("""
        QGroupBox {
            border: 1px solid #666;
            border-radius: 4px;
            margin-top: 0.5em;
            padding-top: 0.5em;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 3px 0 3px;
        }
        QPushButton {
            background-color: #444;
            border: 1px solid #666;
            border-radius: 4px;
            padding: 5px 15px;
        }
        QPushButton:hover {
            background-color: #555;
        }
        QPushButton:pressed {
            background-color: #333;
        }
        QComboBox, QSpinBox, QLineEdit {
            background-color: #444;
            border: 1px solid #666;
            border-radius: 4px;
            padding: 3px;
        }
        QProgressBar {
            border: 1px solid #666;
            border-radius: 4px;
            text-align: center;
        }
        QProgressBar::chunk {
            background-color: #2A82DA;
        }
        QLabel {
            color: #ffffff;
        }
        QLabel > a {
            color: #00ffff;  /* Helles Cyan für bessere Lesbarkeit */
        }
        QLabel > a:hover {
            color: #7fffff;  /* Noch helleres Cyan beim Hover */
        }
    """)

def set_light_theme(app):
    """Set light theme for the application"""
    app.setStyle("Fusion")
    
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(240, 240, 240))
    palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
    palette.setColor(QPalette.Base, QColor(255, 255, 255))
    palette.setColor(QPalette.AlternateBase, QColor(245, 245, 245))
    palette.setColor(QPalette.Text, QColor(0, 0, 0))
    palette.setColor(QPalette.Button, QColor(240, 240, 240))
    palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
    
    app.setPalette(palette)
    
    app.setStyleSheet("""
        QGroupBox {
            border: 1px solid #999;
            border-radius: 4px;
            margin-top: 0.5em;
            padding-top: 0.5em;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 3px 0 3px;
        }
        QPushButton {
            background-color: #f0f0f0;
            border: 1px solid #999;
            border-radius: 4px;
            padding: 5px 15px;
        }
        QPushButton:hover {
            background-color: #e0e0e0;
        }
        QPushButton:pressed {
            background-color: #d0d0d0;
        }
        QProgressBar {
            border: 1px solid #999;
            border-radius: 4px;
            text-align: center;
        }
        QProgressBar::chunk {
            background-color: #2A82DA;
        }
        QLabel[link="true"] {
            color: #000000;
        }
        QLabel[link="true"] a {
            color: #0066cc;
        }
        QLabel[link="true"] a:hover {
            color: #0080ff;
        }
    """)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.setWindowTitle("ScanForge")
        self.setMinimumSize(800, 600)
        
        # Erstelle die Pfeil-Icons
        create_arrow_icons()
        
        # Direkt das Dark Theme anwenden, ohne Settings dafür
        self.setStyleSheet(DARK_THEME_STYLE)
        
        # Hauptwidget und Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        
        # Website Link
        website_label = QLabel()
        website_label.setText('<a href="https://thetriangleforge.de" style="color: #ffffff;">thetriangleforge.de</a>')
        website_label.setOpenExternalLinks(True)
        website_label.setAlignment(Qt.AlignRight)
        main_layout.addWidget(website_label)
        
        # Tabs erstellen
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        
        # Pipeline Tab
        pipeline_tab = QWidget()
        pipeline_layout = QVBoxLayout(pipeline_tab)
        
        # Input Settings
        input_group = QGroupBox("Input Settings")
        input_layout = QGridLayout(input_group)
        input_layout.setContentsMargins(20, 20, 20, 20)
        input_layout.setSpacing(15)
        
        # Input File
        self.file_path = QLabel("No file selected")
        select_file_btn = QPushButton("Select FBX File")
        select_file_btn.clicked.connect(self.select_input_file)
        input_layout.addWidget(QLabel("Input File:"), 0, 0)
        input_layout.addWidget(self.file_path, 0, 1)
        input_layout.addWidget(select_file_btn, 0, 2)
        
        # Output Path
        self.output_path = QLineEdit()
        self.output_path.setPlaceholderText("Select output directory...")
        if 'last_output_dir' in self.config.settings:
            self.output_path.setText(self.config.settings['last_output_dir'])
        select_output_btn = QPushButton("Browse")
        select_output_btn.clicked.connect(self.select_output_path)
        input_layout.addWidget(QLabel("Output Path:"), 1, 0)
        input_layout.addWidget(self.output_path, 1, 1)
        input_layout.addWidget(select_output_btn, 1, 2)
        
        # Setze die Spaltenbreiten
        input_layout.setColumnStretch(1, 1)  # Mittlere Spalte dehnt sich aus
        
        pipeline_layout.addWidget(input_group)
        
        # LOD Settings
        lod_group = QGroupBox("LOD Settings")
        lod_layout = QVBoxLayout()
        
        # Spezielles Layout für LOD 0 mit Tri Count
        lod0_settings = QHBoxLayout()
        lod0_settings.addWidget(QLabel("LOD 0"))
        lod0_settings.addWidget(QLabel("Target Triangle Count:"))
        tri_count_spinbox = QSpinBox()
        tri_count_spinbox.setRange(100, 10000000)  # Minimum 100 Tris, Maximum 10 Million
        tri_count_spinbox.setSingleStep(1000)  # Schritte von 1000 für einfachere Anpassung
        tri_count_spinbox.setValue(100000)  # Standard: 100k Tris
        tri_count_spinbox.setGroupSeparatorShown(True)  # Korrekte Methode für PySide6
        lod0_settings.addWidget(tri_count_spinbox)
        lod_layout.addLayout(lod0_settings)
        
        # LOD 1-4 mit Prozent-Reduktion basierend auf LOD 0
        for i in range(1, 5):
            lod_settings = QHBoxLayout()
            lod_settings.addWidget(QLabel(f"LOD {i}"))
            lod_settings.addWidget(QLabel("Reduction from LOD 0:"))
            
            reduction_spinbox = QSpinBox()
            reduction_spinbox.setRange(1, 99)
            reduction_spinbox.setSuffix("%")
            reduction_spinbox.setValue(25 * i)  # LOD1=25%, LOD2=50%, LOD3=75%, LOD4=90%
            
            lod_settings.addWidget(reduction_spinbox)
            lod_layout.addLayout(lod_settings)
        
        lod_group.setLayout(lod_layout)
        pipeline_layout.addWidget(lod_group)
        
        # Bake Settings Bereich
        bake_group = QGroupBox("Bake Settings")
        bake_layout = QGridLayout()
        
        # Resolution
        bake_layout.addWidget(QLabel("Resolution:"), 0, 0)
        self.bake_resolution_combo = QComboBox()
        self.bake_resolution_combo.addItems(["256x256", "512x512", "1024x1024", "2048x2048", "4096x4096", "8192x8192"])
        bake_layout.addWidget(self.bake_resolution_combo, 0, 1)
        
        # Format
        bake_layout.addWidget(QLabel("Format:"), 1, 0)
        self.bake_format_combo = QComboBox()
        self.bake_format_combo.addItems(["PNG", "TGA"])
        bake_layout.addWidget(self.bake_format_combo, 1, 1)
        
        # Anti-Aliasing
        bake_layout.addWidget(QLabel("Anti-Aliasing:"), 2, 0)
        self.anti_aliasing_combo = QComboBox()
        self.anti_aliasing_combo.addItems(["None", "2x", "4x", "8x"])
        bake_layout.addWidget(self.anti_aliasing_combo, 2, 1)
        
        # Cage Settings in einem eigenen GroupBox
        cage_group = QGroupBox("Cage Settings")
        cage_layout = QGridLayout()
        
        # External Cage Option
        self.use_external_cage = QCheckBox("Use External Cage")
        self.use_external_cage.setChecked(False)
        cage_layout.addWidget(self.use_external_cage, 0, 0, 1, 2)

        # External Cage File Selection
        cage_file_layout = QHBoxLayout()
        self.cage_file_edit = QLineEdit()
        self.cage_file_edit.setPlaceholderText("No cage file selected...")
        self.cage_file_edit.setEnabled(False)
        cage_file_layout.addWidget(self.cage_file_edit)

        self.cage_file_btn = QPushButton("Select Cage")
        self.cage_file_btn.setEnabled(False)
        self.cage_file_btn.clicked.connect(self.select_cage_file)
        cage_file_layout.addWidget(self.cage_file_btn)

        cage_layout.addLayout(cage_file_layout, 1, 0, 1, 2)
        
        # Bestehende Cage Settings
        cage_layout.addWidget(QLabel("Cage Offset:"), 2, 0)
        self.cage_offset_spin = QDoubleSpinBox()
        self.cage_offset_spin.setRange(0.0, 10.0)
        self.cage_offset_spin.setSingleStep(0.01)
        self.cage_offset_spin.setValue(0.02)
        self.cage_offset_spin.setSuffix(" units")
        cage_layout.addWidget(self.cage_offset_spin, 2, 1)

        cage_layout.addWidget(QLabel("Max Ray Distance:"), 3, 0)
        self.ray_distance_spin = QDoubleSpinBox()
        self.ray_distance_spin.setRange(0.0, 100.0)
        self.ray_distance_spin.setSingleStep(0.1)
        self.ray_distance_spin.setValue(1.0)
        self.ray_distance_spin.setSuffix(" units")
        cage_layout.addWidget(self.ray_distance_spin, 3, 1)

        self.match_uv_seams = QCheckBox("Match UV Seams")
        self.match_uv_seams.setChecked(True)
        cage_layout.addWidget(self.match_uv_seams, 4, 0, 1, 2)

        self.match_hard_edges = QCheckBox("Match Hard Edges")
        self.match_hard_edges.setChecked(True)
        cage_layout.addWidget(self.match_hard_edges, 5, 0, 1, 2)

        # Verbinde Checkbox mit Enable/Disable Funktion
        self.use_external_cage.toggled.connect(self.toggle_external_cage)

        cage_group.setLayout(cage_layout)
        
        # Füge Cage Settings zum Bake Layout hinzu
        bake_layout.addWidget(cage_group, 3, 0, 1, 2)
        
        bake_group.setLayout(bake_layout)
        pipeline_layout.addWidget(bake_group)
        
        # Add scroll area for pipeline tab
        pipeline_scroll = QScrollArea()
        pipeline_scroll.setWidget(pipeline_tab)
        pipeline_scroll.setWidgetResizable(True)
        pipeline_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabs.addTab(pipeline_scroll, "Pipeline")
        
        # Log Tab
        log_tab = QWidget()
        log_layout = QVBoxLayout(log_tab)
        
        # Log Text Area
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)  # Nur lesen, nicht editieren
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #ffffff;
                font-family: Consolas, Monaco, monospace;
                font-size: 12px;
                padding: 8px;
                border: none;
            }
        """)
        log_layout.addWidget(self.log_text)
        
        # Clear Log Button
        clear_log_btn = QPushButton("Clear Log")
        clear_log_btn.clicked.connect(self.clear_log)
        clear_log_btn.setMaximumWidth(100)
        log_layout.addWidget(clear_log_btn, alignment=Qt.AlignRight)
        
        self.tabs.addTab(log_tab, "Log")
        
        # === SETTINGS TAB ===
        settings_tab = QWidget()
        settings_layout = QVBoxLayout(settings_tab)
        settings_layout.setContentsMargins(20, 20, 20, 20)
        settings_layout.setSpacing(15)
        
        # Application Paths
        paths_group = QGroupBox("Application Paths")
        paths_layout = QGridLayout()
        
        # Houdini Executable
        paths_layout.addWidget(QLabel("Houdini Executable:"), 0, 0)
        self.houdini_path_edit = QLineEdit()
        paths_layout.addWidget(self.houdini_path_edit, 0, 1)
        houdini_browse_btn = QPushButton("Browse")
        houdini_browse_btn.clicked.connect(lambda: self.browse_file(self.houdini_path_edit, "Houdini Executable"))
        paths_layout.addWidget(houdini_browse_btn, 0, 2)

        # Marmoset Executable
        paths_layout.addWidget(QLabel("Marmoset Executable:"), 1, 0)
        self.marmoset_path_edit = QLineEdit()
        paths_layout.addWidget(self.marmoset_path_edit, 1, 1)
        marmoset_browse_btn = QPushButton("Browse")
        marmoset_browse_btn.clicked.connect(lambda: self.browse_file(self.marmoset_path_edit, "Marmoset Executable"))
        paths_layout.addWidget(marmoset_browse_btn, 1, 2)

        # Houdini Project Path
        paths_layout.addWidget(QLabel("Houdini Project:"), 2, 0)
        self.houdini_project_edit = QLineEdit()
        paths_layout.addWidget(self.houdini_project_edit, 2, 1)
        houdini_project_browse_btn = QPushButton("Browse")
        houdini_project_browse_btn.clicked.connect(lambda: self.browse_directory(self.houdini_project_edit, "Houdini Project Directory"))
        paths_layout.addWidget(houdini_project_browse_btn, 2, 2)

        # Python Environment (Optional)
        paths_layout.addWidget(QLabel("Python Environment (Optional):"), 3, 0)
        self.python_env_edit = QLineEdit()
        paths_layout.addWidget(self.python_env_edit, 3, 1)
        python_env_browse_btn = QPushButton("Browse")
        python_env_browse_btn.clicked.connect(lambda: self.browse_directory(self.python_env_edit, "Python Environment"))
        paths_layout.addWidget(python_env_browse_btn, 3, 2)

        # License File (Optional)
        paths_layout.addWidget(QLabel("License File (Optional):"), 4, 0)
        self.license_path_edit = QLineEdit()
        paths_layout.addWidget(self.license_path_edit, 4, 1)
        license_browse_btn = QPushButton("Browse")
        license_browse_btn.clicked.connect(lambda: self.browse_file(self.license_path_edit, "License File"))
        paths_layout.addWidget(license_browse_btn, 4, 2)

        paths_group.setLayout(paths_layout)
        
        settings_layout.addWidget(paths_group)
        
        # Save Settings Button
        save_settings_btn = QPushButton("Save Settings")
        save_settings_btn.clicked.connect(self.save_settings)
        settings_layout.addWidget(save_settings_btn)
        
        # Add settings tab
        self.tabs.addTab(settings_tab, "Settings")
        
        # === BOTTOM BAR ===
        bottom_widget = QWidget()
        bottom_layout = QHBoxLayout(bottom_widget)
        bottom_layout.setContentsMargins(20, 10, 20, 10)
        
        # Progress Bar and Process Button
        self.progress = QProgressBar()
        self.progress.setMinimumHeight(25)
        bottom_layout.addWidget(self.progress)
        
        process_btn = QPushButton("Process Model")
        process_btn.setMinimumWidth(150)
        process_btn.setMinimumHeight(35)
        process_btn.clicked.connect(self.process_model)
        bottom_layout.addWidget(process_btn)
        
        main_layout.addWidget(bottom_widget)

    def browse_path(self, path_type):
        path = QFileDialog.getOpenFileName(
            self,
            f"Select {path_type.replace('_', ' ').title()}",
            "",
            "Executable files (*.exe);;All files (*.*)"
        )[0]
        if path:
            if path_type == 'houdini_path':
                self.houdini_path.setText(path)
            elif path_type == 'marmoset_path':
                self.marmoset_path.setText(path)

    def save_settings(self):
        self.config.settings['houdini_path'] = self.houdini_path.text()
        self.config.settings['marmoset_path'] = self.marmoset_path.text()
        self.config.save_config()
        QMessageBox.information(self, "Settings Saved", "Application settings have been saved successfully.")

    def select_input_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select FBX File",
            self.config.settings['last_project_dir'],
            "FBX files (*.fbx)"
        )
        if file_name:
            self.file_path.setText(file_name)
            self.config.settings['last_project_dir'] = str(Path(file_name).parent)
            self.config.save_config()

    def select_output_path(self):
        dir_name = QFileDialog.getExistingDirectory(
            self,
            "Select Output Directory",
            self.config.settings.get('last_output_dir', str(Path.home()))
        )
        if dir_name:
            self.output_path.setText(dir_name)
            self.config.settings['last_output_dir'] = dir_name
            self.config.save_config()

    def process_model(self):
        self.log("Starting model processing...", "INFO")
        self.log("Loading input file...", "INFO")
        
        # Überprüfen Sie, ob alle erforderlichen Pfade gesetzt sind
        if not self.file_path.text() or self.file_path.text() == "No file selected":
            self.log("No input file selected!", "ERROR")
            return
        
        if not self.output_path.text():
            self.log("No output directory selected!", "ERROR")
            return
        
        if not Path(self.houdini_path.text()).exists():
            self.log("Houdini path is not set or invalid.", "ERROR")
            return
        
        if not Path(self.marmoset_path.text()).exists():
            self.log("Marmoset Toolbag path is not set or invalid.", "ERROR")
            return
        
        if not Path(self.output_path.text()).exists():
            try:
                Path(self.output_path.text()).mkdir(parents=True)
            except Exception as e:
                self.log(f"Could not create output directory:\n{str(e)}", "ERROR")
                return

        # Get all settings for processing
        settings = self.get_current_settings()
        settings['output_path'] = self.output_path.text()
        self.log("Processing with settings:", "INFO")
        self.log(json.dumps(settings), "INFO")
        
        # Update progress bar
        current = self.progress.value()
        if current < 100:
            self.progress.setValue(current + 10)

    def create_bake_settings(self):
        bake_group = QGroupBox("Bake Settings")
        bake_layout = QGridLayout()

        # Cage Settings
        cage_group = QGroupBox("Cage Settings")
        cage_layout = QGridLayout()

        # Cage Offset
        cage_layout.addWidget(QLabel("Cage Offset:"), 0, 0)
        self.cage_offset_spin = QDoubleSpinBox()
        self.cage_offset_spin.setRange(0.0, 10.0)
        self.cage_offset_spin.setSingleStep(0.01)
        self.cage_offset_spin.setValue(0.02)  # Standard-Wert
        self.cage_offset_spin.setSuffix(" units")
        cage_layout.addWidget(self.cage_offset_spin, 0, 1)

        # Ray Distance
        cage_layout.addWidget(QLabel("Max Ray Distance:"), 1, 0)
        self.ray_distance_spin = QDoubleSpinBox()
        self.ray_distance_spin.setRange(0.0, 100.0)
        self.ray_distance_spin.setSingleStep(0.1)
        self.ray_distance_spin.setValue(1.0)  # Standard-Wert
        self.ray_distance_spin.setSuffix(" units")
        cage_layout.addWidget(self.ray_distance_spin, 1, 1)

        # Match UV Seams
        self.match_uv_seams = QCheckBox("Match UV Seams")
        self.match_uv_seams.setChecked(True)
        cage_layout.addWidget(self.match_uv_seams, 2, 0, 1, 2)

        # Match Hard Edges
        self.match_hard_edges = QCheckBox("Match Hard Edges")
        self.match_hard_edges.setChecked(True)
        cage_layout.addWidget(self.match_hard_edges, 3, 0, 1, 2)

        cage_group.setLayout(cage_layout)
        bake_layout.addWidget(cage_group, 2, 0, 1, 2)  # Position nach Resolution und Format

        # Output Settings
        output_group = QGroupBox("Output Settings")
        output_layout = QGridLayout()
        output_layout.setSpacing(10)
        
        # Resolution
        output_layout.addWidget(QLabel("Resolution:"), 0, 0)
        self.resolution_combo = QComboBox()
        resolutions = ["256x256", "512x512", "1024x1024", "2048x2048", "4096x4096", "8192x8192"]
        self.resolution_combo.addItems(resolutions)
        self.resolution_combo.setCurrentText("2048x2048")
        output_layout.addWidget(self.resolution_combo, 0, 1)
        
        # Format
        output_layout.addWidget(QLabel("Format:"), 1, 0)
        self.format_combo = QComboBox()
        self.format_combo.addItems(["PNG", "TGA"])
        output_layout.addWidget(self.format_combo, 1, 1)
        
        # Bit Depth
        output_layout.addWidget(QLabel("Bit Depth:"), 2, 0)
        self.bit_depth_combo = QComboBox()
        self.bit_depth_combo.addItems(["8-bit", "16-bit"])
        output_layout.addWidget(self.bit_depth_combo, 2, 1)
        
        output_group.setLayout(output_layout)
        bake_layout.addWidget(output_group)
        
        # Bake Options
        options_group = QGroupBox("Bake Options")
        options_layout = QGridLayout()
        options_layout.setSpacing(10)
        
        # Anti-aliasing
        options_layout.addWidget(QLabel("Anti-aliasing:"), 0, 0)
        self.aa_combo = QComboBox()
        self.aa_combo.addItems(["None", "2x", "4x", "8x"])
        self.aa_combo.setCurrentText("4x")
        options_layout.addWidget(self.aa_combo, 0, 1)
        
        # Edge Padding
        options_layout.addWidget(QLabel("Edge Padding:"), 1, 0)
        self.edge_padding_spin = QSpinBox()
        self.edge_padding_spin.setRange(0, 64)
        self.edge_padding_spin.setValue(16)
        self.edge_padding_spin.setSuffix(" px")
        options_layout.addWidget(self.edge_padding_spin, 1, 1)
        
        # Dilation Width
        options_layout.addWidget(QLabel("Dilation Width:"), 2, 0)
        self.dilation_spin = QSpinBox()
        self.dilation_spin.setRange(0, 32)
        self.dilation_spin.setValue(4)
        self.dilation_spin.setSuffix(" px")
        options_layout.addWidget(self.dilation_spin, 2, 1)
        
        options_group.setLayout(options_layout)
        bake_layout.addWidget(options_group)
        
        # Maps Settings
        maps_group = QGroupBox("Maps")
        maps_layout = QVBoxLayout()
        maps_layout.setSpacing(10)
        
        self.bake_settings = {}
        maps_config = {
            "Normal Map": {
                "options": {
                    "Format": ["OpenGL", "DirectX"],
                    "Surface Transfer": ["Closest", "Raycasting", "Subdivision"]
                }
            },
            "Ambient Occlusion": {
                "options": {
                    "Ray Count": [16, 32, 64, 128, 256],
                    "Max Distance": ["0.1", "0.5", "1.0", "2.0", "5.0"]
                }
            },
            "Curvature": {
                "options": {
                    "Mode": ["Average", "Cavity", "Convexity"],
                    "Radius": ["0.1", "0.5", "1.0", "2.0", "5.0"]
                }
            },
            "Position": {
                "options": {
                    "Space": ["World", "Local", "UV"]
                }
            },
            "Thickness": {
                "options": {
                    "Ray Count": [16, 32, 64, 128, 256],
                    "Max Distance": ["0.1", "0.5", "1.0", "2.0", "5.0"]
                }
            }
        }
        
        for map_name, config in maps_config.items():
            map_frame = QFrame()
            map_frame.setFrameStyle(QFrame.StyledPanel)
            map_layout = QGridLayout(map_frame)
            map_layout.setSpacing(10)
            
            # Enable checkbox
            enable_cb = QCheckBox(map_name)
            enable_cb.setChecked(True)
            map_layout.addWidget(enable_cb, 0, 0, 1, 2)
            
            # Map specific options
            row = 1
            map_settings = {"enabled": enable_cb}
            
            if "options" in config:
                for option_name, values in config["options"].items():
                    map_layout.addWidget(QLabel(f"{option_name}:"), row, 0)
                    combo = QComboBox()
                    combo.addItems([str(v) for v in values])
                    combo.setCurrentText(str(values[0]))
                    map_layout.addWidget(combo, row, 1)
                    map_settings[option_name] = combo
                    row += 1
            
            self.bake_settings[map_name] = map_settings
            maps_layout.addWidget(map_frame)
        
        maps_group.setLayout(maps_layout)
        bake_layout.addWidget(maps_group)
        
        return bake_group

    def toggle_external_cage(self):
        is_external = self.use_external_cage.isChecked()
        self.cage_file_edit.setEnabled(is_external)
        self.cage_file_btn.setEnabled(is_external)
        # Deaktiviere automatische Cage-Einstellungen wenn externer Cage verwendet wird
        self.cage_offset_spin.setEnabled(not is_external)
        self.ray_distance_spin.setEnabled(not is_external)
        self.match_uv_seams.setEnabled(not is_external)
        self.match_hard_edges.setEnabled(not is_external)

    def select_cage_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Cage Mesh",
            "",
            "Mesh Files (*.fbx *.obj);;All Files (*)"
        )
        if file_path:
            self.cage_file_edit.setText(file_path)

    def log(self, message, level="INFO"):
        """
        Fügt eine Nachricht zum Log hinzu
        level kann sein: INFO, WARNING, ERROR, SUCCESS
        """
        timestamp = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        
        # Farben für verschiedene Log-Level
        colors = {
            "INFO": "#ffffff",      # Weiß
            "WARNING": "#ffd700",   # Gelb
            "ERROR": "#ff4444",     # Rot
            "SUCCESS": "#00ff00"    # Grün
        }
        
        color = colors.get(level, "#ffffff")
        formatted_message = f'<span style="color: {color}">[{level}] {timestamp}: {message}</span>'
        
        self.log_text.append(formatted_message)
        # Scrolle automatisch nach unten
        self.log_text.verticalScrollBar().setValue(
            self.log_text.verticalScrollBar().maximum()
        )

    def clear_log(self):
        """Löscht den gesamten Log"""
        self.log_text.clear()

def main():
    app = QApplication(sys.argv)
    
    # Light Theme als Standard setzen
    window = MainWindow()
    set_light_theme(app)  # Setze Light Theme als Standard
    
    # Lade das gespeicherte Theme (falls vorhanden)
    if window.config.settings.get('theme', 'Light Theme') == 'Dark Theme':
        set_dark_theme(app)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
