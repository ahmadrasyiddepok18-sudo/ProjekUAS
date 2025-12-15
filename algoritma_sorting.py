"""
Module untuk Algoritma Sorting dengan implementasi Bubble Sort dan Merge Sort.
Termasuk analisis Big O Notation.

Developer: Ahmad Rasyid - Teknik Informatika
Date: 2025-12-15
"""

from typing import List, Tuple, Callable
from mahasiswa import Mahasiswa


class AlgoritmaSorting:
    """
    Class untuk mengimplementasikan berbagai algoritma sorting.
    Setiap metode sorting mencatat jumlah perbandingan untuk analisis.
    """
    
    @staticmethod
    def bubble_sort(
        data: List,
        key: str = "nama",
        ascending: bool = True
    ) -> Tuple[List, int]:
        """
        Bubble Sort - Algoritma sorting sederhana.
        
        ===== ANALISIS BUBBLE SORT =====
        Time Complexity:
        - Best Case: O(n) - ketika data sudah terurut, dengan optimasi
        - Average Case: O(n²) - pertukaran terjadi secara random
        - Worst Case: O(n²) - ketika data terbalik dari urutan yang diinginkan
        
        Space Complexity: O(1) - sorting in-place, tidak perlu space tambahan
        
        Cara Kerja:
        1. Bandingkan elemen bersebelahan
        2. Tukar jika urutan salah
        3. Ulangi sampai tidak ada pertukaran (data sudah terurut)
        
        Keuntungan: Mudah dipahami dan implementasi sederhana
        Kerugian: Sangat lambat untuk data besar (O(n²))
        
        Args:
            data: List mahasiswa (bisa List[Mahasiswa] atau List[dict])
            key: Atribut untuk sorting ("nama" atau "nim")
            ascending: True untuk ascending, False untuk descending
        
        Returns:
            Tuple (data terurut, jumlah perbandingan)
        """
        # Copy data - handle both Mahasiswa objects and dicts
        if data and hasattr(data[0], 'info'):
            arr = [mahasiswa.info() for mahasiswa in data]
        else:
            arr = [dict(item) for item in data]
        n = len(arr)
        comparison_count = 0
        
        # Bubble Sort dengan optimasi
        for i in range(n):
            swapped = False  # Flag untuk deteksi jika sudah terurut
            
            # Setiap iterasi, elemen terbesar akan "bubble up" ke akhir
            for j in range(0, n - i - 1):
                comparison_count += 1
                
                # Dapatkan nilai untuk perbandingan
                val1 = arr[j][key]
                val2 = arr[j + 1][key]
                
                # Bandingkan sesuai arah sorting
                if (val1 > val2 and ascending) or (val1 < val2 and not ascending):
                    # Tukar elemen
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            # Jika tidak ada pertukaran, array sudah terurut
            if not swapped:
                break
        
        return arr, comparison_count
    
    @staticmethod
    def merge_sort(
        data: List,
        key: str = "nama",
        ascending: bool = True
    ) -> Tuple[List, int]:
        """
        Merge Sort - Algoritma sorting yang efisien menggunakan Divide & Conquer.
        
        ===== ANALISIS MERGE SORT =====
        Time Complexity:
        - Best Case: O(n log n) - selalu sama, terlepas dari kondisi data
        - Average Case: O(n log n) - konsisten untuk semua kasus
        - Worst Case: O(n log n) - bahkan data terbalik
        
        Space Complexity: O(n) - memerlukan array tambahan untuk merge
        
        Cara Kerja (Divide & Conquer):
        1. Divide: Bagi array menjadi 2 bagian sampai ukuran 1 elemen
        2. Conquer: Merge array yang sudah terurut dengan membandingkan
        3. Combine: Gabungkan subarray yang sudah terurut
        
        Keuntungan: Stabil (urutan relatif sama) dan O(n log n) konsisten
        Kerugian: Memerlukan memory tambahan O(n)
        
        Args:
            data: List mahasiswa yang akan diurutkan (bisa Mahasiswa objects atau dicts)
            key: Atribut untuk sorting ("nama" atau "nim")
            ascending: True untuk ascending, False untuk descending
        
        Returns:
            Tuple (data terurut, jumlah perbandingan)
        """
        # Handle both Mahasiswa objects and dicts
        if data and hasattr(data[0], 'info'):
            arr = [mahasiswa.info() for mahasiswa in data]
        else:
            arr = [dict(item) for item in data]
        comparison_count = [0]  # Gunakan list agar bisa dimodifikasi di nested function
        
        def merge_sort_recursive(arr_segment: List[dict]) -> List[dict]:
            """Rekursi untuk merge sort."""
            # Base case: array dengan 1 elemen sudah terurut
            if len(arr_segment) <= 1:
                return arr_segment
            
            # Divide: bagi array menjadi 2 bagian
            mid = len(arr_segment) // 2
            left = arr_segment[:mid]
            right = arr_segment[mid:]
            
            # Conquer: urutkan kedua bagian secara rekursif
            left = merge_sort_recursive(left)
            right = merge_sort_recursive(right)
            
            # Combine: merge kedua bagian yang sudah terurut
            return merge(left, right)
        
        def merge(left: List[dict], right: List[dict]) -> List[dict]:
            """Merge dua array yang sudah terurut."""
            result = []
            i = j = 0
            
            # Bandingkan elemen dari left dan right
            while i < len(left) and j < len(right):
                comparison_count[0] += 1
                
                val_left = left[i][key]
                val_right = right[j][key]
                
                if (val_left <= val_right and ascending) or \
                   (val_left >= val_right and not ascending):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            # Tambahkan sisa elemen
            result.extend(left[i:])
            result.extend(right[j:])
            
            return result
        
        arr = merge_sort_recursive(arr)
        return arr, comparison_count[0]
    
    @staticmethod
    def shell_sort(
        data: List,
        key: str = "nama",
        ascending: bool = True
    ) -> Tuple[List, int]:
        """
        Shell Sort - Algoritma sorting yang generalisasi dari Insertion Sort.
        
        ===== ANALISIS SHELL SORT =====
        Time Complexity:
        - Best Case: O(n log n) - gap sequence yang optimal
        - Average Case: O(n^1.3) hingga O(n log² n) - tergantung gap sequence
        - Worst Case: O(n²) - jika gap sequence buruk
        
        Space Complexity: O(1) - sorting in-place
        
        Cara Kerja:
        1. Mulai dengan gap yang besar (setengah dari ukuran array)
        2. Urutkan elemen yang berjarak gap menggunakan insertion sort
        3. Kurangi gap (biasanya gap = gap // 2) dan ulangi
        4. Ketika gap = 1, sama seperti regular insertion sort
        
        Keuntungan: Lebih cepat dari bubble sort, lebih simple dari merge sort
        Kerugian: Time complexity tergantung gap sequence
        
        Args:
            data: List mahasiswa yang akan diurutkan (bisa Mahasiswa objects atau dicts)
            key: Atribut untuk sorting ("nama" atau "nim")
            ascending: True untuk ascending, False untuk descending
        
        Returns:
            Tuple (data terurut, jumlah perbandingan)
        """
        # Handle both Mahasiswa objects and dicts
        if data and hasattr(data[0], 'info'):
            arr = [mahasiswa.info() for mahasiswa in data]
        else:
            arr = [dict(item) for item in data]
        n = len(arr)
        comparison_count = 0
        
        # Mulai dengan gap setengah dari panjang array
        gap = n // 2
        
        # Terus kurangi gap sampai 1
        while gap > 0:
            # Lakukan insertion sort untuk elemen yang berjarak gap
            for i in range(gap, n):
                # Simpan elemen di index i
                temp = arr[i]
                j = i
                
                # Bandingkan dengan elemen sebelumnya yang berjarak gap
                while j >= gap:
                    comparison_count += 1
                    
                    val_current = arr[j - gap][key]
                    val_temp = temp[key]
                    
                    if (val_current > val_temp and ascending) or \
                       (val_current < val_temp and not ascending):
                        arr[j] = arr[j - gap]
                        j -= gap
                    else:
                        break
                
                # Letakkan elemen temp di posisi yang benar
                arr[j] = temp
            
            # Kurangi gap untuk iterasi berikutnya
            gap //= 2
        
        return arr, comparison_count
    
    @staticmethod
    def get_big_o_notation(algoritma: str) -> dict:
        """
        Mengembalikan informasi Big O Notation untuk algoritma tertentu.
        
        Args:
            algoritma: Nama algoritma ("bubble_sort", "merge_sort", "shell_sort")
        
        Returns:
            Dictionary dengan informasi Big O untuk berbagai case
        """
        notations = {
            "bubble_sort": {
                "nama": "Bubble Sort",
                "best_case": "O(n)",
                "average_case": "O(n²)",
                "worst_case": "O(n²)",
                "space_complexity": "O(1)",
                "tipe": "Comparison-based",
                "stabil": "Ya"
            },
            "merge_sort": {
                "nama": "Merge Sort",
                "best_case": "O(n log n)",
                "average_case": "O(n log n)",
                "worst_case": "O(n log n)",
                "space_complexity": "O(n)",
                "tipe": "Divide & Conquer",
                "stabil": "Ya"
            },
            "shell_sort": {
                "nama": "Shell Sort",
                "best_case": "O(n log n)",
                "average_case": "O(n^1.3)",
                "worst_case": "O(n²)",
                "space_complexity": "O(1)",
                "tipe": "Insertion Sort variant",
                "stabil": "Tidak"
            }
        }
        
        return notations.get(algoritma, {})
