import os
import shutil
import logging
import tkinter as tk
from tkinter import filedialog

# Set up logging configuration
logging.basicConfig(
    filename='file_organizer_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Function to select the directory using tkinter
def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder_selected = filedialog.askdirectory()  # Open a folder selection dialog
    return folder_selected

# Function to define file categories
def get_categories():
    return {
        
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.ico'],
    "Documents": ['.pdf', '.txt', '.docx', '.doc', '.xls', '.xlsx', '.csv', '.odt', '.rtf', '.md', '.epub', '.pages'],
    "Videos": ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm', '.3gp', '.mpeg'],
    "Audio": ['.mp3', '.wav', '.aac', '.ogg', '.flac', '.m4a', '.wma', '.aiff', '.alac', '.opus'],
    "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz', '.tar.gz', '.tar.bz2', '.xz'],
    "Installers/Setup Files": ['.exe', '.msi', '.dmg', '.pkg', '.bat', '.sh', '.jar', '.app'],
    "Code/Programming Files": ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.sql', '.swift', '.go'],
    "Fonts": ['.ttf', '.otf', '.woff', '.woff2'],
    "System Files": ['.log', '.bak', '.swp', '.tmp', '.dat', '.ini'],
    "Spreadsheets": ['.xls', '.xlsx', '.ods'],
    "Presentations": ['.ppt', '.pptx', '.odp'],
    "Miscellaneous": ['.md', '.epub', '.json', '.xml', '.yml', '.yaml'],
    "Web Files": ['.html', '.htm', '.js', '.json'],
    "Disk Image Files": ['.iso', '.img'],
    "Backup Files": ['.bak', '.old', '.backup']


    }

# Function to create a folder if it doesn't exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to organize the files
def organize_files(directory):
    categories = get_categories()  # Get file categories

    # Create folders for each category
    for category in categories.keys():
        create_folder(os.path.join(directory, category))

    # Move files into respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):  # Check if it's a file
            for category, extensions in categories.items():
                if any(filename.endswith(ext) for ext in extensions):
                    new_location = os.path.join(directory, category, filename)
                    shutil.move(file_path, new_location)  # Move the file
                    logging.info(f"Moved: {filename} to {category}")
                    print(f"Moved: {filename} to {category}")  # Optional: for user feedback
                    break

# Main function to execute the script
def main():
    directory = select_directory()  # Get directory from user
    print(f"Organizing files in: {directory}")
    
    organize_files(directory)  # Organize files into categories
    
    print("Organizing complete.")

# Run the script
if __name__ == "__main__":
    main()
