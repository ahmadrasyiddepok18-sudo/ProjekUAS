# Manajemen Data Mahasiswa - Aplikasi Streamlit

Aplikasi web sederhana untuk mengelola data mahasiswa dengan berbagai fitur canggih termasuk CRUD operations, sorting algorithms, searching algorithms, dan analisis statistik.

## 📋 Struktur Proyek

```
ProjectRasyid/
├── app.py                      # Aplikasi Streamlit utama
├── mahasiswa.py               # Class OOP (Mahasiswa, MahasiswaBaru, MahasiswaLama)
├── algoritma_sorting.py       # Algoritma Sorting (Bubble, Merge, Shell Sort)
├── algoritma_searching.py     # Algoritma Searching (Linear, Binary Search)
├── crud_manager.py            # CRUD Operations & File Management
├── requirements.txt           # Dependencies
├── data_mahasiswa.json        # Data storage (auto-created)
└── README.md                  # Dokumentasi
```

## 🎯 Fitur Utama

### 1. CRUD Operations
- **Create**: Tambah mahasiswa baru dengan validasi Regex
- **Read**: Lihat semua data atau cari spesifik
- **Update**: Edit data mahasiswa berdasarkan NIM
- **Delete**: Hapus mahasiswa dari sistem

### 2. OOP Architecture
- **Encapsulation**: Atribut privat (`__nama`, `__nim`, dll) dengan @property
- **Inheritance**: Class `MahasiswaBaru` dan `MahasiswaLama` mewarisi `Mahasiswa`
- **Polymorphism**: Override `__str__()` dan `info()` di subclass
- **Object References**: Python menggunakan reference (bukan pointer C++)

### 3. Algoritma Sorting (3 Metode)

#### Bubble Sort
- **Time Complexity**: O(n²) worst/average, O(n) best
- **Space Complexity**: O(1)
- **Tipe**: Comparison-based, in-place
- Cocok untuk: Data kecil atau demonstrasi

#### Merge Sort
- **Time Complexity**: O(n log n) untuk semua case
- **Space Complexity**: O(n)
- **Tipe**: Divide & Conquer, Stable
- Cocok untuk: Data besar, performa konsisten

#### Shell Sort
- **Time Complexity**: O(n^1.3) average, O(n²) worst
- **Space Complexity**: O(1)
- **Tipe**: Insertion Sort variant, in-place
- Cocok untuk: Data sedang, balance antara Bubble dan Merge

### 4. Algoritma Searching (2 Metode)

#### Linear Search
- **Time Complexity**: O(1) best, O(n) average/worst
- **Space Complexity**: O(1)
- **Requirement**: Data bisa terurut atau tidak
- Cocok untuk: Data kecil, data tidak terurut

#### Binary Search
- **Time Complexity**: O(1) best, O(log n) average/worst
- **Space Complexity**: O(1)
- **Requirement**: Data HARUS TERURUT
- Cocok untuk: Data besar dan terurut

### 5. Data Validation
- **Email**: Format `user@domain.com` (Regex validation)
- **NIM**: Format angka 8-12 digit (Regex validation)
- **Nama**: Minimal 3 karakter
- **Error Handling**: Try-Except untuk File I/O

### 6. Penyimpanan Data
- **Format**: JSON (human-readable)
- **Lokasi**: `data_mahasiswa.json` (auto-created)
- **Enkapsulasi**: Semua file I/O di `CRUDManager`

## 🚀 Cara Menjalankan

### Prerequisites
- Python 3.10+
- pip (Python package manager)

### Instalasi

1. **Clone atau Download Project**
   ```bash
   cd C:\Users\Lenovo\Documents\Joki\ProjectRasyid
   ```

