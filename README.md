# YouTube MP3 Downloader (DISCONTINUED)
=========================

**Version 1.0.0 Alpha** 🎉

A simple and efficient script to download YouTube videos as MP3 files.

**What is this script?**
------------------------

This script uses the `yt_dlp` library to download YouTube videos as MP3 files. It allows you to download multiple videos at once by providing a text file with the video URLs.

**How does it work?**
----------------------

1. **Provide a text file**: Create a text file with the YouTube video URLs, one URL per line.
2. **Run the script**: Run the script and select the text file you created.
3. **Choose a folder**: Select a folder to save the downloaded MP3 files.
4. **Download**: The script will download the MP3 files and save them to the selected folder.

**Features**
------------

* Download multiple YouTube videos as MP3 files at once
* Supports high-quality audio downloads (up to 192 kbps)
* Easy to use and configure

**Requirements**
---------------

* Python 3.6+
* `yt_dlp` library (install with `pip install yt_dlp`)
* `ffmpeg` executable (install with your distribution's package manager)

**Instructions**
--------------

1. **Install the requirements**: Install Python, `yt_dlp`, and `ffmpeg` using the above instructions.
2. **Create a text file**: Create a text file with the YouTube video URLs, one URL per line.
3. **Run the script**: Run the script using Python (e.g., `python youtube_mp3_downloader.py`).
4. **Select the text file**: Select the text file you created when prompted.
5. **Choose a folder**: Select a folder to save the downloaded MP3 files.
6. **Download**: The script will download the MP3 files and save them to the selected folder.

**Example Use Case**
--------------------

* Create a text file called `urls.txt` with the following contents:
```txt
https://www.youtube.com/watch?v=jNQXAC9IVRw
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
* Run the script and select `urls.txt` as the input file.
* Choose a folder to save the downloaded MP3 files (e.g., `~/Music`).
* The script will download the MP3 files and save them to the selected folder.

**Troubleshooting**
------------------

* Make sure you have the latest version of `yt_dlp` installed.
* Check that the `ffmpeg` executable is installed and configured correctly. You can check the location of the installation of `ffmpeg` by using this command `whereis ffmpeg`
* If you encounter any issues, please open an issue on this repository.

**License**
---------

This script is licensed under the MIT License.

**Contributing**
--------------

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

**Credits**
--------------
Thanks to Saru2003 for fixing the First issue with the script (unexpected exit after empty file)

**Changelog**
-------------

* **1.0.0 Alpha**: Initial release 🎉
