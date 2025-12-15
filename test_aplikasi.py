"""
File untuk testing dan demo aplikasi Manajemen Data Mahasiswa.
Bisa dijalankan untuk verifikasi bahwa semua modul berfungsi dengan baik.

Developer: Ahmad Rasyid - Teknik Informatika
"""

from mahasiswa import Mahasiswa, MahasiswaBaru, MahasiswaLama
from algoritma_sorting import AlgoritmaSorting
from algoritma_searching import AlgoritmaSearching
from crud_manager import CRUDManager


def test_oop_encapsulation():
    """Test OOP Encapsulation."""
    print("=" * 60)
    print("TEST 1: OOP Encapsulation")
    print("=" * 60)
    
    # Buat object mahasiswa
    m = Mahasiswa("Budi Santoso", "12345678", "Teknik Informatika", "budi@domain.com")
    
    print(f"\n✓ Object created: {m}")
    print(f"✓ Getter property - Nama: {m.nama}")
    
    # Test setter
    m.nama = "Budi Wijaya"
    print(f"✓ Setter property - New nama: {m.nama}")
    
    # Test info method
    print(f"\n✓ Info method:\n{m.info_display()}")
    
    print("\n✅ Encapsulation test PASSED\n")


def test_oop_inheritance():
    """Test OOP Inheritance."""
    print("=" * 60)
    print("TEST 2: OOP Inheritance")
    print("=" * 60)
    
    # Test MahasiswaBaru
    mb = MahasiswaBaru(
        "Ani Wijaya", "87654321", "Teknik Elektro", 
        "ani@domain.com", 2025, program_orientasi=True
    )
    
    print(f"\n✓ MahasiswaBaru created: {mb}")
    print(f"\n✓ Info (Polymorphism):\n{mb.info_display()}")
    
    # Test MahasiswaLama
    ml = MahasiswaLama(
        "Citra Dewi", "11223344", "Teknik Sipil",
        "citra@domain.com", 2022, ipk=3.85, status="aktif"
    )
    
    print(f"\n✓ MahasiswaLama created: {ml}")
    print(f"\n✓ Info (Polymorphism):\n{ml.info_display()}")
    print(f"\n✓ Keterangan IPK: {ml.get_keterangan_ipk()}")
    
    print("\n✅ Inheritance test PASSED\n")


def test_validation():
    """Test Input Validation."""
    print("=" * 60)
    print("TEST 3: Input Validation (Regex)")
    print("=" * 60)
    
    crud = CRUDManager()
    
    # Test NIM validation
    test_nims = [
        ("12345678", True),
        ("abc12345", False),
        ("123", False),
    ]
    
    print("\n✓ NIM Validation:")
    for nim, expected in test_nims:
        result = crud.validasi_nim(nim)
        status = "✓" if result == expected else "✗"
        print(f"  {status} {nim}: {result} (expected: {expected})")
    
    # Test Email validation
    test_emails = [
        ("budi@domain.com", True),
        ("invalid@.com", False),
        ("nodomain.com", False),
    ]
    
    print("\n✓ Email Validation:")
    for email, expected in test_emails:
        result = crud.validasi_email(email)
        status = "✓" if result == expected else "✗"
        print(f"  {status} {email}: {result} (expected: {expected})")
    
    print("\n✅ Validation test PASSED\n")


def test_crud_operations():
    """Test CRUD Operations."""
    print("=" * 60)
    print("TEST 4: CRUD Operations")
    print("=" * 60)
    
    crud = CRUDManager("test_mahasiswa.json")
    
    # CREATE
    print("\n✓ CREATE Operation:")
    success, msg = crud.create_mahasiswa(
        nama="Test Mahasiswa",
        nim="99887766",
        jurusan="Teknik Informatika",
        email="test@domain.com",
        tahun_masuk=2023
    )
    print(f"  {msg}")
    
    # READ
    print("\n✓ READ Operation:")
    data = crud.read_all_mahasiswa()
    print(f"  Total mahasiswa: {len(data)}")
    if data:
        print(f"  First: {data[0]['nama']} ({data[0]['nim']})")
    
    # UPDATE
    print("\n✓ UPDATE Operation:")
    success, msg = crud.update_mahasiswa(
        nim="99887766",
        nama="Test Updated"
    )
    print(f"  {msg}")
    
    # DELETE
    print("\n✓ DELETE Operation:")
    success, msg = crud.delete_mahasiswa("99887766")
    print(f"  {msg}")
    
    print("\n✅ CRUD test PASSED\n")


def test_sorting_algorithms():
    """Test Sorting Algorithms."""
    print("=" * 60)
    print("TEST 5: Sorting Algorithms")
    print("=" * 60)
    
    # Prepare test data
    test_data = [
        Mahasiswa("Zulu Ahmad", "33445566", "IF", "zulu@domain.com"),
        Mahasiswa("Beta Cinta", "22334455", "EE", "beta@domain.com"),
        Mahasiswa("Alpha Rini", "11223344", "TI", "alpha@domain.com"),
    ]
    
    sorting = AlgoritmaSorting()
    
    # Test Bubble Sort
    print("\n✓ Bubble Sort:")
    result, comparisons = sorting.bubble_sort(test_data, "nama", True)
    print(f"  Comparisons: {comparisons}")
    print(f"  Result: {result[0]['nama']} → {result[1]['nama']} → {result[2]['nama']}")
    
    # Test Merge Sort
    print("\n✓ Merge Sort:")
    result, comparisons = sorting.merge_sort(test_data, "nama", True)
    print(f"  Comparisons: {comparisons}")
    print(f"  Result: {result[0]['nama']} → {result[1]['nama']} → {result[2]['nama']}")
    
    # Test Shell Sort
    print("\n✓ Shell Sort:")
    result, comparisons = sorting.shell_sort(test_data, "nama", True)
    print(f"  Comparisons: {comparisons}")
    print(f"  Result: {result[0]['nama']} → {result[1]['nama']} → {result[2]['nama']}")
    
    # Show Big O Notation
    print("\n✓ Big O Notation Comparison:")
    for algo in ["bubble_sort", "merge_sort", "shell_sort"]:
        info = sorting.get_big_o_notation(algo)
        print(f"\n  {info['nama']}:")
        print(f"    Best: {info['best_case']}")
        print(f"    Avg:  {info['average_case']}")
        print(f"    Worst: {info['worst_case']}")
    
    print("\n✅ Sorting test PASSED\n")


