from pytube import YouTube
import os

def downTube(videourl, path):
    yt = YouTube(videourl)
    confirm = input("Deseja baixar apenas o audio? s/n: ") 
    if confirm == "n" or "N":
        yt = yt.streams.filter(progressive=True, file_extension='mp4'). order_by('resolution').desc().first()
    elif conffime == "s" or "S":
        yt = yt.streams.filter(only_audio=True).first()

    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

file = input("Digite o link para download do arquivo: ")
user = input("Digite o usuário que você está usando: ")
path = (f"/home/{user}/Downloads/DownTube")

downTube(file, path)
