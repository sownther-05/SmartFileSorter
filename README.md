# SmartFileSorter

SmartFileSorter is a Python-based file organization tool that automatically organizes files into predefined categories such as Images, Documents, Videos, Audio, Code, Archives, and more. It uses a simple graphical user interface (GUI) powered by Tkinter to select a directory, and then organizes files by their extensions into the appropriate folders.

## Features

- **Automatic File Sorting**: Sorts files into categories like Images, Documents, Videos, Audio, Code, and more.
- **Customizable Categories**: Easily update the categories for sorting files.
- **Logging**: Detailed logs of the file movements are stored in a `file_organizer_log.txt` file for tracking.
- **User-Friendly Interface**: A simple GUI interface for selecting the folder to organize.

## Supported File Categories

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`, `.webp`, `.ico`
- **Documents**: `.pdf`, `.txt`, `.docx`, `.doc`, `.ppt`, `.pptx`, `.xls`, `.xlsx`, `.csv`, `.odt`, `.rtf`, `.md`, `.epub`, `.pages`
- **Videos**: `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`, `.wmv`, `.webm`, `.3gp`, `.mpeg`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.ogg`, `.flac`, `.m4a`, `.wma`, `.aiff`, `.alac`, `.opus`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.tar.gz`, `.tar.bz2`, `.xz`, `.iso`
- **Installers/Setup Files**: `.exe`, `.msi`, `.dmg`, `.pkg`, `.bat`, `.sh`, `.jar`, `.app`
- **Code/Programming Files**: `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.c`, `.php`, `.rb`, `.sql`, `.swift`, `.go`
- **Fonts**: `.ttf`, `.otf`, `.woff`, `.woff2`
- **System Files**: `.log`, `.bak`, `.swp`, `.tmp`, `.dat`, `.ini`
- **Spreadsheets**: `.xls`, `.xlsx`, `.ods`, `.csv`
- **Presentations**: `.ppt`, `.pptx`, `.odp`
- **Miscellaneous**: `.md`, `.epub`, `.json`, `.xml`, `.yml`, `.yaml`
- **Web Files**: `.html`, `.htm`, `.css`, `.js`, `.json`, `.xml`
- **Disk Image Files**: `.iso`, `.img`
- **Backup Files**: `.bak`, `.old`, `.backup`

## Installation

1. **Clone the Repository**:
git clone https://github.com/sownther-05/SmartFileSorter.git


2. **Create and Activate Virtual Environment**:
- Open a terminal and navigate to the project folder.
- Run the following commands to set up the environment:
python -m venv file_organizer_env file_organizer_env\Scripts\activate # On Windows source
file_organizer_env/bin/activate # On MacOS/Linux


3. **Install Required Libraries**:
- Once the virtual environment is activated, install the dependencies:
pip install -r requirements.txt


## Usage

1. **Run the Program**:
- To start the program, simply run the following command:

python file_organizer.py


2. **Select Folder**:
- A file explorer window will pop up where you can choose the folder you want to organize.

3. **Organizing Files**:
- The program will automatically organize the files in the selected folder into different categories based on their file extensions.
- The results will be logged in the `file_organizer_log.txt` file.

4. **Check the Folder**:
- After the organization is complete, check your folder for new subfolders created for each file category.

## Logging

- All the movements of files are logged in the `file_organizer_log.txt` file in the project directory.
- The logs contain details about each file that was moved and its new destination.

## Contributing

If you have any ideas for improving SmartFileSorter or want to contribute to its development, feel free to fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out for any questions or issues!
