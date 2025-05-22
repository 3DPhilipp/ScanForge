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
        
        self.load_config()

    def load_config(self):
        """Load configuration from file or create default if not exists"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.settings = json.load(f)
        else:
            self.settings = self.default_config
            self.save_config()

    def save_config(self):
        """Save current configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=4)

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
