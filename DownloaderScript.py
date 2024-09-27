import yt_dlp
import os

# Set the default FFmpeg path to the one provided
DEFAULT_FFMPEG_PATH = r"C:\Users\ffpeg_path_\"

def get_youtube_links():
    links = []
    print("Enter YouTube links (one per line). Press Enter twice to finish:")
    while True:
        link = input().strip()
        if link:
            links.append(link)
        else:
            break
    return links

def get_download_location():
    while True:
        location = input("Enter the folder path to save MP3 files: ").strip()
        if os.path.isdir(location):
            return location
        else:
            create = input(f"The folder '{location}' doesn't exist. Create it? (y/n): ").lower()
            if create == 'y':
                os.makedirs(location)
                return location
            else:
                print("Please enter a valid folder path.")

def download_youtube_as_mp3(urls, output_folder, ffmpeg_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg_path,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                ydl.download([url])
                print(f"Successfully downloaded: {url}")
            except Exception as e:
                print(f"Error downloading {url}: {str(e)}")

if __name__ == "__main__":
    print("YouTube to MP3 Downloader")
    print("-----------------------")

    youtube_urls = get_youtube_links()
    output_folder = get_download_location()

    # Use the default FFmpeg path
    ffmpeg_path = DEFAULT_FFMPEG_PATH

    # Check if the default FFmpeg path exists
    if not os.path.isfile(ffmpeg_path):
        print(f"Warning: FFmpeg not found at the default location: {ffmpeg_path}")
        custom_path = input("Enter the correct path to FFmpeg, or press Enter to use system PATH: ").strip()
        if custom_path:
            ffmpeg_path = custom_path
        else:
            ffmpeg_path = None  # This will make yt-dlp use the system PATH

    print("\nStarting downloads...")
    download_youtube_as_mp3(youtube_urls, output_folder, ffmpeg_path)
    print("\nDownload process completed.")
