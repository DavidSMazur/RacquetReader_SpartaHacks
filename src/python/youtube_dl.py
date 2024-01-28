from pathlib import Path
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Specify the YouTube URL
# youtube_url = 'https://www.youtube.com/shorts/G7ZJNaszMrc'
# youtube_url = 'https://www.youtube.com/watch?v=oOsmGn2_piE'
# youtube_url = 'https://youtu.be/kmwzGXRen3s?si=R2WfxvhnaI65Fdol&t=174'
# youtube_url = 'https://www.youtube.com/watch?v=EFY460oquXw' #255,260
# youtube_url = 'https://www.youtube.com/watch?v=zMfN8T6Giio' # 0,2.5
youtube_url = 'https://www.youtube.com/watch?v=e-b7yuRSogo' #0, 2.5; 11, 12.5


# Create a YouTube object
yt = YouTube(youtube_url)

# Specify the relative path to the data directory
data_dir = Path('data/video')

# Download the highest quality video to the data directory
download_path = yt.streams.get_highest_resolution().download(data_dir)

# Optional: specify the start and end times of the segment you want to save (in seconds)

start_time = 11
end_time = 12.5

# Specify the output file for the segment
output_file = Path(data_dir, 'coach.mp4')

# Extract the segment and save it
ffmpeg_extract_subclip(download_path, start_time, end_time, targetname=output_file)

# Path(download_path).replace(Path(download_path).with_suffix('.mp4'))
# Delete the original downloaded file
Path.unlink(Path(download_path))