# 🎨 Custom Branding & Styling Guide

## 📋 Overview

Aplikasi Manajemen Data Mahasiswa v1.1 sekarang mendukung **custom logo dan background** untuk branding yang personal!

---

## 📁 Struktur Folder

```
ProjectRasyid/
├── assets/                    ← Folder untuk semua custom assets
│   ├── logo.png             ← Letakkan file logo di sini
│   ├── background.jpg       ← Letakkan file background di sini
│   └── README.md            ← Panduan assets
├── app.py                    ← Main aplikasi (sudah terintegrate dengan styling)
└── ...
```

---

## 🖼️ File Yang Diperlukan

### 1. **logo.png** (WAJIB UNTUK DISPLAY LOGO)

**Spesifikasi:**
- **Format**: PNG (rekomendasi) atau JPG
- **Ukuran**: 200x200 px hingga 300x300 px (square)
- **Background**: Transparan (opsional) atau solid color
- **File size**: < 500 KB

**Penggunaan:**
- Tampil di atas form login
- Tampil di dashboard (atas tengah)
- Tampil di sidebar (opsional dengan konfigurasi lebih lanjut)

**Tips Desain:**
```
✅ DO:
- Gunakan logo dengan background transparan
- Pilih logo yang simple dan clean
- Ukuran minimal 200x200 px
- Gunakan warna yang kontras dengan background aplikasi

❌ DON'T:
- Logo terlalu rumit atau detailed
- Ukuran terlalu kecil (< 150 px)
- Background yang ramai/kompleks
- Ukuran file terlalu besar (> 1MB)
```

---

### 2. **background.jpg** (OPSIONAL - UNTUK STYLE)

**Spesifikasi:**
- **Format**: JPG atau PNG
- **Ukuran**: Minimal 1920x1080 px (recommended)
- **File size**: < 5 MB (untuk performa optimal)
- **Aspect ratio**: 16:9 atau 4:3

**Penggunaan:**
- Background aplikasi (di belakang konten)
- Hanya terlihat jika opacity/transparency dikonfigurasi

**Tips Desain:**
```
✅ BACKGROUND YANG BAIK:
- Warna soft/pastel yang tidak mengganggu teks
- Gradient smooth (contoh: biru ke ungu)
- Minimalis dengan pattern halus
- Brightness tinggi agar teks tetap readable

CONTOH WARNA GRADIENT:
- Biru ke Ungu: #667eea → #764ba2
- Hijau ke Teal: #11998e → #38ef7d
- Pink ke Orange: #fa709a → #fee140
```

---

## 📥 Cara Menempatkan File

### Step 1: Buat/Siapkan File
```
1. Siapkan logo.png (ukuran 200-300 px)
2. Siapkan background.jpg (ukuran 1920x1080 px)
```

### Step 2: Letakkan di Folder Assets
```
C:\Users\Lenovo\Documents\Joki\ProjectRasyid\
└── assets/
    ├── logo.png          ← Paste di sini
    ├── background.jpg    ← Paste di sini
    └── README.md
```

### Step 3: Restart Aplikasi
```bash
streamlit run app.py
```

---

## 🎨 Styling yang Sudah Diintegrate

Aplikasi sekarang memiliki styling modern dengan:

### ✨ Fitur Styling:

