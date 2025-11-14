# 🗂️ File Organizer Script

Script Python untuk mengatur file di folder Downloads secara otomatis berdasarkan tipe file.

## ✨ Fitur

- ✅ **Auto-deteksi** folder Downloads
- ✅ **12 kategori file** yang berbeda
- ✅ **Preview mode** - lihat dulu sebelum eksekusi
- ✅ **Handle duplicate names** - file bernama sama otomatis di-rename
- ✅ **Error handling** - menampilkan error jika ada masalah
- ✅ **Statistik lengkap** - laporan detail setelah selesai
- ✅ **Cross-platform** - bekerja di Windows, Mac, dan Linux

## 📊 Kategori File

| Kategori | Ekstensi File |
|----------|---------------|
| Images | .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp, .tiff, .ico |
| Documents | .pdf, .doc, .docx, .txt, .rtf, .xls, .xlsx, .ppt, .pptx |
| Videos | .mp4, .avi, .mov, .wmv, .flv, .mkv, .webm, .m4v |
| Audio | .mp3, .wav, .flac, .aac, .ogg, .wma, .m4a |
| Archives | .zip, .rar, .7z, .tar, .gz, .bz2, .iso, .dmg |
| Programs | .exe, .msi, .dmg, .pkg, .deb, .rpm, .apk |
| Scripts | .py, .js, .html, .css, .php, .java, .c, .cpp |
| Spreadsheets | .csv, .xls, .xlsx, .xlsm, .ods |
| Presentations | .ppt, .pptx, .key, .odp |
| Fonts | .ttf, .otf, .woff, .woff2 |
| Others | Semua ekstensi lainnya |

## 🚀 Cara Menggunakan

### 1. Clone Repository
```bash
git clone https://github.com/apringutawa/file-organizer.git
cd file-organizer 
```
### 2. Jalankan Script
``` bash
python rapikanfile.py
```
3. Pilih Opsi
```text
🗂️  FILE ORGANIZER SCRIPT
==================================================

Pilih opsi:
1. 👀 Preview file yang akan dipindahkan
2. 🚀 Jalankan organizer (pindahkan file)
3. ❌ Keluar

Masukkan pilihan (1-3):
```
🛠️ Requirements
```
Python 3.6 atau lebih baru

Tidak perlu install library tambahan (menggunakan library standar Python)
```
📝 Customization
Anda bisa menambah kategori dengan mengedit bagian categories dalam script:

```python
categories = {
    "KategoriBaru": [".ext1", ".ext2", ".ext3"],
    # ... kategori lainnya
}
```
⚠️ Important Notes
```
Script hanya memindahkan file, tidak menghapus
File yang sedang digunakan mungkin tidak bisa dipindahkan
Selalu backup data penting sebelum menjalankan pertama kali
File hidden (diawali titik) akan di-skip
```

🐛 Troubleshooting
```
Error: "Permission denied"

Tutup aplikasi yang mungkin menggunakan file tersebut

Jalankan command prompt sebagai administrator (Windows)

Error: Python not found

Pastikan Python sudah terinstall dan ada di PATH

Gunakan python3 instead of python pada beberapa sistem
```
🤝 Contributing
Silakan fork repository ini dan buat pull request untuk improvements.

📄 License
MIT License - bebas digunakan untuk personal maupun komersial.
