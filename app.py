"""
Aplikasi Web Manajemen Data Mahasiswa menggunakan Streamlit.

Fitur:
- CRUD operations (Create, Read, Update, Delete)
- Multiple sorting algorithms (Bubble Sort, Merge Sort, Shell Sort)
- Multiple searching algorithms (Linear Search, Binary Search)
- Data validation dengan Regex
- File I/O dengan JSON
- OOP Architecture dengan Inheritance dan Polymorphism
- Visualisasi statistik

Author: Senior Python Developer
Tech Stack: Python 3.10+, Streamlit, Pandas, JSON
Date: 2025-12-15
"""

import streamlit as st
import pandas as pd
from typing import List, Dict
from crud_manager import CRUDManager
from algoritma_sorting import AlgoritmaSorting
from algoritma_searching import AlgoritmaSearching
from auth_manager import AuthManager


# ========== KONFIGURASI STREAMLIT ==========

def configure_streamlit():
    """Konfigurasi awal untuk Streamlit."""
    st.set_page_config(
        page_title="Manajemen Mahasiswa",
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Load background image jika ada dan convert ke base64
    import os
    import base64
    
    bg_image_path = "assets/background.jpg"
    bg_css = ""
    
    if os.path.exists(bg_image_path):
        try:
            with open(bg_image_path, "rb") as img_file:
                img_data = base64.b64encode(img_file.read()).decode()
                bg_css = f"""
                [data-testid="stAppViewContainer"] {{
                    background-image: 
                        linear-gradient(rgba(255, 255, 255, 0.98), rgba(255, 255, 255, 0.65)),
                        url('data:image/jpeg;base64,{img_data}');
                    background-size: cover;
                    background-position: center;
                    background-attachment: fixed;
                }}
                """
        except Exception as e:
            print(f"Warning: Could not load background image: {e}")
            bg_css = ""
    
    # Custom CSS dengan Background dan Logo - Warna Soft/Pastel
    st.markdown(f"""
        <style>
        /* ===== BACKGROUND STYLING ===== */
        .stApp {{
            background: linear-gradient(135deg, #E8EEF7 0%, #F0E8F5 100%);
            background-attachment: fixed;
        }}
        
        {bg_css}
        
        /* ===== LOGO STYLING ===== */
        .logo-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 auto 20px auto;
            padding: 15px;
            background: linear-gradient(135deg, #D8E5F2 0%, #E8D8F0 100%);
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
            width: 100%;
        }}
        
        .logo-container img {{
            max-width: 150px;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
            margin: 0 auto;
            display: block;
        }}
        
        /* Center Streamlit image */
        [data-testid="stImage"] {{
            display: flex !important;
            justify-content: center !important;
        }}
        
        /* ===== SIDEBAR STYLING ===== */
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, #D8E5F2 0%, #E8D8F0 100%);
        }}
        
        [data-testid="stSidebar"] h3, 
        [data-testid="stSidebar"] h4,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label {{
            color: #4A5568;
            font-weight: 500;
        }}
        
        [data-testid="stSidebar"] .stRadio > label,
        [data-testid="stSidebar"] .stSelectbox > label {{
            color: #4A5568;
            font-weight: 600;
        }}
        
        /* ===== CARD STYLING ===== */
        .header-title {{
            font-size: 2.5em;
            font-weight: bold;
            color: white;
            text-align: center;
            margin-bottom: 20px;
            background: linear-gradient(135deg, #8B9DC3 0%, #9B8DBB 100%);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(139, 157, 195, 0.3);
        }}
        
        .success-box {{
            background: linear-gradient(135deg, #D4F1E8 0%, #D8E8F5 100%);
            border: 2px solid #7BC8A4;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
        }}
        
        .error-box {{
            background: linear-gradient(135deg, #F5D4D8 0%, #F5E8D4 100%);
            border: 2px solid #D4939F;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
        }}
        
        .info-box {{
            background: linear-gradient(135deg, #D4EEF5 0%, #E8D4F5 100%);
            border: 2px solid #8CB8D4;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
        }}
        
        .section-title {{
            font-size: 1.8em;
            font-weight: bold;
            color: #5B6B8A;
            border-bottom: 3px solid #8B9DC3;
            padding-bottom: 10px;
            margin-top: 20px;
        }}
        
        /* ===== BUTTON STYLING ===== */
        .stButton > button {{
            background: linear-gradient(135deg, #8B9DC3 0%, #9B8DBB 100%);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(139, 157, 195, 0.2);
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(139, 157, 195, 0.3);
        }}
        
        /* ===== INPUT STYLING ===== */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > select {{
            border: 2px solid #8B9DC3;
            border-radius: 8px;
            padding: 10px;
        }}
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {{
            border-color: #9B8DBB;
            box-shadow: 0 0 10px rgba(155, 141, 187, 0.2);
        }}
        
        /* ===== DATAFRAME STYLING ===== */
        .stDataFrame {{
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
        }}
        
        /* ===== DIVIDER ===== */
        hr {{
            border: none;
            height: 2px;
            background: linear-gradient(90deg, transparent, #8B9DC3, transparent);
            margin: 20px 0;
        }}
        </style>
    """, unsafe_allow_html=True)


# ========== INISIALISASI SESSION STATE ==========

def init_session_state():
    """Inisialisasi session state untuk Streamlit."""
    if 'crud_manager' not in st.session_state:
        st.session_state.crud_manager = CRUDManager()
    
    if 'last_action' not in st.session_state:
        st.session_state.last_action = None
    
    if 'auth_manager' not in st.session_state:
        st.session_state.auth_manager = AuthManager()
    
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None


# ========== LOGIN & AUTHENTICATION UI ==========

def ui_login_page():
    """UI untuk halaman login."""
    import os
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Display logo jika ada - dengan centering column
        logo_path = "assets/logo.png"
        if os.path.exists(logo_path):
            col_l, col_logo, col_r = st.columns([0.2, 0.6, 0.2])
            with col_logo:
                st.image(logo_path, width=150)
        
        st.markdown('<div class="header-title">🎓 Manajemen Data Mahasiswa</div>', 
                    unsafe_allow_html=True)
        
        st.markdown('<div class="header-title" style="font-size: 1.5em; margin-top: -10px;">🔐 Sistem Login</div>', 
                    unsafe_allow_html=True)
        
        st.divider()
        
        # Tab untuk Login & Register
        tab1, tab2 = st.tabs(["🔓 Login", "📝 Register"])
        
        with tab1:
            st.subheader("Masuk ke Akun")
            
            username = st.text_input("Username", placeholder="Contoh: admin atau user")
            password = st.text_input("Password", type="password", placeholder="Password Anda")
            
            if st.button("🔓 Login", use_container_width=True, type="primary"):
                if not username or not password:
                    st.error("❌ Username dan password harus diisi!")
                else:
                    auth = st.session_state.auth_manager
                    success, message, user_info = auth.login(username, password)
                    
                    if success:
                        st.session_state.logged_in = True
                        st.session_state.current_user = user_info
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
            
            st.divider()
            st.info("""
            **Demo Credentials:**
            - Username: `admin` | Password: `admin123`
            - Username: `user` | Password: `user123`
            """)
        
        with tab2:
            st.subheader("Buat Akun Baru")
            
            new_username = st.text_input("Username", key="reg_username")
            new_password = st.text_input("Password", type="password", key="reg_password")
            new_password_confirm = st.text_input("Konfirmasi Password", type="password", key="reg_confirm")
            new_nama = st.text_input("Nama Lengkap", key="reg_nama")
            new_email = st.text_input("Email", key="reg_email")
            
            if st.button("📝 Daftar", use_container_width=True, type="secondary"):
                if not all([new_username, new_password, new_password_confirm, new_nama, new_email]):
                    st.error("❌ Semua field harus diisi!")
                elif new_password != new_password_confirm:
                    st.error("❌ Password tidak cocok!")
                else:
                    auth = st.session_state.auth_manager
                    success, message = auth.register(
                        username=new_username,
                        password=new_password,
                        nama_lengkap=new_nama,
                        email=new_email
                    )
                    
                    if success:
                        st.success(message)
                        st.info("✅ Akun berhasil dibuat! Silahkan login dengan username dan password Anda.")
                    else:
                        st.error(message)


def ui_user_profile():
    """Tampilkan profil user di sidebar."""
    with st.sidebar:
        user = st.session_state.current_user
        st.markdown("---")
        st.markdown(f"### 👤 {user['nama_lengkap']}")
        st.caption(f"@{user['username']} | Role: {user['role'].upper()}")
        
        # Menu user
        user_menu = st.selectbox(
            "User Menu:",
            ["Dashboard", "Profil", "Ubah Password", "Logout"],
            key="user_menu"
        )
        
        return user_menu


def ui_profile_page():
    """UI untuk halaman profil user."""
    st.markdown('<div class="section-title">👤 PROFIL PENGGUNA</div>', 
                unsafe_allow_html=True)
    
    user = st.session_state.current_user
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**Username:** {user['username']}")
        st.markdown(f"**Nama Lengkap:** {user['nama_lengkap']}")
    
    with col2:
        st.markdown(f"**Email:** {user['email']}")
        st.markdown(f"**Role:** {user['role'].upper()}")


def ui_change_password():
    """UI untuk mengubah password."""
    st.markdown('<div class="section-title">🔐 UBAH PASSWORD</div>', 
                unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        old_password = st.text_input("Password Lama", type="password")
        new_password = st.text_input("Password Baru", type="password")
        confirm_password = st.text_input("Konfirmasi Password Baru", type="password")
        
        if st.button("💾 Ubah Password", type="primary", use_container_width=True):
            if not all([old_password, new_password, confirm_password]):
                st.error("❌ Semua field harus diisi!")
            elif new_password != confirm_password:
                st.error("❌ Password baru tidak cocok!")
            else:
                auth = st.session_state.auth_manager
                success, message = auth.change_password(
                    st.session_state.current_user['username'],
                    old_password,
                    new_password
                )
                
                if success:
                    st.success(message)
                else:
                    st.error(message)
    
    with col2:
        st.info("""
        **Panduan Keamanan:**
        - Password minimal 6 karakter
        - Gunakan kombinasi huruf dan angka
        - Jangan bagikan password Anda
        - Logout setelah selesai
        """)


# ========== UI COMPONENTS ==========

def ui_sidebar_menu():
    """Render sidebar dengan menu navigasi."""
    with st.sidebar:
        st.markdown("### 📚 MENU NAVIGASI")
        st.divider()
        
        # User profile section
        user = st.session_state.current_user
        st.markdown(f"### 👤 {user['nama_lengkap']}")
        st.caption(f"@{user['username']} | {user['role'].upper()}")
        
        st.divider()
        
        # User menu (prioritas tinggi)
        user_menu = st.selectbox(
            "⚙️ Pengaturan Akun:",
            ["Pilih...", "Lihat Profil", "Ubah Password", "Logout"],
            key="user_menu"
        )
        
        if user_menu == "Lihat Profil":
            return "profil"
        elif user_menu == "Ubah Password":
            return "ubah_password"
        elif user_menu == "Logout":
            st.session_state.logged_in = False
            st.session_state.current_user = None
            st.rerun()
        
        st.divider()
        
        # Main menu
        menu = st.radio(
            "Pilih Menu:",
            options=[
                "🏠 Dashboard",
                "➕ Tambah Mahasiswa",
                "📋 Lihat Data Mahasiswa",
                "✏️ Edit Mahasiswa",
                "🗑️ Hapus Mahasiswa",
                "🔍 Cari Mahasiswa",
                "📊 Sorting Data",
                "📈 Statistik"
            ],
            index=0
        )
        
        return menu
        st.info(
            "**Manajemen Data Mahasiswa v1.0**\n\n"
            "Aplikasi ini menggunakan:\n"
            "- OOP Architecture (Class, Inheritance, Polymorphism)\n"
            "- CRUD Operations\n"
            "- Multiple Sorting Algorithms\n"
            "- Multiple Searching Algorithms\n"
            "- Authentication & Login\n"
            "- JSON File Storage"
        )
        
        return menu


def ui_dashboard():
    """Dashboard utama aplikasi."""
    import os
    
    # Display logo di dashboard
    col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
    with col2:
        logo_path = "assets/logo.png"
        if os.path.exists(logo_path):
            st.image(logo_path, width=120)
    
    st.markdown('<div class="header-title">🎓 MANAJEMEN DATA MAHASISWA</div>', 
                unsafe_allow_html=True)
    
    st.markdown("""
    Aplikasi Manajemen Data Mahasiswa adalah sistem informasi terintegrasi yang dirancang
    untuk mengelola data mahasiswa dengan fitur lengkap mencakup:
    
    ### ✨ Fitur Utama:
    1. **CRUD Operations** - Tambah, Lihat, Edit, Hapus data mahasiswa
    2. **Sorting Algorithms** - Urutkan data dengan berbagai algoritma
    3. **Searching Algorithms** - Cari data dengan Linear & Binary Search
    4. **Data Validation** - Validasi dengan Regex untuk Email dan NIM
    5. **Statistik** - Analisis data mahasiswa per jurusan dan status
    
    ### 🏗️ Arsitektur OOP:
    - **Encapsulation**: Atribut privat dengan @property
    - **Inheritance**: Class MahasiswaBaru dan MahasiswaLama mewarisi Mahasiswa
    - **Polymorphism**: Override __str__ dan info() method
    
    ### 💾 Data Storage:
    Data disimpan dalam format JSON untuk kemudahan pembacaan dan editing manual.
    """)
    
    st.divider()
    
    # Tampilkan statistik singkat
    crud = st.session_state.crud_manager
    data = crud.read_all_mahasiswa()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Mahasiswa", len(data))
    
    with col2:
        statik = crud.get_statistik()
        jumlah_jurusan = len(statik.get("total_per_jurusan", {}))
        st.metric("Jurusan", jumlah_jurusan)
    
    with col3:
        st.metric("Rata-rata IPK", f"{statik.get('rata_ipk', 0.0):.2f}")
    
    with col4:
        jumlah_aktif = statik.get("total_per_status", {}).get("aktif", 0)
        st.metric("Mahasiswa Aktif", jumlah_aktif)


def ui_tambah_mahasiswa():
    """UI untuk menambah mahasiswa baru."""
    st.markdown('<div class="section-title">➕ TAMBAH MAHASISWA BARU</div>', 
                unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        nama = st.text_input("Nama Lengkap", placeholder="Contoh: Budi Santoso")
        nim = st.text_input("NIM (Nomor Induk Mahasiswa)", placeholder="Contoh: 12345678")
        jurusan = st.selectbox(
            "Jurusan/Program Studi",
            options=[
                "Teknik Informatika",
                "Teknik Elektro",
                "Teknik Sipil",
                "Teknik Mesin",
                "Akuntansi",
                "Manajemen",
                "Sistem Informasi",
                "Lainnya"
            ]
        )
    
    with col2:
        email = st.text_input("Email", placeholder="Contoh: budi@domain.com")
        tahun_masuk = st.number_input("Tahun Masuk", min_value=1990, max_value=2025, value=2023)
        kategori = st.selectbox(
            "Kategori Mahasiswa",
            options=["umum", "baru", "lama"],
            help="Umum: Standard, Baru: Baru masuk, Lama: Sudah kuliah dengan IPK"
        )
    
    # Field tambahan berdasarkan kategori
    if kategori == "lama":
        col3, col4 = st.columns(2)
        with col3:
            ipk = st.number_input("IPK", min_value=0.0, max_value=4.0, value=3.0, step=0.1)
        with col4:
            status = st.selectbox("Status", options=["aktif", "tidak aktif", "lulus", "cuti"])
    else:
        ipk = 0.0
        status = "aktif"
    
    # Tombol submit
    if st.button("✅ Tambah Mahasiswa", type="primary", use_container_width=True):
        if not nama or not nim or not email:
            st.error("❌ Semua field harus diisi!")
        else:
            crud = st.session_state.crud_manager
            success, message = crud.create_mahasiswa(
                nama=nama,
                nim=nim,
                jurusan=jurusan,
                email=email,
                tahun_masuk=tahun_masuk,
                status=status,
                kategori=kategori,
                ipk=ipk
            )
            
            if success:
                st.success(message)
                st.session_state.last_action = "created"
                st.rerun()
            else:
                st.error(message)


def ui_lihat_data():
    """UI untuk melihat semua data mahasiswa."""
    st.markdown('<div class="section-title">📋 LIHAT DATA MAHASISWA</div>', 
                unsafe_allow_html=True)
    
    crud = st.session_state.crud_manager
    data = crud.read_all_mahasiswa()
    
    if not data:
        st.warning("📭 Belum ada data mahasiswa. Tambahkan mahasiswa baru terlebih dahulu.")
        return
    
    # Konversi ke DataFrame untuk ditampilkan
    df = pd.DataFrame(data)
    
    # Pilih kolom yang ditampilkan
    st.subheader("📊 Tabel Data Mahasiswa")
    
    # Filter berdasarkan jurusan
    col1, col2 = st.columns(2)
    with col1:
        jurusan_filter = st.multiselect(
            "Filter by Jurusan",
            options=df['jurusan'].unique(),
            help="Kosongkan untuk menampilkan semua"
        )
    
    with col2:
        status_filter = st.multiselect(
            "Filter by Status",
            options=df['status'].unique(),
            help="Kosongkan untuk menampilkan semua"
        )
    
    # Apply filters
    filtered_df = df.copy()
    if jurusan_filter:
        filtered_df = filtered_df[filtered_df['jurusan'].isin(jurusan_filter)]
    if status_filter:
        filtered_df = filtered_df[filtered_df['status'].isin(status_filter)]
    
    # Tampilkan tabel
    st.dataframe(filtered_df, use_container_width=True)
    
    st.info(f"Total: {len(filtered_df)} mahasiswa")


def ui_edit_mahasiswa():
    """UI untuk mengedit data mahasiswa."""
    st.markdown('<div class="section-title">✏️ EDIT MAHASISWA</div>', 
                unsafe_allow_html=True)
    
    crud = st.session_state.crud_manager
    data = crud.read_all_mahasiswa()
    
    if not data:
        st.warning("📭 Belum ada data mahasiswa.")
        return
    
    # Cari mahasiswa berdasarkan NIM
    nim_list = [m['nim'] for m in data]
    nim_selected = st.selectbox("Pilih Mahasiswa (berdasarkan NIM)", options=nim_list)
    
    # Tampilkan data mahasiswa yang dipilih
    mahasiswa = crud.read_mahasiswa_by_nim(nim_selected)
    
    if mahasiswa:
        st.info(f"📌 Mengedit: **{mahasiswa['nama']}** (NIM: {mahasiswa['nim']})")
        
        col1, col2 = st.columns(2)
        
        with col1:
            new_nama = st.text_input("Nama", value=mahasiswa['nama'])
            new_email = st.text_input("Email", value=mahasiswa['email'])
        
        with col2:
            new_jurusan = st.text_input("Jurusan", value=mahasiswa['jurusan'])
            new_status = st.selectbox(
                "Status",
                options=["aktif", "tidak aktif", "lulus", "cuti"],
                index=["aktif", "tidak aktif", "lulus", "cuti"].index(mahasiswa.get('status', 'aktif'))
            )
        
        # Field IPK jika ada
        new_ipk = None
        if 'ipk' in mahasiswa:
            new_ipk = st.number_input("IPK", min_value=0.0, max_value=4.0, 
                                      value=mahasiswa['ipk'], step=0.1)
        
        # Tombol submit
        if st.button("💾 Simpan Perubahan", type="primary", use_container_width=True):
            success, message = crud.update_mahasiswa(
                nim=nim_selected,
                nama=new_nama,
                jurusan=new_jurusan,
                email=new_email,
                status=new_status,
                ipk=new_ipk
            )
            
            if success:
                st.success(message)
                st.rerun()
            else:
                st.error(message)


def ui_hapus_mahasiswa():
    """UI untuk menghapus mahasiswa."""
    st.markdown('<div class="section-title">🗑️ HAPUS MAHASISWA</div>', 
                unsafe_allow_html=True)
    
    st.warning("⚠️ Tindakan ini tidak dapat dibatalkan. Pastikan data yang dihapus sudah benar!")
    
    crud = st.session_state.crud_manager
    data = crud.read_all_mahasiswa()
    
    if not data:
        st.warning("📭 Belum ada data mahasiswa.")
        return
    
    # Buat pilihan untuk delete
    nim_list = [f"{m['nim']} - {m['nama']}" for m in data]
    selected = st.selectbox("Pilih Mahasiswa untuk Dihapus", options=nim_list)
    nim_to_delete = selected.split(" - ")[0]
    
    # Konfirmasi
    if st.button("❌ Hapus Mahasiswa", type="secondary", use_container_width=True):
        success, message = crud.delete_mahasiswa(nim_to_delete)
        
        if success:
            st.success(message)
            st.rerun()
        else:
            st.error(message)


def ui_cari_mahasiswa():
    """UI untuk mencari mahasiswa."""
    st.markdown('<div class="section-title">🔍 CARI MAHASISWA</div>', 
                unsafe_allow_html=True)
    
    crud = st.session_state.crud_manager
    data = crud.read_all_mahasiswa()
    
    if not data:
        st.warning("📭 Belum ada data mahasiswa.")
        return
    
    # Pilih tipe pencarian
    col1, col2 = st.columns([1, 2])
    
    with col1:
        search_type = st.radio(
            "Metode Pencarian:",
            options=["Linear Search", "Binary Search"]
        )
    
    with col2:
        search_key = st.selectbox(
            "Cari Berdasarkan:",
            options=["nama", "nim", "jurusan", "email"]
        )
    
    search_value = st.text_input("Masukkan Nilai yang Dicari")
    
    if st.button("🔎 Cari", type="primary", use_container_width=True):
        if not search_value:
            st.warning("⚠️ Masukkan nilai pencarian terlebih dahulu")
            return
        
        searching = AlgoritmaSearching()
        
        if search_type == "Linear Search":
            # Linear search langsung pada data
            index, comparisons = searching.linear_search(data, search_key, search_value)
            
            # Tampilkan Big O Notation
            big_o = searching.get_big_o_notation("linear_search")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Best Case", big_o['best_case'])
            with col2:
                st.metric("Average Case", big_o['average_case'])
            with col3:
                st.metric("Worst Case", big_o['worst_case'])
            with col4:
                st.metric("Space", big_o['space_complexity'])
            
            st.info(f"📊 Jumlah Perbandingan: {comparisons}")
            
            if index is not None:
                st.success("✅ Data Ditemukan!")
                st.dataframe(pd.DataFrame([data[index]]), use_container_width=True)
            else:
                st.warning("❌ Data tidak ditemukan")
        
        else:  # Binary Search
            # Urutkan data sesuai key
            sorted_data, _ = AlgoritmaSorting.merge_sort(data, key=search_key, ascending=True)
            
            # Lakukan binary search
            index, comparisons = searching.binary_search(sorted_data, search_key, search_value)
            
            # Tampilkan Big O Notation
            big_o = searching.get_big_o_notation("binary_search")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Best Case", big_o['best_case'])
            with col2:
                st.metric("Average Case", big_o['average_case'])
            with col3:
                st.metric("Worst Case", big_o['worst_case'])
            with col4:
                st.metric("Space", big_o['space_complexity'])
            
            st.info(f"📊 Jumlah Perbandingan: {comparisons} | "
                   f"ℹ️ Data di-sorting otomatis sebelum pencarian")
            
            if index is not None:
                st.success("✅ Data Ditemukan!")
                st.dataframe(pd.DataFrame([sorted_data[index]]), use_container_width=True)
            else:
                st.warning("❌ Data tidak ditemukan")


def ui_sorting():
    """UI untuk sorting data."""
    st.markdown('<div class="section-title">📊 SORTING DATA</div>', 
                unsafe_allow_html=True)
    
    crud = st.session_state.crud_manager
    data = crud.read_all_mahasiswa()
    
    if not data:
        st.warning("📭 Belum ada data mahasiswa.")
        return
    
    # Pilih algoritma
    col1, col2, col3 = st.columns(3)
    
    with col1:
        algoritma = st.selectbox(
            "Pilih Algoritma Sorting:",
            options=["Bubble Sort", "Merge Sort", "Shell Sort"]
        )
    
    with col2:
        sort_key = st.selectbox(
            "Urutkan Berdasarkan:",
            options=["nama", "nim", "jurusan", "email"]
        )
    
    with col3:
        sort_order = st.radio(
            "Urutan:",
            options=["Ascending ↑", "Descending ↓"],
            horizontal=True
        )
    
    ascending = sort_order == "Ascending ↑"
    
    # Pilih metode algoritma
    sorting = AlgoritmaSorting()
    
    if st.button("▶️ Jalankan Sorting", type="primary", use_container_width=True):
        # Jalankan sorting
        if algoritma == "Bubble Sort":
            sorted_data, comparisons = sorting.bubble_sort(data, sort_key, ascending)
            algo_key = "bubble_sort"
        elif algoritma == "Merge Sort":
            sorted_data, comparisons = sorting.merge_sort(data, sort_key, ascending)
            algo_key = "merge_sort"
        else:  # Shell Sort
            sorted_data, comparisons = sorting.shell_sort(data, sort_key, ascending)
            algo_key = "shell_sort"
        
        # Tampilkan Big O Notation
        big_o = sorting.get_big_o_notation(algo_key)
        
        st.success(f"✅ Sorting Selesai! Dibutuhkan {comparisons} perbandingan.")
        
        # Tampilkan tabel Big O
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Best Case", big_o['best_case'])
        with col2:
            st.metric("Average Case", big_o['average_case'])
        with col3:
            st.metric("Worst Case", big_o['worst_case'])
        with col4:
            st.metric("Space Complexity", big_o['space_complexity'])
        
        # Informasi tambahan
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Tipe Algoritma", big_o['tipe'])
        with col2:
            st.metric("Stabil", big_o['stabil'])
        
        # Tampilkan hasil
        st.subheader("📋 Hasil Sorting:")
        st.dataframe(pd.DataFrame(sorted_data), use_container_width=True)


def ui_statistik():
    """UI untuk menampilkan statistik."""
    st.markdown('<div class="section-title">📈 STATISTIK DATA MAHASISWA</div>', 
                unsafe_allow_html=True)
    
    crud = st.session_state.crud_manager
    statik = crud.get_statistik()
    data = crud.read_all_mahasiswa()
    
    if not data:
        st.warning("📭 Belum ada data mahasiswa.")
        return
    
    # Tampilkan metrics utama
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📚 Total Mahasiswa", statik['total_mahasiswa'])
    
    with col2:
        st.metric("🏢 Jumlah Jurusan", len(statik['total_per_jurusan']))
    
    with col3:
        st.metric("📊 Rata-rata IPK", f"{statik['rata_ipk']:.2f}")
    
    with col4:
        st.metric("✅ Dengan IPK", statik['data_dengan_ipk'])
    
    st.divider()
    
    # Statistik per jurusan
    st.subheader("📚 Distribusi per Jurusan")
    jurusan_data = statik['total_per_jurusan']
    
    if jurusan_data:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Tabel
            jurusan_df = pd.DataFrame(
                list(jurusan_data.items()),
                columns=['Jurusan', 'Jumlah']
            )
            st.dataframe(jurusan_df, use_container_width=True)
        
        with col2:
            # Chart
            st.bar_chart(jurusan_data)
    
    st.divider()
    
    # Statistik per status
    st.subheader("✅ Distribusi per Status")
    status_data = statik['total_per_status']
    
    if status_data:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            status_df = pd.DataFrame(
                list(status_data.items()),
                columns=['Status', 'Jumlah']
            )
            st.dataframe(status_df, use_container_width=True)
        
        with col2:
            st.bar_chart(status_data)


# ========== MAIN FUNCTION ==========

def main():
    """Fungsi utama aplikasi Streamlit."""
    configure_streamlit()
    init_session_state()
    
    # Check login status
    if not st.session_state.logged_in:
        ui_login_page()
        return
    
    # Sidebar menu setelah login
    menu = ui_sidebar_menu()
    
    # Route ke halaman sesuai menu
    if menu == "profil":
        ui_profile_page()
    elif menu == "ubah_password":
        ui_change_password()
    elif menu == "🏠 Dashboard":
        ui_dashboard()
    elif menu == "➕ Tambah Mahasiswa":
        ui_tambah_mahasiswa()
    elif menu == "📋 Lihat Data Mahasiswa":
        ui_lihat_data()
    elif menu == "✏️ Edit Mahasiswa":
        ui_edit_mahasiswa()
    elif menu == "🗑️ Hapus Mahasiswa":
        ui_hapus_mahasiswa()
    elif menu == "🔍 Cari Mahasiswa":
        ui_cari_mahasiswa()
    elif menu == "📊 Sorting Data":
        ui_sorting()
    elif menu == "📈 Statistik":
        ui_statistik()


if __name__ == "__main__":
    main()
