# src/config.py
class Config:
    def __init__(self):
        self.settings = {
            'last_project_dir': '',
            'last_output_dir': '',
            'houdini_path': '',
            'marmoset_path': '',
            'houdini_project': '',
            'python_env': '',
            'license_file': ''
        }

    def save_config(self):
        """
        Save configuration to file
        """
        pass  # Wir implementieren das Speichern später

    def load_config(self):
        """
        Load configuration from file
        """
        pass  # Wir implementieren das Laden später

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
