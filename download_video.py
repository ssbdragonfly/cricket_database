import ssl
import certifi
from pytube import YouTube

ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl._create_default_https_context = ssl._create_unverified_context

def download_video(url, output_path='videos/'):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4').first()
    stream.download(output_path)
    return output_path + stream.default_filename

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    video_path = download_video(video_url)
    print(f"Video downloaded to: {video_path}")
