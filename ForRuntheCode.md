TR
-----
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
-------------------------------------------------------------------------------------------------------------------------------------------------------

Eng
-----
For this code to work properly, the following Python libraries must be installed:

yt-dlp: The main library used to download and process YouTube videos. You can use the following command to install this library:
pip install yt-dlp

FFmpeg: An essential tool for processing audio files (converting them to MP3). yt-dlp uses FFmpeg for MP3 conversion. To install FFmpeg, you can follow these steps:
Windows:
Download and install the appropriate version from FFmpeg's official website.
After the installation is complete, make sure FFmpeg is added to the system path (PATH).

MacOS/Linux:
brew install ffmpeg # For Homebrew users
or 
sudo apt install ffmpeg # For Debian/Ubuntu based systems
After installing the above libraries, the code should run smoothly.
