# Windows System Cleaner

## Overview

The System Cleaner application is a Python-based tool built using PyQt6 for the user interface and various modules for cleaning files, cache, and temporary files on the system. It provides a graphical interface for users to select options to clean up their system based on specified criteria.

## Features


- **Cache Cleaner**: Clears cache storage on the system to free up space.
- **Temp File Cleaner**: Deletes temporary files to improve system performance.
- **Progress Meter**: Visual representation of the amount of storage cleared during operations.
- **Toast Notifications**: Displays success messages for operations like file deletion and cache clearing.

## Requirements

- Python 3.6+
- PyQt6
- PySide6 (for UI components)


## Installation

1. Clone the repository:
   ```
   git clone https://github.com/nigrumpirate/windowsyscleaner.git
   cd windowsyscleaner
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Build the executable using PyInstaller (or alternative):

   - For PyInstaller:
     ```
     pyinstaller main.py --onefile --windowed --name SystemCleaner --icon=icon.ico
     ```

   - For cx_Freeze or Py2exe, refer to their respective documentation for build instructions.

4. Run the executable:
   - Navigate to the `dist` directory after building.
   - Double-click on `SystemCleaner.exe` to launch the application.
  

### OR

- You can run the main.py file directly by `python main.py or python3 main.py`

## Usage

- Launch the `SystemCleaner.exe` executable.
- Click on "Button" to initiate operations.
- Progress and success messages will be displayed in the application window.
- Adjust UI elements and behavior as needed by modifying the Python scripts (`main.py`, UI components) and styles (`styles.qss`).

## Troubleshooting

- **Antivirus Issues**: If the executable is flagged by antivirus software, exclude the build directory from scans or report it as a false positive.
- **File Not Found**: Ensure that all required files (`styles.qss`, icons) are included in the build process using `--add-data` or equivalent options.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.


