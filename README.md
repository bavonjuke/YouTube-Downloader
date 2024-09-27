# YouTube-Downloader
Script to download YouTube mp3 files


YouTube to MP3 Downloader
This Python script allows you to download audio(s) from YouTube videos and convert them to MP3 format. It provides an interactive command-line interface for ease of use.
Features

Download audio from multiple YouTube videos at once
Convert downloaded audio to MP3 format
Specify custom download location
Uses a default FFmpeg path, with option to specify a custom path

Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.6 or higher
FFmpeg installed on your system
yt-dlp Python library

Installation

Clone this repository

Navigate to the project directory:
Copycd youtube-to-mp3-downloader

Install the required Python library:
Copypip install yt-dlp

Ensure FFmpeg is installed and the path in the script is correct.

Usage

Run the script:
Copypython youtube_to_mp3_downloader.py

Enter YouTube links when prompted (one per line). Press Enter twice to finish entering links.
Specify the folder where you want to save the MP3 files.
The script will download the audio and convert it to MP3 format.

Configuration
The default FFmpeg path is set to:
pythonCopyDEFAULT_FFMPEG_PATH = r"C:\Users\ffmeg_path_on_your_disk"
If your FFmpeg is installed in a different location, update this path in the script.
