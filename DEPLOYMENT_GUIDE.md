# 🌐 PANDUAN DEPLOYMENT KE STREAMLIT COMMUNITY CLOUD

Aplikasi Manajemen Data Mahasiswa dapat di-host GRATIS menggunakan Streamlit Community Cloud.
Dokumentasi lengkap cara deployment step-by-step.

---

## 📋 Daftar Isi
1. [Prerequisites](#prerequisites)
2. [Step 1: Setup GitHub](#step-1-setup-github)
3. [Step 2: Upload Kode ke GitHub](#step-2-upload-kode-ke-github)
4. [Step 3: Deploy ke Streamlit Cloud](#step-3-deploy-ke-streamlit-cloud)
5. [Step 4: Konfigurasi & Maintenance](#step-4-konfigurasi--maintenance)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Sebelum memulai, pastikan Anda sudah memiliki:

### ✅ Software yang Diperlukan:
- [Git](https://git-scm.com/download/win) - Version control
- [GitHub Account](https://github.com/signup) - Repository hosting (gratis)
- Python 3.10+ (sudah ada)

### ✅ Project Files:
- Semua file aplikasi (`app.py`, `mahasiswa.py`, dll)
- `requirements.txt` - File dependencies
- `.gitignore` - File untuk exclude

---

## Step 1: Setup GitHub

### 1a. Buat GitHub Account (Jika belum punya)
1. Buka https://github.com
2. Klik "Sign up"
3. Isi form registrasi
4. Verify email Anda
5. Selesai ✅

### 1b. Buat Repository Baru
1. Login ke GitHub
2. Klik "+" di atas (top right)
3. Pilih "New repository"
4. **Repository name**: `ProjectRasyid` (atau nama favorit)
5. **Description**: "Aplikasi Manajemen Data Mahasiswa dengan Streamlit"
6. **Visibility**: Public (agar bisa deploy ke Streamlit Cloud)
7. ❌ Jangan centang "Initialize this repository with a README"
8. Klik "Create repository"

### Catatan:
Setelah create, GitHub akan menunjukkan instruksi. Ikuti langkah berikutnya.

---

## Step 2: Upload Kode ke GitHub

### 2a. Setup Git di Local Computer

Buka PowerShell/Command Prompt di folder project:

```powershell
cd C:\Users\Lenovo\Documents\Joki\ProjectRasyid
```

### 2b. Inisialisasi Git Repository

```powershell
# Inisialisasi git
git init

# Tambahkan semua file
git add .

# Buat commit pertama
git commit -m "Initial commit: Aplikasi Manajemen Mahasiswa v1.0"
```

### 2c. Setup GitHub Credentials

**Opsi A: GitHub Personal Access Token (Recommended)**

1. Buka https://github.com/settings/tokens
2. Klik "Generate new token" → "Generate new token (classic)"
3. Name: `projectrasyid-token`
4. Scope: Centang `repo` (full control of private repositories)
5. Expiration: 90 days (or more)
6. Klik "Generate token"
7. **COPY TOKEN** (sekali hilang tidak bisa lihat lagi!)

Store token di tempat aman (notepad sementara).

**Opsi B: SSH Key (Advanced)**

Jika ingin menggunakan SSH (lebih aman):
- Ikuti: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### 2d. Connect Repository ke GitHub

Ganti `YOUR_USERNAME` dan `YOUR_TOKEN` di command berikut:

```powershell
# Add remote repository
git remote add origin https://YOUR_USERNAME:YOUR_TOKEN@github.com/YOUR_USERNAME/ProjectRasyid.git

# Verify remote
git remote -v
# Output harus:
# origin  https://YOUR_USERNAME:***@github.com/YOUR_USERNAME/ProjectRasyid.git (fetch)
# origin  https://YOUR_USERNAME:***@github.com/YOUR_USERNAME/ProjectRasyid.git (push)
```

### 2e. Push Kode ke GitHub

```powershell
# Rename branch ke main (jika perlu)
git branch -M main

# Push ke GitHub
git push -u origin main

# Verifikasi: Buka https://github.com/YOUR_USERNAME/ProjectRasyid
# Semua file harus sudah ada di GitHub!
```

**Expected Output:**
```
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
...
To https://github.com/YOUR_USERNAME/ProjectRasyid.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

---

## Step 3: Deploy ke Streamlit Cloud

### 3a. Login ke Streamlit Cloud

1. Buka https://share.streamlit.io
2. Klik "Sign in with GitHub"
3. Authorize Streamlit dan login

### 3b. Deploy Aplikasi

1. Setelah login, klik "**Create app**"
2. Form akan muncul:
   - **GitHub repo owner**: Pilih username Anda
   - **Repository**: Pilih `ProjectRasyid`
   - **Branch**: Pilih `main`
   - **Main file path**: `app.py`
3. Klik "**Deploy**"

Tunggu 2-5 menit untuk proses deployment...

### 3c. Verifikasi Deployment

1. Setelah selesai, URL aplikasi akan muncul
2. Format: `https://your-username-projectrasyid-app-xxxxx.streamlit.app`
3. Klik URL untuk membuka aplikasi
4. Testing semua fitur untuk memastikan berfungsi ✅

### 3d. Share Aplikasi

**Bagikan URL ke teman:**
```
https://your-username-projectrasyid-app-xxxxx.streamlit.app
```

Mereka bisa mengakses tanpa perlu install apapun!

---

## Step 4: Konfigurasi & Maintenance

### 4a. Update Kode (Auto-Deploy)

Setiap kali Anda update kode dan push ke GitHub, aplikasi akan otomatis ter-update:

```powershell
# Edit file (misal: app.py)
# ... edit ...

# Add dan commit changes
git add .
git commit -m "Fix: Perbaikan halaman statistik"

# Push ke GitHub
git push origin main

# Tunggu 1-2 menit, aplikasi akan auto-redeploy!
```

### 4b. Monitoring & Logs

Di Streamlit Cloud Dashboard:
1. Buka https://share.streamlit.io
2. Klik aplikasi Anda
3. Lihat "Logs" untuk debugging
4. Lihat "Settings" untuk konfigurasi

### 4c. Custom Domain (Optional - Paid)

Jika ingin domain custom (misal: `mahasiswa.mycompany.com`):
- Streamlit Pro/Business diperlukan
- Basic version sudah gratis dengan domain auto-generated

---

## Troubleshooting

### ❌ Error: "Module not found"

**Penyebab**: Dependencies tidak terinstall

**Solusi**:
1. Verifikasi `requirements.txt` ada di root folder
2. Pastikan berisi:
   ```
   streamlit==1.37.0
   pandas==2.1.3
   ```
3. Push ulang ke GitHub

### ❌ Error: "ModuleNotFoundError: No module named 'mahasiswa'"

**Penyebab**: File `mahasiswa.py` tidak di-push

**Solusi**:
```powershell
# Verifikasi file ada
dir

# Pastikan git track semua file
git add .
git status

# Semua file harus ada di "Changes to be committed"
git commit -m "Fix: Add missing modules"
git push origin main
```

### ❌ Error: "RuntimeError: Streamlit requires raw Python objects, not requests objects"

**Penyebab**: Cache issue

**Solusi**:
1. Di Streamlit Cloud dashboard, klik ⋮ (menu) → "Reboot app"
2. Atau clear browser cache

### ❌ Data tidak tersimpan antar session

**Penyebab**: Streamlit Cloud reset setiap session baru

**Solusi sementara**: Normal behavior (data JSON bersifat ephemeral)

**Solusi permanen** (Future): Setup database (Firebase, Supabase, PostgreSQL)
- Memerlukan setup credentials di `.streamlit/secrets.toml`

### ❌ Repository visibility error

**Error**: "Private repositories not supported"

**Solusi**: Repository HARUS public
1. Settings → General → Change repository visibility → Public

---

## 🎯 Checklist Deployment

Sebelum deploy, pastikan:

- [ ] Semua file Python ada dan tidak error
- [ ] `requirements.txt` sudah update
- [ ] `.gitignore` sudah ada
- [ ] GitHub account sudah siap
- [ ] Repository sudah public
- [ ] Semua file sudah push ke GitHub
- [ ] Streamlit account sudah login
- [ ] `app.py` sudah di-set sebagai main file
- [ ] Aplikasi bisa dibuka di Streamlit Cloud
- [ ] Semua fitur sudah testing di local

---

## 📊 Performance & Monitoring

### Best Practices:
1. **Keep requirements.txt minimal** - Hanya package yang diperlukan
2. **Use @st.cache_data untuk cache** - Jika data tidak sering berubah
3. **Monitor resource usage** - Streamlit Cloud limited resource
4. **Regular backup** - Push kode ke GitHub regularly

### Streamlit Cloud Resources:
- RAM: ~1GB per app
- CPU: Shared
- Storage: Ephemeral (data lost on reboot)
- Execution: Timeout ~30 menit

---

## 🔐 Security Best Practices

### ✅ Do's:
- [ ] Use GitHub Personal Access Token (jangan share)
- [ ] Keep secrets di `.streamlit/secrets.toml` (not in git)
- [ ] Regular update dependencies
- [ ] Monitor logs untuk suspicious activity

### ❌ Don'ts:
- ❌ Commit credentials/passwords ke GitHub
- ❌ Use public WiFi untuk git operations
- ❌ Share Personal Access Token
- ❌ Keep old/unused branches

---

## 📞 Support & Resources

### Dokumentasi Resmi:
- [Streamlit Docs](https://docs.streamlit.io)
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-cloud)
- [GitHub Docs](https://docs.github.com)

### Community:
- [Streamlit Forum](https://discuss.streamlit.io)
- [GitHub Discussions](https://github.com/discussions)

### YouTube Tutorials:
- "Deploy Streamlit to Streamlit Cloud" - Official
- "GitHub basics" - Official GitHub

---

## ✅ Final Checklist

Setelah deployment selesai:

- [ ] Aplikasi bisa diakses di public URL
- [ ] Semua menu berfungsi (Dashboard, CRUD, Sorting, Searching, Statistik)
- [ ] Data bisa ditambah, diedit, dihapus
- [ ] Searching dan sorting bekerja
- [ ] Responsive design di mobile/tablet
- [ ] URL sudah dibagikan ke pengguna

---

## 🎉 Selesai!

Aplikasi Anda sekarang sudah **LIVE** di internet dan bisa diakses publik!

**Bagikan URL ini:**
```
https://your-username-projectrasyid-app-xxxxx.streamlit.app
```

---

**Happy Deploying!** 🚀