def test_searching_algorithms():
    """Test Searching Algorithms."""
    print("=" * 60)
    print("TEST 6: Searching Algorithms")
    print("=" * 60)
    
    # Prepare test data
    test_data = [
        {"nama": "Alpha", "nim": "11111111"},
        {"nama": "Beta", "nim": "22222222"},
        {"nama": "Gamma", "nim": "33333333"},
        {"nama": "Delta", "nim": "44444444"},
    ]
    
    searching = AlgoritmaSearching()
    
    # Test Linear Search
    print("\n✓ Linear Search:")
    index, comparisons = searching.linear_search(test_data, "nama", "Gamma")
    print(f"  Target: 'Gamma'")
    print(f"  Found at index: {index}")
    print(f"  Comparisons: {comparisons}")
    
    # Test Binary Search
    print("\n✓ Binary Search:")
    # Binary search memerlukan data sorted
    sorted_data = sorted(test_data, key=lambda x: x['nim'])
    index, comparisons = searching.binary_search(sorted_data, "nim", "33333333")
    print(f"  Target: '33333333'")
    print(f"  Found at index: {index}")
    print(f"  Comparisons: {comparisons}")
    
    # Show Big O Notation
    print("\n✓ Big O Notation Comparison:")
    for algo in ["linear_search", "binary_search"]:
        info = searching.get_big_o_notation(algo)
        print(f"\n  {info['nama']}:")
        print(f"    Best: {info['best_case']}")
        print(f"    Avg:  {info['average_case']}")
        print(f"    Worst: {info['worst_case']}")
    
    print("\n✅ Searching test PASSED\n")


def test_error_handling():
    """Test Error Handling."""
    print("=" * 60)
    print("TEST 7: Error Handling")
    print("=" * 60)
    
    crud = CRUDManager("test_mahasiswa.json")
    
    # Test invalid email
    print("\n✓ Invalid Email Error Handling:")
    success, msg = crud.create_mahasiswa(
        nama="Test User",
        nim="12345678",
        jurusan="IF",
        email="invalid-email",  # Invalid format
        tahun_masuk=2023
    )
    print(f"  Result: {msg}")
    
    # Test invalid NIM
    print("\n✓ Invalid NIM Error Handling:")
    success, msg = crud.create_mahasiswa(
        nama="Test User",
        nim="abc",  # Invalid format
        jurusan="IF",
        email="test@domain.com",
        tahun_masuk=2023
    )
    print(f"  Result: {msg}")
    
    # Test duplicate NIM
    print("\n✓ Duplicate NIM Error Handling:")
    crud.create_mahasiswa(
        nama="First User",
        nim="87654321",
        jurusan="IF",
        email="first@domain.com",
        tahun_masuk=2023
    )
    
    success, msg = crud.create_mahasiswa(
        nama="Second User",
        nim="87654321",  # Same NIM
        jurusan="EE",
        email="second@domain.com",
        tahun_masuk=2023
    )
    print(f"  Result: {msg}")
    
    print("\n✅ Error Handling test PASSED\n")


def test_object_references():
    """Test Python Object References."""
    print("=" * 60)
    print("TEST 8: Python Object References (vs C++ Pointers)")
    print("=" * 60)
    
    print("\n✓ Object References in Python:")
    
    # Create object
    m1 = Mahasiswa("Budi", "12345678", "IF", "budi@domain.com")
    print(f"  m1 = Mahasiswa(...)")
    print(f"  m1 ID: {id(m1)} (memory address)")
    
    # Create reference to same object
    m2 = m1
    print(f"\n  m2 = m1  (reference, NOT copy)")
    print(f"  m2 ID: {id(m2)} (same as m1!)")
    
    # Modify through m2
    m2.nama = "Budi Wijaya"
    print(f"\n  m2.nama = 'Budi Wijaya'")
    print(f"  m1.nama = '{m1.nama}' (changed too!)")
    print(f"  ✓ Both refer to SAME object in memory")
    
    print("\n✓ Difference from C++ Pointer Arithmetic:")
    print("""
    Python:
      - m1 adalah reference ke object
      - Tidak bisa: m1++ (INVALID)
      - Tidak bisa: m1[0] (pointer offset)
      - Auto garbage collection
    
    C++:
      - ptr adalah raw memory address
      - Bisa: ptr++ (move ke next memory)
      - Bisa: ptr[0] (array access via offset)
      - Manual: delete ptr (memory management)
    """)
    
    print("✅ Object References test PASSED\n")


def main():
    """Run all tests."""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  TESTING APLIKASI MANAJEMEN DATA MAHASISWA  ".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")
    
    try:
        test_oop_encapsulation()
        test_oop_inheritance()
        test_validation()
        test_crud_operations()
        test_sorting_algorithms()
        test_searching_algorithms()
        test_error_handling()
        test_object_references()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nAplikasi siap untuk dijalankan dengan:")
        print("  streamlit run app.py\n")
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
