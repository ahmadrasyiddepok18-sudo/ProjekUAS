"""
Module untuk Class Mahasiswa dengan OOP Architecture
Berisi implementasi Encapsulation, Inheritance, dan Polymorphism

Developer: Ahmad Rasyid - Teknik Informatika
Date: 2025-12-15
"""

from datetime import datetime
from typing import Dict, Any


class Mahasiswa:
    """
    Class Mahasiswa dengan atribut privat (Encapsulation).
    
    Atribut privat menggunakan prefix __ (double underscore) untuk name mangling.
    Python menggunakan OBJECT REFERENCES (referensi objek) bukan pointer seperti C++:
    - Dalam C++: Pointer adalah alamat memory mentah yang dapat dimanipulasi
    - Dalam Python: Reference adalah referensi yang aman ke object di memory
    - Python secara otomatis mengelola reference counting dan garbage collection
    - Ketika kita assign: mahasiswa = Mahasiswa(...), 'mahasiswa' adalah referensi ke object
    - Tidak ada arithmetic pada reference seperti pointer increment (++p) di C++
    """
    
    # Class variable untuk tracking total mahasiswa
    total_mahasiswa = 0
    
    def __init__(self, nama: str, nim: str, jurusan: str, email: str, 
                 tahun_masuk: int = None, status: str = "aktif"):
        """
        Inisialisasi object Mahasiswa dengan atribut privat.
        
        Args:
            nama: Nama lengkap mahasiswa
            nim: Nomor Induk Mahasiswa (harus format angka)
            jurusan: Program studi mahasiswa
            email: Email mahasiswa (harus format valid)
            tahun_masuk: Tahun masuk kuliah
            status: Status mahasiswa (default: "aktif")
        """
        # Atribut privat - hanya bisa diakses via property/method
        self.__nama = nama
        self.__nim = nim
        self.__jurusan = jurusan
        self.__email = email
        self.__tahun_masuk = tahun_masuk or datetime.now().year
        self.__status = status
        self.__tanggal_dibuat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Increment total mahasiswa
        Mahasiswa.total_mahasiswa += 1
    
    # ========== GETTER & SETTER (Property Encapsulation) ==========
    
    @property
    def nama(self) -> str:
        """Getter untuk nama mahasiswa."""
        return self.__nama
    
    @nama.setter
    def nama(self, value: str) -> None:
        """Setter untuk nama mahasiswa."""
        if not value or len(value.strip()) == 0:
            raise ValueError("Nama tidak boleh kosong")
        self.__nama = value.strip()
    
    @property
    def nim(self) -> str:
        """Getter untuk NIM mahasiswa."""
        return self.__nim
    
    @nim.setter
    def nim(self, value: str) -> None:
        """Setter untuk NIM mahasiswa."""
        if not value or len(value.strip()) == 0:
            raise ValueError("NIM tidak boleh kosong")
        self.__nim = value.strip()
    
    @property
    def jurusan(self) -> str:
        """Getter untuk jurusan mahasiswa."""
        return self.__jurusan
    
    @jurusan.setter
    def jurusan(self, value: str) -> None:
        """Setter untuk jurusan mahasiswa."""
        if not value or len(value.strip()) == 0:
            raise ValueError("Jurusan tidak boleh kosong")
        self.__jurusan = value.strip()
    
    @property
    def email(self) -> str:
        """Getter untuk email mahasiswa."""
        return self.__email
    
    @email.setter
    def email(self, value: str) -> None:
        """Setter untuk email mahasiswa."""
        if not value or len(value.strip()) == 0:
            raise ValueError("Email tidak boleh kosong")
        self.__email = value.strip()
    
    @property
    def tahun_masuk(self) -> int:
        """Getter untuk tahun masuk mahasiswa."""
        return self.__tahun_masuk
    
    @tahun_masuk.setter
    def tahun_masuk(self, value: int) -> None:
        """Setter untuk tahun masuk mahasiswa."""
        if not isinstance(value, int) or value < 1990 or value > datetime.now().year:
            raise ValueError("Tahun masuk harus angka antara 1990 dan tahun sekarang")
        self.__tahun_masuk = value
    
    @property
    def status(self) -> str:
        """Getter untuk status mahasiswa."""
        return self.__status
    
    @status.setter
    def status(self, value: str) -> None:
        """Setter untuk status mahasiswa."""
        status_valid = ["aktif", "tidak aktif", "lulus", "cuti"]
        if value.lower() not in status_valid:
            raise ValueError(f"Status harus salah satu dari: {', '.join(status_valid)}")
        self.__status = value.lower()
    
    @property
    def tanggal_dibuat(self) -> str:
        """Getter untuk tanggal dibuat."""
        return self.__tanggal_dibuat
    
    # ========== METHOD UNTUK INFORMASI ==========
    
    def __str__(self) -> str:
        """
        Polymorphism: Override metode __str__ untuk representasi string object.
        Metode ini dipanggil ketika object dikonversi menjadi string.
        """
        return (f"Mahasiswa(Nama: {self.__nama}, NIM: {self.__nim}, "
                f"Jurusan: {self.__jurusan}, Email: {self.__email}, "
                f"Status: {self.__status})")
    
    def __repr__(self) -> str:
        """Representasi untuk debugging."""
        return self.__str__()
    
    def info(self) -> Dict[str, Any]:
        """
        Method untuk mendapatkan informasi lengkap dalam bentuk dictionary.
        Polymorphism: Metode ini bisa di-override di subclass.
        """
        return {
            "nama": self.__nama,
            "nim": self.__nim,
            "jurusan": self.__jurusan,
            "email": self.__email,
            "tahun_masuk": self.__tahun_masuk,
            "status": self.__status,
            "tanggal_dibuat": self.__tanggal_dibuat
        }
    
    def info_display(self) -> str:
        """Method untuk menampilkan info dalam format readable."""
        return (
            f"📋 Nama: {self.__nama}\n"
            f"🆔 NIM: {self.__nim}\n"
            f"📚 Jurusan: {self.__jurusan}\n"
            f"📧 Email: {self.__email}\n"
            f"📅 Tahun Masuk: {self.__tahun_masuk}\n"
            f"✅ Status: {self.__status}"
        )


