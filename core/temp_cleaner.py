import os
import tempfile
import shutil

class TempCleaner:
    def __init__(self):
        self.temp_dir = tempfile.gettempdir()

    def delete(self):
        total_size_cleared = 0

        if os.path.exists(self.temp_dir):
            for root, dirs, files in os.walk(self.temp_dir):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    try:
                        total_size_cleared += os.path.getsize(filepath)
                        os.remove(filepath)
                    except PermissionError:
                        print(f"PermissionError: Cannot delete {filepath}")
                    except Exception as e:
                        print(f"Error: {e} - {filepath}")

            for directory in dirs:
                dirpath = os.path.join(root, directory)
                try:
                    shutil.rmtree(dirpath)
                except PermissionError:
                    print(f"PermissionError: Cannot delete directory {dirpath}")
                except Exception as e:
                    print(f"Error: {e} - {dirpath}")

        return total_size_cleared / (1024 * 1024)  # Return size in MB
