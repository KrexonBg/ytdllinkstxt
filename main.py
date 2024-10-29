import os
import sys
from yt_dlp import YoutubeDL
from helpers import is_non_zero_file

# Function to download videos and save to a specific directory
def download_mp3(youtube_url, output_folder):
    ydl_opts = {
        'format':
        'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl':
        os.path.join(output_folder, '%(title)s.%(ext)s'),
        'ffmpeg_location':
        '/usr/bin/ffmpeg'  # Linux example
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])


# Ask for the folder name
folder_name = input(
    "Enter the folder name (or press Enter to use the current directory): ")
if folder_name:
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    os.chdir(folder_name)

# Scan the current directory for .txt files
txt_files = [f for f in os.listdir() if f.endswith('.txt')]
print(txt_files)

# Check if there are any.txt files
if not txt_files:
    print("No.txt files found in the current directory.")
    sys.exit(1)

# List the.txt files and ask the user to select one
print("Available playlists:")
for i, file in enumerate(txt_files, start=1):
    print(f"{i} - {file}")

while True:
    choice = input(
        "Which playlist do you want to be downloaded? (Enter the number) > ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(txt_files):
            selected_file = txt_files[choice - 1]
            break
        else:
            print("Invalid choice. Please enter a number within the range.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Create the output folder if it doesn't exist
output_folder_name = os.path.splitext(selected_file)[0]
if not os.path.exists(output_folder_name):
    os.makedirs(output_folder_name)

try:
    with open(selected_file, 'r') as file:
        if not is_non_zero_file(selected_file): # file length is zero
            print("Empty file selected.")
            sys.exit(1)
        for line in file:
            youtube_url = line.strip()
            if youtube_url:  # Check if the line is not empty
                print(f"Downloading {youtube_url}...")
                download_mp3(youtube_url, output_folder_name)
                print(f"Downloaded and saved to {output_folder_name}")
except FileNotFoundError:
    print(f"File {selected_file} not found.")
    sys.exit(1)