1. **Gradient Background**
   - Warna gradien: Ungu ke Violet (#667eea → #764ba2)
   - Smooth transitions

2. **Sidebar Styling**
   - Background gradient
   - Teks berwarna putih
   - Font weight lebih bold

3. **Button Styling**
   - Gradient background
   - Hover effect (naik 2px)
   - Shadow effect
   - Rounded corners

4. **Input Field**
   - Border ungu (#667eea)
   - Focus state dengan shadow
   - Rounded corners

5. **Card/Box Styling**
   - Success box: Green gradient (#84fab0 → #8fd3f4)
   - Error box: Red gradient (#fa709a → #fee140)
   - Info box: Cyan gradient (#a8edea → #fed6e3)

6. **Text Styling**
   - Header title: Gradient text effect
   - Section title: Bold dengan border bottom
   - Smooth animations

---

## 🔍 Preview Styling

### Color Scheme:
```
Primary Color: #667eea (Biru Ungu)
Secondary Color: #764ba2 (Ungu)
Success Color: #2ecc71 (Hijau)
Error Color: #e74c3c (Merah)
Info Color: #3498db (Biru Cyan)
```

### Font Sizes:
```
Header Title: 2.5em (40px)
Section Title: 1.8em (28px)
Subheader: 1.5em (24px)
Normal Text: 1em (16px)
```

---

## 🎯 Integrasi di App

### Di Mana Logo Ditampilkan:

1. **Login Page**
   ```
   [Logo Image] (150px width)
   ─────────────────
   🎓 Manajemen Data Mahasiswa
   🔐 Sistem Login
   ```

2. **Dashboard**
   ```
   [Logo Image] (120px width)
   ─────────────────
   🎓 MANAJEMEN DATA MAHASISWA
   (Deskripsi aplikasi)
   ```

3. **Sidebar** (opsional dengan custom config)

---

## 📦 Sumber Asset Gratis

Jika Anda tidak memiliki desain sendiri, bisa gunakan:

### **Logo:**
- [Flaticon](https://www.flaticon.com) - Icon & logo gratis
- [LogoMaker](https://www.logomaker.com) - Generator logo
- [Canva](https://www.canva.com) - Design tools online
- [Pixabay](https://pixabay.com) - Gambar gratis

### **Background:**
- [Unsplash](https://unsplash.com) - Foto background gratis
- [Pexels](https://www.pexels.com) - Koleksi gambar terbaik
- [Pixabay](https://pixabay.com) - Ribuan gambar gratis
- [Gradient Mesh](https://www.meshgradient.com) - Generator gradient

### **Design Tools:**
- [Canva](https://www.canva.com) - Drag & drop design
- [Figma](https://www.figma.com) - Professional design
- [GIMP](https://www.gimp.org) - Free Photoshop alternative
- [Photopea](https://www.photopea.com) - Online Photoshop

---

## 🔧 Customization Lanjutan

### Jika Ingin Mengubah Warna Gradient:

Edit `app.py` bagian CSS:
```python
/* Ganti nilai hex color di sini */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

# Contoh gradien lain:
# Hijau: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
# Merah: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
# Orange: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
```

### Jika Ingin Mengubah Ukuran Logo:

Edit di `app.py` bagian `ui_dashboard()`:
```python
st.image(logo_path, use_column_width=True, width=120)
#                                            ^^^^
# Ubah nilai width (120 = ukuran dalam pixel)
```

---

## ⚙️ Troubleshooting

### ❌ Logo tidak tampil?
1. Pastikan file bernama `logo.png` (case-sensitive pada Linux/Mac)
2. Pastikan file ada di folder `assets/`
3. Restart Streamlit: `Ctrl+C` then `streamlit run app.py`

### ❌ Background tidak tampil?
1. Styling gradient akan selalu tampil
2. File `background.jpg` hanya untuk enhancement (opsional)
3. Jika ingin menambah background custom, edit CSS lebih lanjut

### ❌ Kualitas logo jelek?
- Gunakan ukuran minimal 200x200 px
- Export dengan transparent background (PNG)
- Gunakan tools online untuk optimize: [TinyPNG](https://tinypng.com)

### ❌ Aplikasi loading lambat?
- Kurangi ukuran background.jpg (< 2 MB)
- Compress logo.png dengan [TinyPNG](https://tinypng.com)
- Gunakan format JPG untuk background (lebih kecil dari PNG)

---

## 📊 Checklist Sebelum Deploy

- [ ] `logo.png` sudah ada di `assets/`
- [ ] `background.jpg` sudah ada di `assets/` (opsional)
- [ ] Ukuran logo minimal 200x200 px
- [ ] File size < 500 KB untuk logo
- [ ] File size < 5 MB untuk background
- [ ] Streamlit sudah di-restart
- [ ] Logo tampil di login page ✅
- [ ] Logo tampil di dashboard ✅
- [ ] Warna styling sesuai dengan preferensi

---

## 🚀 Deploy ke Streamlit Cloud

Saat deploy ke Streamlit Cloud, pastikan:

1. **Upload folder assets ke GitHub**
   ```bash
   git add assets/
   git commit -m "Add custom logo and background"
   git push origin main
   ```

2. **Streamlit Cloud akan otomatis include assets folder**

3. **Logo akan tampil di Streamlit Cloud deployment**

---

## 📝 File Checklist

Struktur final yang harus ada:
```
✅ C:\Users\Lenovo\Documents\Joki\ProjectRasyid\
   ✅ assets/
      ✅ README.md
      ✅ logo.png (jika ada)
      ✅ background.jpg (jika ada)
   ✅ app.py (sudah update dengan styling)
   ✅ auth_manager.py
   ✅ crud_manager.py
   ✅ mahasiswa.py
   ✅ algoritma_sorting.py
   ✅ algoritma_searching.py
```

---

## 💡 Tips & Tricks

### ✨ Desain Logo yang Baik:
```
1. Gunakan 2-3 warna maksimal
2. Buat logo yang scalable (bagus di ukuran kecil dan besar)
3. Hindari text yang terlalu kecil dalam logo
4. Test di background yang berbeda
```

### 🎨 Kombinasi Warna Populer:
```
1. Biru + Ungu: #667eea + #764ba2 ← DEFAULT
2. Hijau + Teal: #11998e + #38ef7d
3. Pink + Orange: #fa709a + #fee140
4. Merah + Orange: #eb3349 + #f45c43
5. Purple + Magenta: #c471ed + #12c2e9
```

---

## 📞 Support

Jika ada pertanyaan tentang styling:
1. Cek folder `assets/README.md`
2. Baca bagian CSS di `app.py` (lines 28-188)
3. Cek `CUSTOM_BRANDING_GUIDE.md` (file ini)

---

**Last Updated**: December 15, 2025  
**Version**: 1.1.0  
**Status**: ✅ READY FOR CUSTOM ASSETS
