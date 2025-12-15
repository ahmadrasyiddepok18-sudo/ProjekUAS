# Assets Folder

Folder ini berisi semua custom assets untuk aplikasi Manajemen Data Mahasiswa.

## File yang Diperlukan

### 1. **logo.png**
- **Ukuran Rekomendasi**: 200x200 px atau 300x300 px
- **Format**: PNG dengan transparent background (opsional)
- **Tujuan**: Tampil di header aplikasi dan sidebar
- **Resolusi**: Min 150px × 150px (lebih besar lebih baik)

### 2. **background.jpg**
- **Ukuran Rekomendasi**: Minimal 1920x1080 px
- **Format**: JPG atau PNG
- **Tujuan**: Background aplikasi (login page & dashboard)
- **Kualitas**: Pastikan tidak terlalu besar (< 5MB untuk performa optimal)

## Cara Menempatkan File

1. Simpan `logo.png` dan `background.jpg` di folder ini: `assets/`
2. Struktur folder akan menjadi:
   ```
   ProjectRasyid/
   ├── assets/
   │   ├── logo.png              ← Letakkan di sini
   │   ├── background.jpg        ← Letakkan di sini
   │   └── README.md
   ├── app.py
   └── ...
   ```

3. Streamlit akan otomatis membaca file-file tersebut

## Tips Desain

### Logo:
- Gunakan warna yang kontras
- Buat dengan background transparan untuk fleksibilitas
- Hindari teks yang terlalu kecil

### Background:
- Gunakan warna soft/pastel agar tidak menggangu teks
- Hindari gradient yang terlalu kompleks
- Pilih tema yang sesuai dengan warna aplikasi (biru, hijau, atau abu-abu)
- Pastikan brightness sesuai agar teks tetap readable

## Contoh Asset Gratis

Jika tidak punya desain, coba:
- **Logo**: Flaticon, Pixabay, Unsplash
- **Background**: Unsplash, Pexels, Pixels.com

## Format yang Didukung

- Logo: PNG, JPG, SVG (PNG direkomendasikan untuk transparan)
- Background: JPG, PNG

---

**Status**: ⏳ Menunggu file assets dari user
**Update**: File akan otomatis diintegrasikan ke styling app.py
