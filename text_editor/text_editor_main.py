
from file import File

class TextEditorSingleton:
    # class instance
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TextEditorSingleton, cls).__new__(cls)
            # Additional initialization can be done here
        return cls._instance

    def __init__(self):
        pass
    

    def create_file(self, name: str, capacity: int):
        """
        Functional API to create files
        """
        print("--File Created---")
        # initialize instance of the file and return
        file_obj = File(capacity)
        return file_obj