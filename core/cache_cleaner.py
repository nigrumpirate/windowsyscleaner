import os
import shutil

class CacheCleaner:
    def __init__(self):
        self.cache_dirs = [os.path.expanduser('~/.cache'), '/tmp']

    def clear(self):
        total_size_cleared = 0

        for cache_dir in self.cache_dirs:
            if os.path.exists(cache_dir):
                for root, dirs, files in os.walk(cache_dir):
                    for filename in files:
                        filepath = os.path.join(root, filename)
                        total_size_cleared += os.path.getsize(filepath)
                shutil.rmtree(cache_dir)
                os.makedirs(cache_dir)
                print(f"Cleared: {cache_dir}")

        return total_size_cleared / (1024 * 1024)  # Return size in MB
