import os
from pytube import YouTube

def download_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        stream.download(output_path)
        print(f"Video downloaded successfully to: {output_path}/{yt.title}.mp4")
    except Exception as e:
        print("An error occurred while downloading the video:", str(e))

def download_music(video_url, output_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        stream.download(output_path)
        print(f"Audio downloaded successfully to: {output_path}/{yt.title}.mp4")
    except Exception as e:
        print("An error occurred while downloading the audio:", str(e))

if __name__ == "__main__":
    home = os.path.expanduser("~")
    video_url = input("Enter the video URL: ").strip()
    download_audio = input("Do you want to download audio only? (y/n): ").strip().lower()

    if download_audio == "y":
        path = os.path.join(home, "Music", "DownTube")
        download_music(video_url, path)
        print(f"Saved in: {path}/{yt.title}.mp4")
    elif download_audio == "n":
        path = os.path.join(home, "Videos", "DownTube")
        download_video(video_url, path)
        print(f"Saved in: {path}/{yt.title}.mp4")
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")
