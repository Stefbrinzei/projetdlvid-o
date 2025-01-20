import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best[ext=mp4]',  # Télécharge directement le meilleur format MP4 disponible
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Téléchargement en cours...")
            ydl.download([url])
            print("Téléchargement terminé!")
    except Exception as e:
        print(f"Une erreur est survenue : {str(e)}")

if __name__ == "__main__":
    link = input("Entrez le lien de la vidéo Youtube : ")
    download_video(link)