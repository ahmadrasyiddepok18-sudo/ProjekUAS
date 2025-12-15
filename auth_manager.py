"""
Module untuk Authentication dan User Management.
Menangani login, logout, dan user credentials.

Developer: Ahmad Rasyid - Teknik Informatika
Date: 2025-12-15
"""

import json
import hashlib
from typing import Dict, Tuple, Optional
from datetime import datetime


class AuthManager:
    """
    Class untuk mengelola autentikasi user dan login system.
    """
    
    def __init__(self, file_path: str = "users_data.json"):
        """
        Inisialisasi Auth Manager.
        
        Args:
            file_path: Path untuk file JSON penyimpanan user credentials
        """
        self.file_path = file_path
        self._ensure_users_file_exists()
    
    def _ensure_users_file_exists(self) -> None:
        """
        Memastikan file users JSON ada dengan default users.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                json.load(f)
        except FileNotFoundError:
            # File tidak ada, buat dengan default users
            default_users = [
                {
                    "username": "admin",
                    "password": self._hash_password("admin123"),
                    "nama_lengkap": "Administrator",
                    "role": "admin",
                    "email": "admin@mahasiswa.com",
                    "created_at": datetime.now().isoformat()
                },
                {
                    "username": "user",
                    "password": self._hash_password("user123"),
                    "nama_lengkap": "User Biasa",
                    "role": "user",
                    "email": "user@mahasiswa.com",
                    "created_at": datetime.now().isoformat()
                }
            ]
            self._save_users(default_users)
        except json.JSONDecodeError:
            # File corrupt, reset dengan default users
            default_users = [
                {
                    "username": "admin",
                    "password": self._hash_password("admin123"),
                    "nama_lengkap": "Administrator",
                    "role": "admin",
                    "email": "admin@mahasiswa.com",
                    "created_at": datetime.now().isoformat()
                },
                {
                    "username": "user",
                    "password": self._hash_password("user123"),
                    "nama_lengkap": "User Biasa",
                    "role": "user",
                    "email": "user@mahasiswa.com",
                    "created_at": datetime.now().isoformat()
                }
            ]
            self._save_users(default_users)
    
    @staticmethod
    def _hash_password(password: str) -> str:
        """
        Hash password menggunakan SHA256.
        
        Args:
            password: Password yang akan di-hash
        
        Returns:
            Hashed password (hexadecimal string)
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _load_users(self) -> list:
        """
        Load semua users dari file JSON.
        
        Returns:
            List dari user dictionaries
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save_users(self, users: list) -> None:
        """
        Simpan users ke file JSON.
        
        Args:
            users: List dari user dictionaries
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(users, f, ensure_ascii=False, indent=2)
        except IOError as e:
            raise IOError(f"Error saat menyimpan users: {str(e)}")
    
    def login(self, username: str, password: str) -> Tuple[bool, str, Optional[Dict]]:
        """
        Autentikasi user dengan username dan password.
        
        Args:
            username: Username user
            password: Password user (akan di-hash)
        
        Returns:
            Tuple (success: bool, message: str, user_info: Dict or None)
        """
        if not username or not password:
            return False, "❌ Username dan password harus diisi", None
        
        users = self._load_users()
        hashed_password = self._hash_password(password)
        
        for user in users:
            if user.get("username") == username:
                if user.get("password") == hashed_password:
                    # Login sukses
                    user_info = {
                        "username": user.get("username"),
                        "nama_lengkap": user.get("nama_lengkap"),
                        "role": user.get("role"),
                        "email": user.get("email")
                    }
                    return True, f"✅ Selamat datang, {user.get('nama_lengkap')}!", user_info
                else:
                    return False, "❌ Password salah", None
        
        return False, "❌ Username tidak ditemukan", None
    
    def register(
        self,
        username: str,
        password: str,
        nama_lengkap: str,
        email: str,
        role: str = "user"
    ) -> Tuple[bool, str]:
        """
        Register user baru.
        
        Args:
            username: Username baru
            password: Password baru
            nama_lengkap: Nama lengkap user
            email: Email user
            role: Role user ("admin" atau "user")
        
        Returns:
            Tuple (success: bool, message: str)
        """
        # Validasi input
        if not username or len(username) < 3:
            return False, "❌ Username minimal 3 karakter"
        
        if not password or len(password) < 6:
            return False, "❌ Password minimal 6 karakter"
        
        if not nama_lengkap or len(nama_lengkap) < 3:
            return False, "❌ Nama lengkap minimal 3 karakter"
        
        if not email or '@' not in email:
            return False, "❌ Email format tidak valid"
        
        # Check duplicate username
        users = self._load_users()
        for user in users:
            if user.get("username") == username:
                return False, "❌ Username sudah terdaftar"
            if user.get("email") == email:
                return False, "❌ Email sudah terdaftar"
        
        # Buat user baru
        new_user = {
            "username": username.strip(),
            "password": self._hash_password(password),
            "nama_lengkap": nama_lengkap.strip(),
            "email": email.strip(),
            "role": role,
            "created_at": datetime.now().isoformat()
        }
        
        users.append(new_user)
        self._save_users(users)
        
        return True, f"✅ User '{username}' berhasil didaftarkan"
    
    def get_user_by_username(self, username: str) -> Optional[Dict]:
        """
        Get user info berdasarkan username.
        
        Args:
            username: Username yang dicari
        
        Returns:
            User dictionary atau None jika tidak ditemukan
        """
        users = self._load_users()
        for user in users:
            if user.get("username") == username:
                return {
                    "username": user.get("username"),
                    "nama_lengkap": user.get("nama_lengkap"),
                    "role": user.get("role"),
                    "email": user.get("email"),
                    "created_at": user.get("created_at")
                }
        return None
    
    def change_password(
        self,
        username: str,
        old_password: str,
        new_password: str
    ) -> Tuple[bool, str]:
        """
        Ubah password user.
        
        Args:
            username: Username user
            old_password: Password lama
            new_password: Password baru
        
        Returns:
            Tuple (success: bool, message: str)
        """
        # Verify old password
        success, msg, _ = self.login(username, old_password)
        if not success:
            return False, "❌ Password lama salah"
        
        # Validasi password baru
        if not new_password or len(new_password) < 6:
            return False, "❌ Password baru minimal 6 karakter"
        
        if new_password == old_password:
            return False, "❌ Password baru tidak boleh sama dengan password lama"
        
        # Update password
        users = self._load_users()
        for user in users:
            if user.get("username") == username:
                user["password"] = self._hash_password(new_password)
                self._save_users(users)
                return True, "✅ Password berhasil diubah"
        
        return False, "❌ User tidak ditemukan"
    
    def get_all_users(self) -> list:
        """
        Get semua users (untuk admin dashboard).
        
        Returns:
            List dari user info (tanpa password)
        """
        users = self._load_users()
        return [
            {
                "username": u.get("username"),
                "nama_lengkap": u.get("nama_lengkap"),
                "email": u.get("email"),
                "role": u.get("role"),
                "created_at": u.get("created_at")
            }
            for u in users
        ]
    
    def delete_user(self, username: str) -> Tuple[bool, str]:
        """
        Delete user (admin only).
        
        Args:
            username: Username yang akan dihapus
        
        Returns:
            Tuple (success: bool, message: str)
        """
        users = self._load_users()
        
        if username == "admin":
            return False, "❌ User admin tidak dapat dihapus"
        
        initial_count = len(users)
        users = [u for u in users if u.get("username") != username]
        
        if len(users) == initial_count:
            return False, f"❌ User '{username}' tidak ditemukan"
        
        self._save_users(users)
        return True, f"✅ User '{username}' berhasil dihapus"
