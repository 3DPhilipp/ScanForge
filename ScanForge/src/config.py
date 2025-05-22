# src/config.py
"""Configuration management for ScanForge"""
import json
import os
from pathlib import Path

class Config:
    def __init__(self):
        self.config_dir = Path.home() / '.pipeline_tool'
        self.config_file = self.config_dir / 'config.json'
        self.presets_dir = self.config_dir / 'presets'
        
        # Create directories if they don't exist
        self.config_dir.mkdir(exist_ok=True)
        self.presets_dir.mkdir(exist_ok=True)
        
        # Default settings
        self.default_config = {
            'houdini_path': '',
            'marmoset_path': '',
            'last_project_dir': str(Path.home()),
            'default_preset': 'default'
        }
        
        self.settings = {
            'last_project_dir': '',
            'last_output_dir': '',
            'houdini_path': '',
            'marmoset_path': '',
            'houdini_project': '',
            'python_env': '',
            'license_file': ''
        }
        
        self.load_config()

    def load_config(self):
        """Load configuration from file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded_settings = json.load(f)
                    # Update settings while preserving default values for new settings
                    self.settings.update(loaded_settings)
        except Exception as e:
            print(f"Error loading config: {e}")
            # If loading fails, keep using default settings

    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
        except Exception as e:
            print(f"Error saving config: {e}")

    def save_preset(self, name, lod_settings):
        """Save LOD settings as a preset"""
        preset_file = self.presets_dir / f'{name}.json'
        with open(preset_file, 'w') as f:
            json.dump(lod_settings, f, indent=4)

    def load_preset(self, name):
        """Load a preset by name"""
        preset_file = self.presets_dir / f'{name}.json'
        if preset_file.exists():
            with open(preset_file, 'r') as f:
                return json.load(f)
        return None

    def get_presets(self):
        """Get list of available presets"""
        return [f.stem for f in self.presets_dir.glob('*.json')]

    # Application paths
    HOUDINI_PATH = ""
    MARMOSET_PATH = ""
    
    # Default directories
    DEFAULT_INPUT_DIR = ""
    DEFAULT_OUTPUT_DIR = ""
    
    # Bake settings
    DEFAULT_BAKE_RESOLUTION = 2048
    DEFAULT_CAGE_OFFSET = 0.02
    
    # LOD settings
    DEFAULT_LOD0_TRI_COUNT = 100000
    
    @classmethod
    def save(cls):
        # TODO: Implement settings save functionality
        pass
    
    @classmethod
    def load(cls):
        # TODO: Implement settings load functionality
        pass
