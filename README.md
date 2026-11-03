# FolderOrganizer 🗂️

A terminal-based file organizer written in Python. It scans a folder and moves each file into a subfolder based on its extension, bringing order to your cluttered downloads or other directories in just a few seconds.

<br>

## Features ✨

* Centralized terminal interface, featuring an interactive menu and an animated loading bar;

* Automatic organization by file type;

* Automatic creation of the necessary subfolders;

* Overwrite protection: if a file with the same name already exists at the destination, it is ignored;

* Error handling with a user-friendly message;

* Compatible with Windows, Linux, and macOS (screen clearing via cls/clear).

<br>

## Categories 📁

<br>

Folder | Extensions
:------: | :-----------------------:
Images | .jpg, .jpeg, .png, .webp, .gif, .tiff, .bmp, .raw, .svg, .ai, between others
Documents | .pdf, .txt, .doc, .docx, .odt, .rtf, .xls, .xlsx, .pptx, .html, between others
Videos | .mp4, .mov, .avi, .mkv, .webm, .wmv, .flv, .mpg, between others
Audio | .mp3, .wav, .flac, .m4a, .aac, .wma, between others
Executables | .exe, .msi, .bat, .cmd, .sh, .app, .dmg, between others
ZIP_folders | .zip
ISO | .iso, .torrent, .vbo-extpack

<br>

## Requirements 🚀

Python 3.15 or higher, as the code uses lazy imports (PEP 810) and match/case.

<br>

## Execution 🔮

~~~Bash
git clone https://github.com/seu-usuario/FolderOrganizer.git
cd FolderOrganizer
python folder_organizer.py
~~~

* In the menu, enter 1 to organize or 2 to exit.

* Provide the folder path relative to your user folder (for example, Downloads or Documents/Projects).

* Wait for the loading bar. The files will be moved into their corresponding subfolders.

<br>

## How it works ⚙️

* Defines a dictionary that maps each category to its corresponding file extensions.

* Creates subfolders within the chosen directory (using `mkdir(exist_ok=True)`).

* Iterates through the items in the folder using `Path.iterdir()` and compares each file's extension (converted to lowercase) against the defined categories.

* Moves the file using `shutil.move`, provided that no other file with the same name already exists at the destination.

<br>

## Technologies 🛠️

* Python 3

* Standard libraries: pathlib, shutil, os, sys, time, builtins

<br>

## Notes ⚠️

* Files with extensions not listed remain in the original folder.

* Existing subfolders are left untouched; only loose files located at the root of the chosen folder are affected.

* The path is always resolved relative to Path.home().

* It is recommended to test this in a separate test folder first, as the operation moves the files.

<br>

## Ideas for the future 📄

* Support for more extensions (.7z, .rar, .csv, .json, etc.);

* Option to undo the organization process;

* Preview mode (dry run);

* Support for absolute paths;

* Rename duplicate files instead of ignoring them.