import os
import yt_dlp

def download_youtube_mp3(video_url, output_folder="downloads"):
    try:
        # Çıktı klasörünü oluştur (eğer yoksa)
        os.makedirs(output_folder, exist_ok=True)

        # YT-DLP ayarlarını yap
        ydl_opts = {
            'format': 'bestaudio/best',  
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192', 
            }],
            'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),  
            'noplaylist': True,  
        }

        # İndirme işlemini başlat
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            print(f"İndirme Tamamlandı: {info.get('title', 'Bilinmeyen Başlık')}.mp3")
    
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Kullanıcıdan link al ve MP3 olarak indir
if __name__ == "__main__":
    video_url = input("YouTube linkini girin: ")
    download_youtube_mp3(video_url)
