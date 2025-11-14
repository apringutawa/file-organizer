import os
import shutil
from pathlib import Path

def organize_downloads_folder():
    # Path folder Download (otomatis detect OS)
    downloads_path = Path.home() / "Downloads"
    
    # Mapping ekstensi file ke folder
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods"],
        "Videos": [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm", ".m4v", ".3gp"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso", ".dmg"],
        "Programs": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".apk"],
        "Scripts": [".py", ".js", ".html", ".css", ".php", ".java", ".c", ".cpp", ".json", ".xml"],
        "Spreadsheets": [".csv", ".xls", ".xlsx", ".xlsm", ".ods"],
        "Presentations": [".ppt", ".pptx", ".key", ".odp"],
        "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
        "Others": []  # Untuk file dengan ekstensi tidak dikenal
    }
    
    # Buat folder jika belum ada
    for category in categories:
        (downloads_path / category).mkdir(exist_ok=True)
    
    # Counter untuk statistik
    moved_files = 0
    errors = 0
    
    print("🔍 Memindai folder Download...")
    print(f"📁 Lokasi: {downloads_path}")
    print("-" * 50)
    
    # Loop melalui semua file di folder Download
    for file_path in downloads_path.iterdir():
        # Skip jika ini folder atau file hidden
        if file_path.is_dir() and file_path.name in categories:
            continue
        if file_path.name.startswith('.') or file_path.name == "file_organizer.py":
            continue
        
        if file_path.is_file():
            # Dapatkan ekstensi file
            extension = file_path.suffix.lower()
            
            # Cari kategori yang sesuai
            destination_folder = "Others"
            for category, extensions in categories.items():
                if extension in extensions:
                    destination_folder = category
                    break
            
            # Path tujuan
            destination_path = downloads_path / destination_folder / file_path.name
            
            try:
                # Handle file dengan nama yang sama
                counter = 1
                original_destination = destination_path
                while destination_path.exists():
                    stem = file_path.stem
                    suffix = file_path.suffix
                    destination_path = downloads_path / destination_folder / f"{stem}_{counter}{suffix}"
                    counter += 1
                
                # Pindahkan file
                shutil.move(str(file_path), str(destination_path))
                print(f"✅ {file_path.name} → {destination_folder}/")
                moved_files += 1
                
            except Exception as e:
                print(f"❌ Gagal memindahkan {file_path.name}: {str(e)}")
                errors += 1
    
    # Tampilkan statistik
    print("-" * 50)
    print(f"📊 Statistik:")
    print(f"   ✅ File berhasil dipindahkan: {moved_files}")
    print(f"   ❌ Error: {errors}")
    print(f"   📁 Total kategori: {len(categories)}")
    
    # Tampilkan isi folder yang diorganisir
    print("\n📂 Struktur folder setelah diatur:")
    for category in categories:
        category_path = downloads_path / category
        if category_path.exists():
            file_count = len([f for f in category_path.iterdir() if f.is_file()])
            print(f"   📁 {category}: {file_count} file")

def preview_organization():
    """Fungsi untuk preview sebelum memindahkan file"""
    downloads_path = Path.home() / "Downloads"
    
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods"],
        "Videos": [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm", ".m4v", ".3gp"],
        "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso", ".dmg"],
        "Programs": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".apk"],
        "Scripts": [".py", ".js", ".html", ".css", ".php", ".java", ".c", ".cpp", ".json", ".xml"],
        "Spreadsheets": [".csv", ".xls", ".xlsx", ".xlsm", ".ods"],
        "Presentations": [".ppt", ".pptx", ".key", ".odp"],
        "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
        "Others": []
    }
    
    print("👀 PREVIEW - File yang akan dipindahkan:")
    print("-" * 50)
    
    file_count = 0
    for category, extensions in categories.items():
        category_files = []
        for file_path in downloads_path.iterdir():
            if file_path.is_file() and not file_path.name.startswith('.'):
                if file_path.suffix.lower() in extensions or (category == "Others" and not any(file_path.suffix.lower() in ext_list for ext_list in categories.values())):
                    category_files.append(file_path.name)
        
        if category_files:
            print(f"📁 {category}:")
            for file in category_files[:5]:  # Tampilkan max 5 file per kategori
                print(f"    📄 {file}")
            if len(category_files) > 5:
                print(f"    ... dan {len(category_files) - 5} file lainnya")
            file_count += len(category_files)
    
    print("-" * 50)
    print(f"📄 Total file yang akan diatur: {file_count}")

if __name__ == "__main__":
    print("🗂️  FILE ORGANIZER SCRIPT")
    print("=" * 50)
    
    while True:
        print("\nPilih opsi:")
        print("1. 👀 Preview file yang akan dipindahkan")
        print("2. 🚀 Jalankan organizer (pindahkan file)")
        print("3. ❌ Keluar")
        
        choice = input("\nMasukkan pilihan (1-3): ").strip()
        
        if choice == "1":
            preview_organization()
        elif choice == "2":
            organize_downloads_folder()
            break
        elif choice == "3":
            print("👋 Sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")