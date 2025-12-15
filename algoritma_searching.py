"""
Module untuk Algoritma Searching (Linear Search dan Binary Search).
Termasuk analisis Big O Notation.

Developer: Ahmad Rasyid - Teknik Informatika
Date: 2025-12-15
"""

from typing import List, Tuple, Optional
from mahasiswa import Mahasiswa


class AlgoritmaSearching:
    """
    Class untuk mengimplementasikan berbagai algoritma searching.
    """
    
    @staticmethod
    def linear_search(
        data: List[dict],
        search_key: str,
        search_value: str
    ) -> Tuple[Optional[int], int]:
        """
        Linear Search - Pencarian dengan memeriksa setiap elemen.
        
        ===== ANALISIS LINEAR SEARCH =====
        Time Complexity:
        - Best Case: O(1) - elemen ditemukan di posisi pertama
        - Average Case: O(n) - elemen ditemukan di tengah
        - Worst Case: O(n) - elemen di akhir atau tidak ditemukan
        
        Space Complexity: O(1) - hanya perlu satu variabel tambahan
        
        Cara Kerja:
        1. Mulai dari elemen pertama
        2. Bandingkan setiap elemen dengan nilai yang dicari
        3. Jika ditemukan, return index
        4. Jika semua diperiksa tidak ditemukan, return -1 (atau None)
        
        Keuntungan:
        - Bekerja pada data terurut atau tidak terurut
        - Implementasi sederhana
        
        Kerugian:
        - Lambat untuk data besar (O(n))
        - Harus memeriksa setiap elemen
        
        Args:
            data: List dari dictionary mahasiswa
            search_key: Kunci untuk pencarian ("nama", "nim", "jurusan", "email")
            search_value: Nilai yang dicari (case-insensitive)
        
        Returns:
            Tuple (index yang ditemukan atau None, jumlah perbandingan)
        """
        search_value_lower = str(search_value).lower()
        comparison_count = 0
        
        for index, item in enumerate(data):
            comparison_count += 1
            
            # Konversi ke string dan lowercase untuk case-insensitive search
            current_value = str(item.get(search_key, "")).lower()
            
            # Cek apakah nilai cocok (substring matching)
            if search_value_lower in current_value:
                return index, comparison_count
        
        # Tidak ditemukan
        return None, comparison_count
    
    @staticmethod
    def linear_search_exact(
        data: List[dict],
        search_key: str,
        search_value: str
    ) -> Tuple[Optional[int], int]:
        """
        Linear Search dengan pencarian exact match (bukan substring).
        
        Args:
            data: List dari dictionary mahasiswa
            search_key: Kunci untuk pencarian
            search_value: Nilai yang dicari
        
        Returns:
            Tuple (index yang ditemukan atau None, jumlah perbandingan)
        """
        comparison_count = 0
        
        for index, item in enumerate(data):
            comparison_count += 1
            
            current_value = str(item.get(search_key, ""))
            
            if search_value == current_value:
                return index, comparison_count
        
        return None, comparison_count
    
    @staticmethod
    def binary_search(
        data: List[dict],
        search_key: str,
        search_value: str
    ) -> Tuple[Optional[int], int]:
        """
        Binary Search - Pencarian cepat untuk data yang sudah terurut.
        
        ===== ANALISIS BINARY SEARCH =====
        Time Complexity:
        - Best Case: O(1) - elemen ditemukan di posisi tengah
        - Average Case: O(log n) - membagi data menjadi 2 setiap iterasi
        - Worst Case: O(log n) - bahkan jika tidak ditemukan
        
        Space Complexity: O(1) - iteratif version, O(log n) jika recursive
        
        Cara Kerja (Divide & Conquer):
        1. Tentukan left = 0, right = n-1, mid = (left + right) // 2
        2. Bandingkan nilai di mid dengan nilai yang dicari
        3. Jika cocok, return mid
        4. Jika nilai di mid > target, search di left half (right = mid - 1)
        5. Jika nilai di mid < target, search di right half (left = mid + 1)
        6. Ulangi sampai ditemukan atau left > right
        
        Keuntungan:
        - Sangat cepat untuk data besar O(log n)
        - Setiap step mengeliminasi setengah data
        
        Kerugian:
        - DATA HARUS SUDAH TERURUT
        - Tidak bisa digunakan untuk substring matching
        
        Args:
            data: List dari dictionary mahasiswa (HARUS SUDAH TERURUT)
            search_key: Kunci untuk pencarian (biasanya "nim" atau "nama")
            search_value: Nilai yang dicari (exact match)
        
        Returns:
            Tuple (index yang ditemukan atau None, jumlah perbandingan)
        """
        left = 0
        right = len(data) - 1
        comparison_count = 0
        
        while left <= right:
            mid = (left + right) // 2
            comparison_count += 1
            
            mid_value = str(data[mid].get(search_key, ""))
            search_value_str = str(search_value)
            
            # Cek apakah nilai di mid cocok dengan yang dicari
            if mid_value == search_value_str:
                return mid, comparison_count
            
            # Bandingkan untuk menentukan ke arah mana pencarian dilanjutkan
            elif mid_value < search_value_str:
                # Nilai target ada di sebelah kanan
                left = mid + 1
            else:
                # Nilai target ada di sebelah kiri
                right = mid - 1
        
        # Tidak ditemukan
        return None, comparison_count
    
    @staticmethod
    def get_big_o_notation(algoritma: str) -> dict:
        """
        Mengembalikan informasi Big O Notation untuk algoritma searching.
        
        Args:
            algoritma: Nama algoritma ("linear_search" atau "binary_search")
        
        Returns:
            Dictionary dengan informasi Big O
        """
        notations = {
            "linear_search": {
                "nama": "Linear Search",
                "best_case": "O(1)",
                "average_case": "O(n)",
                "worst_case": "O(n)",
                "space_complexity": "O(1)",
                "data_requirement": "Dapat terurut atau tidak",
                "tipe": "Brute Force",
                "keterangan": "Memeriksa setiap elemen dari awal"
            },
            "binary_search": {
                "nama": "Binary Search",
                "best_case": "O(1)",
                "average_case": "O(log n)",
                "worst_case": "O(log n)",
                "space_complexity": "O(1)",
                "data_requirement": "HARUS TERURUT",
                "tipe": "Divide & Conquer",
                "keterangan": "Membagi data menjadi 2 setiap iterasi"
            }
        }
        
        return notations.get(algoritma, {})
