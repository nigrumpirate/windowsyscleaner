import os
import time

class FileCleaner:
    def __init__(self, days):
        self.days = days

    def clean(self, directory):
        now = time.time()
        cutoff = now - (self.days * 86400)
        total_size_cleared = 0

        for root, dirs, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                if os.path.getmtime(filepath) < cutoff:
                    total_size_cleared += os.path.getsize(filepath)
                    os.remove(filepath)
                    print(f"Deleted: {filepath}")

        return total_size_cleared / (1024 * 1024)  # Return size in MB
