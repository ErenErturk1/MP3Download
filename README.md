Bu kodun düzgün çalışabilmesi için aşağıdaki Python kütüphanelerinin yüklü olması gerekir:

yt-dlp: YouTube videolarını indirmek ve işlemek için kullanılan ana kütüphane. Bu kütüphaneyi yüklemek için şu komutu kullanabilirsiniz:
pip install yt-dlp

FFmpeg: Ses dosyalarını işlemek (MP3'ye dönüştürmek) için gerekli bir araçtır. yt-dlp MP3 dönüştürme işlemi için FFmpeg'i kullanır. FFmpeg'i yüklemek için şu adımları izleyebilirsiniz:
Windows:
FFmpeg'in resmi web sitesinden uygun sürümü indirip yükleyin.
Yükleme tamamlandıktan sonra, FFmpeg'in sistem yoluna (PATH) eklendiğinden emin olun.

MacOS/Linux:
brew install ffmpeg  # Homebrew kullananlar için
veya
sudo apt install ffmpeg  # Debian/Ubuntu tabanlı sistemler için
Yukarıdaki kütüphaneleri yükledikten sonra, kod sorunsuz bir şekilde çalışmalıdır.