class MahasiswaBaru(Mahasiswa):
    """
    Inheritance: Class MahasiswaBaru mewarisi dari class Mahasiswa.
    Digunakan untuk mahasiswa baru dengan atribut tambahan.
    """
    
    def __init__(self, nama: str, nim: str, jurusan: str, email: str,
                 tahun_masuk: int = None, program_orientasi: bool = True):
        """
        Inisialisasi MahasiswaBaru dengan atribut tambahan.
        Memanggil super().__init__() untuk inisialisasi parent class.
        """
        super().__init__(nama, nim, jurusan, email, tahun_masuk, status="aktif")
        self.program_orientasi = program_orientasi
    
    def info(self) -> Dict[str, Any]:
        """
        Polymorphism: Override method info() dari parent class.
        Menambahkan informasi spesifik untuk mahasiswa baru.
        """
        info_parent = super().info()
        info_parent["program_orientasi"] = self.program_orientasi
        info_parent["kategori"] = "Mahasiswa Baru"
        return info_parent
    
    def info_display(self) -> str:
        """Override method info_display() dengan tambahan info program orientasi."""
        info_parent = super().info_display()
        program_text = "Sudah Mengikuti" if self.program_orientasi else "Belum Mengikuti"
        return f"{info_parent}\n🎓 Program Orientasi: {program_text}"


class MahasiswaLama(Mahasiswa):
    """
    Inheritance: Class MahasiswaLama mewarisi dari class Mahasiswa.
    Digunakan untuk mahasiswa lama dengan atribut IPK.
    """
    
    def __init__(self, nama: str, nim: str, jurusan: str, email: str,
                 tahun_masuk: int = None, ipk: float = 0.0, status: str = "aktif"):
        """
        Inisialisasi MahasiswaLama dengan atribut IPK.
        """
        super().__init__(nama, nim, jurusan, email, tahun_masuk, status)
        self._ipk = ipk  # Atribut protected (single underscore)
    
    @property
    def ipk(self) -> float:
        """Getter untuk IPK."""
        return self._ipk
    
    @ipk.setter
    def ipk(self, value: float) -> None:
        """Setter untuk IPK dengan validasi."""
        if not isinstance(value, (int, float)) or value < 0.0 or value > 4.0:
            raise ValueError("IPK harus angka antara 0.0 dan 4.0")
        self._ipk = round(value, 2)
    
    def get_keterangan_ipk(self) -> str:
        """Method untuk mendapatkan keterangan berdasarkan IPK."""
        if self._ipk >= 3.5:
            return "Cumlaude"
        elif self._ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self._ipk >= 2.5:
            return "Memuaskan"
        else:
            return "Cukup"
    
    def info(self) -> Dict[str, Any]:
        """
        Polymorphism: Override method info() dengan tambahan IPK.
        """
        info_parent = super().info()
        info_parent["ipk"] = self._ipk
        info_parent["keterangan_ipk"] = self.get_keterangan_ipk()
        info_parent["kategori"] = "Mahasiswa Lama"
        return info_parent
    
    def info_display(self) -> str:
        """Override method info_display() dengan informasi IPK."""
        info_parent = super().info_display()
        return (f"{info_parent}\n"
                f"📊 IPK: {self._ipk}\n"
                f"🏆 Keterangan: {self.get_keterangan_ipk()}")
