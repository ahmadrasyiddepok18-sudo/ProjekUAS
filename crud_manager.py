"""
Module untuk CRUD Operations dan File Management.
Menangani penyimpanan dan pembacaan data mahasiswa dari file JSON.

Developer: Ahmad Rasyid - Teknik Informatika
Date: 2025-12-15
"""

import json
import re
from typing import List, Optional, Dict, Any
from datetime import datetime
from mahasiswa import Mahasiswa, MahasiswaBaru, MahasiswaLama


class CRUDManager:
    """
    Class untuk mengelola CRUD operations (Create, Read, Update, Delete)
    dengan penyimpanan file JSON.
    """
    
    def __init__(self, file_path: str = "data_mahasiswa.json"):
        """
        Inisialisasi CRUD Manager.
        
        Args:
            file_path: Path untuk file JSON penyimpanan data
        """
        self.file_path = file_path
        self._ensure_file_exists()
    
    def _ensure_file_exists(self) -> None:
        """
        Memastikan file JSON ada. Jika tidak, buat file dengan data kosong.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                json.load(f)
        except FileNotFoundError:
            # File tidak ada, buat file baru dengan list kosong
            self._save_to_file([])
        except json.JSONDecodeError:
            # File corrupt, inisialisasi dengan data kosong
            self._save_to_file([])
    
    def _save_to_file(self, data: List[Dict]) -> None:
        """
        Simpan data ke file JSON dengan indentation untuk readability.
        
        Args:
            data: List dari dictionary mahasiswa
        
        Raises:
            IOError: Jika ada error saat menulis file
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except IOError as e:
            raise IOError(f"Error saat menyimpan file: {str(e)}")
    
    def _load_from_file(self) -> List[Dict]:
        """
        Muat data dari file JSON.
        
        Returns:
            List dari dictionary mahasiswa
        
        Raises:
            IOError: Jika ada error saat membaca file
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            raise IOError(f"File JSON corrupt: {str(e)}")
        except IOError as e:
            raise IOError(f"Error saat membaca file: {str(e)}")
    
    # ========== VALIDASI INPUT ==========
    
    @staticmethod
    def validasi_nim(nim: str) -> bool:
        """
        Validasi format NIM menggunakan Regex.
        Format: hanya angka, minimal 8 digit.
        
        Args:
            nim: String NIM yang akan divalidasi
        
        Returns:
            True jika valid, False jika tidak
        """
        # Pattern: hanya angka, 8-12 digit
        pattern = r'^\d{8,12}$'
        return bool(re.match(pattern, nim.strip()))
    
    @staticmethod
    def validasi_email(email: str) -> bool:
        """
        Validasi format Email menggunakan Regex.
        Requirements: ada @, ada domain, ada TLD (top-level domain).
        
        Args:
            email: String email yang akan divalidasi
        
        Returns:
            True jika valid, False jika tidak
        """
        # Pattern email: username@domain.tld
        # Username: alfanumerik, titik, underscore, hyphen
        # Domain: alfanumerik, hyphen
        # TLD: minimal 2 karakter
        pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email.strip()))
    
    @staticmethod
    def validasi_nama(nama: str) -> bool:
        """
        Validasi nama: tidak boleh kosong, minimal 3 karakter.
        
        Args:
            nama: String nama yang akan divalidasi
        
        Returns:
            True jika valid, False jika tidak
        """
        return len(nama.strip()) >= 3
    
    @staticmethod
    def validasi_jurusan(jurusan: str) -> bool:
        """
        Validasi jurusan: tidak boleh kosong.
        
        Args:
            jurusan: String jurusan yang akan divalidasi
        
        Returns:
            True jika valid, False jika tidak
        """
        return len(jurusan.strip()) > 0
    
    # ========== CREATE OPERATION ==========
    
    def create_mahasiswa(
        self,
        nama: str,
        nim: str,
        jurusan: str,
        email: str,
        tahun_masuk: int = None,
        status: str = "aktif",
        kategori: str = "umum",
        ipk: float = 0.0
    ) -> tuple[bool, str]:
        """
        Create: Tambah mahasiswa baru ke sistem.
        
        Args:
            nama: Nama mahasiswa
            nim: NIM mahasiswa
            jurusan: Jurusan/program studi
            email: Email mahasiswa
            tahun_masuk: Tahun masuk (opsional)
            status: Status mahasiswa
            kategori: Kategori ("umum", "baru", "lama")
            ipk: IPK mahasiswa (untuk kategori lama)
        
        Returns:
            Tuple (success: bool, message: str)
        """
        try:
            # Validasi input
            if not self.validasi_nama(nama):
                return False, "❌ Nama minimal 3 karakter"
            
            if not self.validasi_nim(nim):
                return False, "❌ NIM harus format angka 8-12 digit"
            
            if not self.validasi_email(email):
                return False, "❌ Email format tidak valid (contoh: user@domain.com)"
            
            if not self.validasi_jurusan(jurusan):
                return False, "❌ Jurusan tidak boleh kosong"
            
            # Load data existing
            data = self._load_from_file()
            
            # Cek apakah NIM sudah ada
            for mahasiswa in data:
                if mahasiswa.get("nim") == nim:
                    return False, f"❌ NIM {nim} sudah terdaftar"
            
            # Buat object mahasiswa berdasarkan kategori
            if kategori == "baru":
                mahasiswa_obj = MahasiswaBaru(nama, nim, jurusan, email, tahun_masuk)
                info = mahasiswa_obj.info()
            elif kategori == "lama":
                mahasiswa_obj = MahasiswaLama(
                    nama, nim, jurusan, email, tahun_masuk, ipk, status
                )
                info = mahasiswa_obj.info()
            else:
                mahasiswa_obj = Mahasiswa(nama, nim, jurusan, email, tahun_masuk, status)
                info = mahasiswa_obj.info()
            
            # Tambah ke data
            data.append(info)
            
            # Simpan ke file
            self._save_to_file(data)
            
            return True, f"✅ Mahasiswa '{nama}' berhasil ditambahkan"
        
        except Exception as e:
            return False, f"❌ Error: {str(e)}"
    
    # ========== READ OPERATION ==========
    
    def read_all_mahasiswa(self) -> List[Dict]:
        """
        Read: Ambil semua data mahasiswa.
        
        Returns:
            List dari dictionary mahasiswa
        """
        try:
            return self._load_from_file()
        except IOError:
            return []
    
    def read_mahasiswa_by_nim(self, nim: str) -> Optional[Dict]:
        """
        Read: Cari mahasiswa berdasarkan NIM.
        
        Args:
            nim: NIM yang dicari
        
        Returns:
            Dictionary mahasiswa atau None jika tidak ditemukan
        """
        try:
            data = self._load_from_file()
            for mahasiswa in data:
                if mahasiswa.get("nim") == nim:
                    return mahasiswa
            return None
        except IOError:
            return None
    
    # ========== UPDATE OPERATION ==========
    
    def update_mahasiswa(
        self,
        nim: str,
        nama: str = None,
        jurusan: str = None,
        email: str = None,
        status: str = None,
        ipk: float = None
    ) -> tuple[bool, str]:
        """
        Update: Edit data mahasiswa berdasarkan NIM.
        
        Args:
            nim: NIM mahasiswa yang akan diupdate
            nama: Nama baru (opsional)
            jurusan: Jurusan baru (opsional)
            email: Email baru (opsional)
            status: Status baru (opsional)
            ipk: IPK baru (opsional, untuk mahasiswa lama)
        
        Returns:
            Tuple (success: bool, message: str)
        """
        try:
            data = self._load_from_file()
            found = False
            
            for mahasiswa in data:
                if mahasiswa.get("nim") == nim:
                    found = True
                    
                    # Validasi dan update field yang diberikan
                    if nama is not None:
                        if not self.validasi_nama(nama):
                            return False, "❌ Nama minimal 3 karakter"
                        mahasiswa["nama"] = nama
                    
                    if jurusan is not None:
                        if not self.validasi_jurusan(jurusan):
                            return False, "❌ Jurusan tidak boleh kosong"
                        mahasiswa["jurusan"] = jurusan
                    
                    if email is not None:
                        if not self.validasi_email(email):
                            return False, "❌ Format email tidak valid"
                        mahasiswa["email"] = email
                    
                    if status is not None:
                        status_valid = ["aktif", "tidak aktif", "lulus", "cuti"]
                        if status.lower() not in status_valid:
                            return False, f"❌ Status harus: {', '.join(status_valid)}"
                        mahasiswa["status"] = status.lower()
                    
                    if ipk is not None:
                        if "ipk" in mahasiswa:
                            if not (0.0 <= ipk <= 4.0):
                                return False, "❌ IPK harus antara 0.0 - 4.0"
                            mahasiswa["ipk"] = round(ipk, 2)
                    
                    break
            
            if not found:
                return False, f"❌ Mahasiswa dengan NIM {nim} tidak ditemukan"
            
            # Simpan perubahan
            self._save_to_file(data)
            return True, f"✅ Data mahasiswa berhasil diupdate"
        
        except Exception as e:
            return False, f"❌ Error saat update: {str(e)}"
    
    # ========== DELETE OPERATION ==========
    
    def delete_mahasiswa(self, nim: str) -> tuple[bool, str]:
        """
        Delete: Hapus mahasiswa berdasarkan NIM.
        
        Args:
            nim: NIM mahasiswa yang akan dihapus
        
        Returns:
            Tuple (success: bool, message: str)
        """
        try:
            data = self._load_from_file()
            initial_length = len(data)
            
            # Filter: hapus mahasiswa dengan NIM yang cocok
            data = [m for m in data if m.get("nim") != nim]
            
            if len(data) == initial_length:
                return False, f"❌ Mahasiswa dengan NIM {nim} tidak ditemukan"
            
            # Simpan data yang sudah dihapus
            self._save_to_file(data)
            return True, f"✅ Mahasiswa berhasil dihapus"
        
        except Exception as e:
            return False, f"❌ Error saat delete: {str(e)}"
    
    # ========== STATISTIK ==========
    
    def get_statistik(self) -> Dict[str, Any]:
        """
        Dapatkan statistik data mahasiswa.
        
        Returns:
            Dictionary berisi berbagai statistik
        """
        try:
            data = self._load_from_file()
            
            if not data:
                return {
                    "total_mahasiswa": 0,
                    "total_per_jurusan": {},
                    "total_per_status": {},
                    "rata_ipk": 0.0
                }
            
            # Hitung statistik
            total_mahasiswa = len(data)
            total_per_jurusan = {}
            total_per_status = {}
            total_ipk = 0.0
            count_ipk = 0
            
            for mahasiswa in data:
                # Per jurusan
                jurusan = mahasiswa.get("jurusan", "Unknown")
                total_per_jurusan[jurusan] = total_per_jurusan.get(jurusan, 0) + 1
                
                # Per status
                status = mahasiswa.get("status", "Unknown")
                total_per_status[status] = total_per_status.get(status, 0) + 1
                
                # Rata-rata IPK
                if "ipk" in mahasiswa:
                    total_ipk += mahasiswa["ipk"]
                    count_ipk += 1
            
            rata_ipk = (total_ipk / count_ipk) if count_ipk > 0 else 0.0
            
            return {
                "total_mahasiswa": total_mahasiswa,
                "total_per_jurusan": total_per_jurusan,
                "total_per_status": total_per_status,
                "rata_ipk": round(rata_ipk, 2),
                "data_dengan_ipk": count_ipk
            }
        
        except Exception as e:
            print(f"Error mendapatkan statistik: {str(e)}")
            return {}
