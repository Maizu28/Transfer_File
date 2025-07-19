import os
import socket
import qrcode
from PIL import Image
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

# --- FUNGSI & KONFIGURASI AWAL ---
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

app = Flask(__name__)
PORT = 5000
LOCAL_URL = f"http://{get_local_ip()}:{PORT}"

# --- PEMBUATAN QR CODE SAAT STARTUP ---
STATIC_FOLDER = 'static'
os.makedirs(STATIC_FOLDER, exist_ok=True)
qr_img = qrcode.make(LOCAL_URL)
qr_img.save(os.path.join(STATIC_FOLDER, "local_qr.png"))
print(f"[*] QR Code dibuat untuk alamat: {LOCAL_URL}")

# --- PENGATURAN KATEGORI FILE ---
UPLOAD_FOLDER = 'uploads'
CATEGORIES = {
    'foto': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'],
    'video': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm'],
    'documen': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.rtf', '.csv'],
    'compress': ['.zip', '.rar', '.7z', '.tar', '.gz']
}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
for category in list(CATEGORIES.keys()) + ['lainnya']:
    os.makedirs(os.path.join(UPLOAD_FOLDER, category), exist_ok=True)

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return 'lainnya'

# --- RUTE APLIKASI WEB ---
@app.route('/')
def index():
    categorized_files = {}
    for category in os.listdir(app.config['UPLOAD_FOLDER']):
        category_path = os.path.join(app.config['UPLOAD_FOLDER'], category)
        if os.path.isdir(category_path):
            files = sorted(os.listdir(category_path), reverse=True)
            if files:
                categorized_files[category] = files
    
    sorted_categorized_files = {k: categorized_files[k] for k in sorted(categorized_files.keys())}
    return render_template('index.html', categorized_files=sorted_categorized_files, local_url=LOCAL_URL)

# --- FUNGSI UPLOAD FILE (DIPERBARUI UNTUK MULTI-FILE) ---
@app.route('/upload', methods=['POST'])
def upload_file():
    # Gunakan getlist untuk mendapatkan semua file dari input 'file'
    uploaded_files = request.files.getlist("file")
    
    if not uploaded_files:
        return redirect(request.url)

    for file in uploaded_files:
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            
            # Logika konversi JPG ke PNG tetap berlaku untuk setiap file
            if filename.lower().endswith(('.jpg', '.jpeg')):
                image = Image.open(file.stream).convert("RGBA")
                base_filename = os.path.splitext(filename)[0]
                filename = f"{base_filename}.png"
                category = get_category(filename)
                save_path = os.path.join(app.config['UPLOAD_FOLDER'], category, filename)
                image.save(save_path, 'PNG')
            else:
                category = get_category(filename)
                save_path = os.path.join(app.config['UPLOAD_FOLDER'], category, filename)
                file.save(save_path)
            
    return redirect(url_for('index'))

@app.route('/uploads/<category>/<filename>')
def uploaded_file(category, filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], category), filename)

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=PORT)