2. **Buat Virtual Environment (Optional tapi Recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # atau
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Menjalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser default di `http://localhost:8501`

## 📖 Panduan Penggunaan

### Dashboard
- Ringkasan statistik aplikasi
- Metric utama (Total Mahasiswa, Jurusan, IPK, Status)

### Tambah Mahasiswa
1. Isi form dengan data mahasiswa
2. Pilih kategori (umum/baru/lama)
3. Untuk kategori "lama", masukkan IPK
4. Klik "Tambah Mahasiswa"

**Validasi otomatis:**
- Email harus format valid
- NIM harus angka 8-12 digit
- Nama minimal 3 karakter
- NIM tidak boleh duplikat

### Lihat Data Mahasiswa
- Tampilkan semua mahasiswa dalam format tabel
- Filter berdasarkan jurusan dan status
- Eksport data jika diperlukan

### Edit Mahasiswa
1. Pilih mahasiswa dari dropdown (berdasarkan NIM)
2. Edit field yang diinginkan
3. Klik "Simpan Perubahan"

### Hapus Mahasiswa
⚠️ **Hati-hati**: Tindakan tidak dapat dibatalkan
1. Pilih mahasiswa yang ingin dihapus
2. Klik "Hapus Mahasiswa"

### Cari Mahasiswa
1. Pilih metode: Linear Search atau Binary Search
2. Pilih field pencarian (nama, NIM, jurusan, email)
3. Masukkan nilai pencarian
4. Sistem akan menampilkan analisis Big O Notation

**Catatan Binary Search:**
- Data akan di-sort otomatis sebelum pencarian
- Lebih cepat untuk data besar

### Sorting Data
1. Pilih algoritma (Bubble/Merge/Shell Sort)
2. Pilih field untuk sorting (nama, NIM, jurusan, email)
3. Pilih urutan (ascending/descending)
4. Sistem akan menampilkan:
   - Jumlah perbandingan
   - Big O Notation lengkap
   - Hasil sorting dalam tabel

### Statistik
- Total mahasiswa
- Distribusi per jurusan (tabel + chart)
- Distribusi per status (tabel + chart)
- Rata-rata IPK

## 🏗️ Penjelasan Arsitektur OOP

### Encapsulation (Enkapsulasi)
```python
class Mahasiswa:
    def __init__(self, nama, nim, jurusan, email):
        # Atribut privat dengan __ (name mangling)
        self.__nama = nama
        self.__nim = nim
        # ... dll
    
    # Akses via property (getter)
    @property
    def nama(self):
        return self.__nama
    
    # Modifikasi via setter
    @nama.setter
    def nama(self, value):
        if len(value) >= 3:
            self.__nama = value
```

### Inheritance (Pewarisan)
```python
# Parent class
class Mahasiswa:
    def __init__(self, nama, nim, jurusan, email):
        self.__nama = nama
        # ... dll

# Child class mewarisi parent
class MahasiswaBaru(Mahasiswa):
    def __init__(self, nama, nim, jurusan, email, program_orientasi=True):
        super().__init__(nama, nim, jurusan, email)  # Call parent init
        self.program_orientasi = program_orientasi
```

### Polymorphism (Polimorfisme)
```python
class Mahasiswa:
    def info(self):  # Parent implementation
        return {...}

class MahasiswaBaru(Mahasiswa):
    def info(self):  # Override (Polymorphism)
        info_parent = super().info()
        info_parent["program_orientasi"] = self.program_orientasi
        return info_parent
```

### Object References vs Pointers (C++)
**Python:**
```python
# Python menggunakan REFERENCES (referensi aman)
mahasiswa = Mahasiswa("Budi", "12345678", "IF", "budi@domain.com")
# 'mahasiswa' adalah referensi ke object di memory
# Tidak bisa arithmetic: mahasiswa++ (TIDAK VALID)
# Python auto garbage collect jika tidak ada referensi lagi
```

**C++ (untuk perbandingan):**
```cpp
// C++ menggunakan POINTERS (pointer arithmetic)
Mahasiswa* mahasiswa = new Mahasiswa(...);
// mahasiswa adalah alamat memory yang bisa di-increment: mahasiswa++
// Manual delete diperlukan: delete mahasiswa;
```

**Perbedaan Key:**
| Aspek | Python Reference | C++ Pointer |
|-------|------------------|------------|
| Arithmetic | ❌ Tidak ada | ✅ Ada |
| Memory Management | Auto (GC) | Manual |
| Null Safety | Relative safe | Perlu hati-hati |
| Syntax | `mahasiswa.method()` | `mahasiswa->method()` |

## 💾 Format JSON Data

```json
[
  {
    "nama": "Budi Santoso",
    "nim": "12345678",
    "jurusan": "Teknik Informatika",
    "email": "budi@domain.com",
    "tahun_masuk": 2023,
    "status": "aktif",
    "tanggal_dibuat": "2025-12-15 10:30:45",
    "kategori": "umum"
  },
  {
    "nama": "Ani Wijaya",
    "nim": "87654321",
    "jurusan": "Teknik Elektro",
    "email": "ani@domain.com",
    "tahun_masuk": 2022,
    "status": "aktif",
    "tanggal_dibuat": "2025-12-15 10:35:20",
    "kategori": "lama",
    "ipk": 3.75,
    "keterangan_ipk": "Cumlaude"
  }
]
```

## 📚 Big O Notation Summary

### Sorting Algorithms
| Algoritma | Best Case | Average | Worst Case | Space | Stable |
|-----------|-----------|---------|-----------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| Shell | O(n log n) | O(n^1.3) | O(n²) | O(1) | ❌ |

### Searching Algorithms
| Algoritma | Best Case | Average | Worst Case | Space | Requirement |
|-----------|-----------|---------|-----------|-------|-------------|
| Linear | O(1) | O(n) | O(n) | O(1) | Sembarang |
| Binary | O(1) | O(log n) | O(log n) | O(1) | Sorted |

## 🌐 Deploy ke Streamlit Community Cloud (GRATIS)

### Langkah-langkah Deployment:

#### 1. Push Code ke GitHub
```bash
# Inisialisasi git (jika belum ada)
git init
git add .
git commit -m "Initial commit: Aplikasi Manajemen Mahasiswa"

# Buat repository di GitHub (https://github.com)
# Push ke GitHub
git remote add origin https://github.com/username/ProjectRasyid.git
git branch -M main
git push -u origin main
```

#### 2. Deploy ke Streamlit Cloud
1. Buka https://share.streamlit.io
2. Klik "New app"
3. Login dengan GitHub account
4. Pilih repository `ProjectRasyid`
5. Pilih branch `main`
6. Pilih app path: `app.py`
7. Klik "Deploy"

#### 3. Configuration
- Streamlit Cloud akan otomatis membaca `requirements.txt`
- App akan deploy di URL: `https://username-projectrasyid-app-xxxxxx.streamlit.app`
- URL akan tersedia untuk dibagikan ke publik

#### 4. Tips Maintenance
- Setiap push ke GitHub akan auto-redeploy
- `data_mahasiswa.json` disimpan di setiap instance (persisten)
- Untuk shared database, gunakan Streamlit secrets + database (future enhancement)

#### Contoh GitHub Actions untuk Auto-Deploy (Optional):
```yaml
# .github/workflows/deploy.yml
name: Deploy to Streamlit Cloud
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Streamlit Cloud
        run: |
          streamlit run app.py --deploy
```

### Akses Aplikasi
Setelah deployment, aplikasi bisa diakses publik di:
```
https://username-projectrasyid-app-xxxxx.streamlit.app
```

Bagikan URL ini ke siapa saja untuk mengakses aplikasi tanpa perlu install apapun!

## 🔧 Troubleshooting

### Error: Module not found
```bash
# Pastikan requirements.txt terinstall
pip install -r requirements.txt
```

### Error: Port 8501 already in use
```bash
# Gunakan port berbeda
streamlit run app.py --server.port 8502
```

### Error: JSON file corrupt
- Delete `data_mahasiswa.json`
- Jalankan ulang aplikasi, file akan di-recreate

### Data tidak tersimpan
- Pastikan folder memiliki write permission
- Cek di file explorer apakah `data_mahasiswa.json` ada

## 📝 Developer & Author

**Nama**: Ahmad Rasyid  
**Program**: Teknik Informatika  
**Tugas**: Final Project - Pemrograman Lanjut  
**Tanggal**: December 2025

Aplikasi ini mendemonstrasikan kemampuan dalam:
- Object-Oriented Programming (OOP)
- Data Structures & Algorithms
- Web Development dengan Streamlit
- Database & File Management
- Software Engineering best practices

## 🎓 Learning Outcomes
Setelah mempelajari dan menggunakan aplikasi ini, Anda akan memahami:
1. ✅ OOP Architecture (Encapsulation, Inheritance, Polymorphism)
2. ✅ CRUD Operations dengan File I/O
3. ✅ Algoritma Sorting dan Time Complexity Analysis
4. ✅ Algoritma Searching dan Optimasi
5. ✅ Data Validation dengan Regex
6. ✅ Error Handling best practices
7. ✅ Web Development dengan Streamlit
8. ✅ JSON Data Format
9. ✅ Python References vs C++ Pointers
10. ✅ Web Deployment (Streamlit Cloud)

---

**Happy Learning & Coding!** 🚀
