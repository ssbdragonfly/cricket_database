from download_video import download_video
from extract_over_and_ball import process_video
from save_data import save_data

def main():
    video_url = input("Enter the YouTube video URL: ")
    video_path = download_video(video_url)
    over_and_ball_info = process_video(video_path)
    shot_types = ['Drive', 'Pull', 'Cut', 'Sweep', 'Hook']
    save_data(over_and_ball_info, shot_types)

if __name__ == "__main__":
    main()
