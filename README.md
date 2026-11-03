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