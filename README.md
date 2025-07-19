📂 Pengunggah Berkas Lokal (Local File Uploader)
Sebuah aplikasi web sederhana yang dibangun dengan Python dan Flask untuk membuat server uploader file pribadi di laptop Anda. Transfer file antar perangkat di jaringan lokal Anda dengan mudah, tanpa perlu cloud storage atau kabel data.

✨ Fitur Utama
📤 Unggah Multi-File: Pilih atau seret beberapa file sekaligus.

👆 Drag & Drop: Area unggah modern yang mendukung seret dan letakkan file.

📊 Progress Bar Individual: Lacak progress unggahan untuk setiap file secara terpisah, lengkap dengan nama dan hitungan file.

🗂️ Kategori Otomatis: File yang diunggah secara otomatis dikelompokkan ke dalam folder (Foto, Video, Dokumen, Kompres, Lainnya).

🔄 Konversi JPG ke PNG: Semua file .jpg atau .jpeg akan otomatis dikonversi menjadi format .png saat disimpan.

📱 Akses via QR Code: Pindai QR code yang dibuat otomatis untuk membuka uploader di ponsel atau tablet Anda.

💻 Penyimpanan Lokal: Semua file disimpan langsung di laptop Anda, memberikan privasi dan kontrol penuh.

⚙️ Ringan & Cepat: Dibangun dengan Flask yang minimalis, tanpa dependensi yang berat.

🚀 Berjalan Saat Startup: Dapat diatur untuk berjalan otomatis saat komputer dinyalakan.

🛠️ Teknologi yang Digunakan
Backend: Python 3, Flask

Frontend: HTML5, CSS3, JavaScript (Vanilla)

Library Python: Pillow (untuk gambar), qrcode

🚀 Instalasi & Penggunaan
Ikuti langkah-langkah ini untuk menjalankan aplikasi di komputer Anda.

1. Persiapan Awal
Pastikan Anda sudah menginstal Python 3 di sistem Anda.

2. Clone Repositori
Buka terminal atau Git Bash Anda dan clone repositori ini:

Bash

git clone https://github.com/nama-anda/nama-repositori.git
cd nama-repositori
(Ganti nama-anda/nama-repositori dengan URL repositori Anda)

3. Buat Virtual Environment (Sangat Disarankan)
Ini akan mengisolasi dependensi proyek Anda.

Bash

# Untuk Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Untuk Windows
python -m venv venv
.\venv\Scripts\activate
4. Install Dependensi
Proyek ini memerlukan beberapa library Python. Buat file bernama requirements.txt di dalam folder proyek Anda dan isi dengan:

Plaintext

Flask
Pillow
qrcode[pil]
Kemudian, install semuanya dengan perintah:

Bash

pip install -r requirements.txt
5. Jalankan Aplikasi
Setelah semua dependensi terinstal, jalankan server Flask:

Bash

python app.py
6. Akses Uploader Anda
Buka browser di laptop Anda dan kunjungi http://127.0.0.1:5000.

Untuk mengakses dari perangkat lain (ponsel/tablet), pastikan perangkat tersebut terhubung ke jaringan Wi-Fi yang sama, lalu pindai QR code yang muncul di halaman web.

ऑटो-स्टार्ट (Menjalankan Saat Startup)
Anda bisa mengkonfigurasi skrip ini agar berjalan otomatis saat komputer menyala dengan mengikuti panduan untuk sistem operasi Anda (menggunakan file .bat di Windows, Login Items di macOS, atau systemd di Linux).
