from pytube import YouTube
import os


def downTubeVideo(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
    print(yt.title)


def downTubeMusic(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(only_audio=True).first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)


video = input("Digite o link do vídeo desejado: ")
confirm = input("Deseja baixar só o audio? s/n: ")

if confirm == "s" or "S":
    path = "/home/wopgan/Música/DownTube"
    downTubeMusic(video, path)

else:
    path = "/home/wopgan/Vídeos/DownTube"
    downTubeVideo(video, path)
