# 📚 DOKUMENTASI KODE APLIKASI MANAJEMEN DATA MAHASISWA

Dokumentasi teknis lengkap untuk arsitektur, design pattern, dan penjelasan algoritma.

---

## 📋 Daftar Isi
1. [Struktur File](#struktur-file)
2. [Arsitektur Aplikasi](#arsitektur-aplikasi)
3. [Penjelasan Class & Method](#penjelasan-class--method)
4. [Algoritma Detil](#algoritma-detil)
5. [Flow Diagram](#flow-diagram)

---

## Struktur File

```
ProjectRasyid/
├── app.py                          # Main Streamlit application (800+ lines)
├── mahasiswa.py                    # OOP Classes (250+ lines)
├── algoritma_sorting.py            # Sorting algorithms (300+ lines)
├── algoritma_searching.py          # Searching algorithms (150+ lines)
├── crud_manager.py                 # CRUD & File I/O (350+ lines)
├── test_aplikasi.py               # Testing suite (350+ lines)
├── requirements.txt               # Dependencies
├── .streamlit/config.toml         # Streamlit configuration
├── .gitignore                     # Git ignore rules
├── README.md                      # Quick start guide
├── DEPLOYMENT_GUIDE.md            # Deployment instructions
├── CODE_DOCUMENTATION.md          # This file
└── data_mahasiswa.json            # Data storage (auto-created)

Total lines of code: ~2000 lines
```

---

## Arsitektur Aplikasi

```
┌─────────────────────────────────────────────────────────────┐
│                    STREAMLIT UI LAYER (app.py)              │
│  - Dashboard, CRUD Forms, Sorting UI, Searching UI, Stats   │
│  - Input validation & user interaction                       │
└────────────┬──────────────────────────────────────────────┬─┘
             │                                              │
       ┌─────▼──────┐                           ┌───────────▼──┐
       │   LOGIC    │                           │ ALGORITHMS  │
       │   LAYER    │                           │   LAYER     │
       │            │                           │             │
       │CRUDManager │◄──────────────────────────┤ Sorting     │
       │ - Create   │   (calls methods)         │ - Bubble    │
       │ - Read     │                           │ - Merge     │
       │ - Update   │◄──────────────────────────┤ - Shell     │
       │ - Delete   │                           │ Searching   │
       │ - Validate │                           │ - Linear    │
       │ - Stats    │◄──────────────────────────┤ - Binary    │
       └─────┬──────┘                           └─────────────┘
             │
      ┌──────▼────────────┐
      │   OOP LAYER       │
      │                   │
      │  Mahasiswa        │ (private attributes)
      │  ├─ __nama        │ (encapsulation)
      │  ├─ __nim         │
      │  ├─ __jurusan     │
      │  ├─ __email       │
      │  └─ methods()     │
      │                   │
      │  MahasiswaBaru    │ (inheritance)
      │  └─ extends       │
      │     Mahasiswa     │
      │                   │
      │  MahasiswaLama    │ (inheritance)
      │  └─ extends       │
      │     Mahasiswa     │
      └─────┬─────────────┘
            │
      ┌─────▼──────────────┐
      │  DATA LAYER        │
      │  (JSON File I/O)   │
      │                    │
      │  data_mahasiswa.   │
      │  json              │
      └────────────────────┘
```

---

## Penjelasan Class & Method

### 1. Mahasiswa (Base Class)

**Tujuan**: Merepresentasikan data mahasiswa dengan OOP principles

**Atribut Privat** (Encapsulation):
```python
class Mahasiswa:
    def __init__(self, nama, nim, jurusan, email, tahun_masuk, status):
        self.__nama = nama           # Private (name mangling: _Mahasiswa__nama)
        self.__nim = nim
        self.__jurusan = jurusan
        self.__email = email
        self.__tahun_masuk = tahun_masuk
        self.__status = status
        self.__tanggal_dibuat = datetime.now().isoformat()
```

**Why Private?**
- Mencegah modifikasi langsung yang tidak valid
- Enforce validation melalui setter
- Proteksi data integrity

**Properties (Getter/Setter)**:
```python
@property
def nama(self) -> str:
    """Getter"""
    return self.__nama

@nama.setter
def nama(self, value: str) -> None:
    """Setter dengan validasi"""
    if len(value) >= 3:
        self.__nama = value
```

**Methods**:
| Method | Purpose |
|--------|---------|
| `__init__()` | Constructor |
| `__str__()` | String representation (polymorphic) |
| `__repr__()` | For debugging |
| `info()` | Return dict info (polymorphic) |
| `info_display()` | Formatted display |
| Properties (nama, nim, etc) | Controlled access |

---

### 2. MahasiswaBaru (Child Class)

**Inheritance dari Mahasiswa**:
```python
class MahasiswaBaru(Mahasiswa):
    def __init__(self, ..., program_orientasi=True):
        super().__init__(...)  # Call parent constructor
        self.program_orientasi = program_orientasi
```

**Polymorphism - Override `info()`**:
```python
def info(self) -> Dict:
    # Get parent info
    info_parent = super().info()
    # Add child-specific info
    info_parent["program_orientasi"] = self.program_orientasi
    info_parent["kategori"] = "Mahasiswa Baru"
    return info_parent
```

---

### 3. MahasiswaLama (Child Class)

**Inheritance + New Property**:
```python
class MahasiswaLama(Mahasiswa):
    def __init__(self, ..., ipk=0.0):
        super().__init__(...)
        self._ipk = ipk  # Protected (single underscore)
    
    @property
    def ipk(self) -> float:
        return self._ipk
    
    @ipk.setter
    def ipk(self, value: float) -> None:
        if 0.0 <= value <= 4.0:
            self._ipk = round(value, 2)
```

**Additional Methods**:
```python
def get_keterangan_ipk(self) -> str:
    """Konversi IPK ke keterangan"""
    if self._ipk >= 3.5:
        return "Cumlaude"
    elif self._ipk >= 3.0:
        return "Sangat Memuaskan"
    # ... dll
```

---

## CRUDManager Class

**Tanggung Jawab**:
- File I/O operations (JSON)
- Data validation (Regex)
- CRUD logic
- Error handling

### Method: Create

```python
def create_mahasiswa(self, nama, nim, jurusan, email, ...):
    """
    Langkah-langkah:
    1. Validate input (Regex + custom rules)
    2. Load existing data
    3. Check NIM duplication
    4. Create Mahasiswa object
    5. Convert to dict
    6. Append ke data
    7. Save to JSON file
    """
    # Validation with Regex
    if not self.validasi_nim(nim):
        return False, "Invalid NIM format"
    
    if not self.validasi_email(email):
        return False, "Invalid email format"
    
    # File I/O
    data = self._load_from_file()
    
    # Check duplication
    for m in data:
        if m.get("nim") == nim:
            return False, "NIM already exists"
    
    # Create & append
    mahasiswa_obj = Mahasiswa(...)
    data.append(mahasiswa_obj.info())
    self._save_to_file(data)
    
    return True, "Success"
```

### Method: Read

```python
def read_all_mahasiswa(self) -> List[Dict]:
    """Load semua data dari JSON"""
    try:
        with open(self.file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
```

### Method: Update

```python
def update_mahasiswa(self, nim, nama=None, ...):
    """
    Langkah-langkah:
    1. Load data
    2. Find mahasiswa by NIM
    3. Validate new values
    4. Update fields
    5. Save to JSON
    """
```

### Method: Delete

```python
def delete_mahasiswa(self, nim: str):
    """Filter out mahasiswa dengan NIM tertentu"""
    data = self._load_from_file()
    data = [m for m in data if m.get("nim") != nim]
    self._save_to_file(data)
```

---

## Algoritma Detil

### Sorting Algorithms

#### 1. Bubble Sort

**Pseudo Code**:
```
BubbleSort(array, key, ascending):
    n = length(array)
    for i = 0 to n-1:
        swapped = false
        for j = 0 to n-i-2:
            if compare(array[j], array[j+1]):
                swap(array[j], array[j+1])
                swapped = true
        if not swapped:
            break
    return array
```

**Complexity Analysis**:
- **Best Case**: O(n) - Data sudah sorted, early termination
- **Average Case**: O(n²) - Random swaps
- **Worst Case**: O(n²) - Data fully reversed

**Visual**:
```
Pass 1: [5,2,8,1,9] → [2,5,1,8,9] → [2,1,5,8,9]
Pass 2: [2,1,5,8,9] → [1,2,5,8,9] → [1,2,5,8,9]
Pass 3: [1,2,5,8,9] → no swap → DONE
```

**Implementation**:
```python
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:  # compare
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
            swapped = True
    if not swapped:
        break
```

---

#### 2. Merge Sort

**Pseudo Code** (Divide & Conquer):
```
MergeSort(array):
    if length(array) <= 1:
        return array
    
    mid = length(array) / 2
    left = MergeSort(array[0:mid])
    right = MergeSort(array[mid:])
    
    return Merge(left, right)

Merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i++
        else:
            result.append(right[j])
            j++
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Complexity Analysis**:
- **Best Case**: O(n log n) - Consistent
- **Average Case**: O(n log n) - Consistent
- **Worst Case**: O(n log n) - Consistent

**Why log n?**
```
Level 0:        [1,5,2,8,3,7,4,6]           (1 array)
                       ↓ divide
Level 1:    [1,5,2,8]    [3,7,4,6]          (2 arrays)
                 ↓              ↓ divide
Level 2:    [1,5] [2,8]    [3,7] [4,6]     (4 arrays)
              ↓     ↓         ↓     ↓ divide
Level 3:    [1][5] [2][8]  [3][7] [4][6]   (8 arrays)

Divide: 8→4→2→1 = log₂(8) = 3 levels
Merge: Each level needs O(n) comparisons
Total: O(n log n)
```

**Space Complexity**: O(n) - Temporary arrays needed

---

#### 3. Shell Sort

**Pseudo Code** (Generalized Insertion Sort):
```
ShellSort(array):
    gap = length(array) / 2
    while gap > 0:
        for i = gap to length(array):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j -= gap
            array[j] = temp
        gap = gap / 2
```

**Visual Example**:
```
Initial: [9,5,2,8,1,7,3,6,4]
Gap=4:   [9,1] [5,7] [2,3] [8,6] [4]
         ↓
         [1,5,2,6,3,7,8,9,4]

Gap=2:   [1,5] [2,6] [3,7] [8,9] [4]
         ↓
         [1,2,3,6,5,7,8,4,9]

Gap=1:   Standard Insertion Sort
         [1,2,3,4,5,6,7,8,9]
```

**Complexity Analysis**:
- Tergantung pada gap sequence
- Best gap: Knuth sequence (1, 4, 13, 40, ...)
- **Average Case**: O(n^1.3) - Much better than Bubble Sort!

---

### Searching Algorithms

#### 1. Linear Search

**Pseudo Code**:
```
LinearSearch(array, target):
    for i = 0 to length(array):
        if array[i] == target:
            return i
    return -1  // Not found
```

**Complexity**:
- **Best**: O(1) - Found at first position
- **Average**: O(n) - Found at middle
- **Worst**: O(n) - Found at last or not found

**Advantage**:
- Works on unsorted data
- Simple to implement
- Good for small datasets

**Implementation**:
```python
for index, item in enumerate(data):
    if item[search_key].lower() == search_value.lower():
        return index, comparisons
```

---

#### 2. Binary Search

**Pseudo Code**:
```
BinarySearch(sorted_array, target):
    left = 0
    right = length(array) - 1
    
    while left <= right:
        mid = (left + right) / 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  // Not found
```

**Complexity**:
- **Best**: O(1) - Found at mid
- **Average**: O(log n) - Divide & conquer
- **Worst**: O(log n) - Consistent

**Why log n?**
```
Array: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
       (16 elements)

Search 14:
Step 1: left=0, right=15, mid=7 (value=8)
        8 < 14, so left=8

Step 2: left=8, right=15, mid=11 (value=12)
        12 < 14, so left=12

Step 3: left=12, right=15, mid=13 (value=14)
        14 == 14, FOUND!

Steps: 16→8→4→2→1 = log₂(16) = 4
```

**Requirement**: Data HARUS sorted!

**Optimization in App**:
```python
# Auto-sort sebelum binary search
sorted_data, _ = AlgoritmaSorting.merge_sort(data, key, ascending)
index, comparisons = AlgoritmaSearching.binary_search(sorted_data, key, target)
```

---

## Validation (Regex)

### NIM Validation
```python
pattern = r'^\d{8,12}$'
# ^ = start of string
# \d = digit
# {8,12} = between 8-12 digits
# $ = end of string

Examples:
✓ "12345678" - Valid (8 digits)
✓ "123456789012" - Valid (12 digits)
✗ "ABC12345" - Invalid (contains letters)
✗ "1234567" - Invalid (only 7 digits)
```

### Email Validation
```python
pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# ^ = start
# [a-zA-Z0-9._-]+ = username (alphanumeric, dot, underscore, hyphen)
# @ = literal @
# [a-zA-Z0-9.-]+ = domain (alphanumeric, dot, hyphen)
# \. = literal dot
# [a-zA-Z]{2,} = TLD (minimum 2 letters)
# $ = end

Examples:
✓ "user@example.com" - Valid
✓ "john.doe@company.co.uk" - Valid
✗ "invalid@.com" - Invalid (no domain name)
✗ "nodomain.com" - Invalid (no @)
✗ "user@domain" - Invalid (no TLD)
```

---

## Error Handling

### File I/O Error Handling
```python
try:
    with open(self.file_path, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    # File doesn't exist, create with empty list
    self._save_to_file([])
except json.JSONDecodeError:
    # File corrupted, reinitialize
    self._save_to_file([])
except IOError as e:
    # Other I/O errors
    raise IOError(f"Error reading file: {str(e)}")
```

### Input Validation Error Handling
```python
try:
    success, message = crud.create_mahasiswa(...)
    
    if not success:
        st.error(message)
        return
    
    st.success(message)
except Exception as e:
    st.error(f"Unexpected error: {str(e)}")
    import traceback
    traceback.print_exc()
```

---

## Flow Diagram

### Create Mahasiswa Flow
```
User Input Form
    ↓
Streamlit captures: nama, nim, jurusan, email, ...
    ↓
app.py calls: crud.create_mahasiswa(...)
    ↓
CRUD Manager:
  - Validate NIM (Regex)
  - Validate Email (Regex)
  - Check duplicate NIM
    ↓
Create Mahasiswa object:
  - Encapsulation: Private attributes
  - Call __init__()
    ↓
Convert to dict via .info()
    ↓
Load existing data from JSON
    ↓
Append new mahasiswa dict
    ↓
Save to JSON file
    ↓
Return success message
    ↓
Streamlit displays: ✅ Success!
    ↓
Rerun UI
```

### Search Mahasiswa Flow
```
User selects: Search Method & Field
User enters: Search value
    ↓
IF Linear Search:
  - Call searching.linear_search(data, field, value)
  - Iterate through all data
  - Return first match + comparison count
    ↓
ELSE Binary Search:
  - Sort data: sorting.merge_sort(data, field)
  - Call searching.binary_search(sorted_data, field, value)
  - Divide & conquer search
  - Return match + comparison count
    ↓
Display Big O Notation
    ↓
Display result in Streamlit
```

---

## Performance Comparison Table

| Task | Algoritma | Time | Space | Best For |
|------|-----------|------|-------|----------|
| **Sort small (n<50)** | Bubble | O(n²) | O(1) | Learning |
| **Sort large (n>1000)** | Merge | O(n log n) | O(n) | Production |
| **Sort medium (n~100-500)** | Shell | O(n^1.3) | O(1) | Balance |
| **Search unsorted** | Linear | O(n) | O(1) | Simple |
| **Search sorted** | Binary | O(log n) | O(1) | Fast |

---

## Testing Strategy

Aplikasi sudah ditest dengan comprehensive test suite (`test_aplikasi.py`):

1. ✅ OOP Encapsulation
2. ✅ OOP Inheritance & Polymorphism
3. ✅ Input Validation (Regex)
4. ✅ CRUD Operations
5. ✅ Sorting Algorithms
6. ✅ Searching Algorithms
7. ✅ Error Handling
8. ✅ Object References (vs C++ Pointers)

**Jalankan test**:
```bash
python test_aplikasi.py
```

---

## Modularization Benefits

| Module | Responsibility |
|--------|-----------------|
| `mahasiswa.py` | OOP Logic only |
| `algoritma_sorting.py` | Sorting algorithms |
| `algoritma_searching.py` | Searching algorithms |
| `crud_manager.py` | Data persistence |
| `app.py` | UI/UX only |

**Benefit**: 
- Easy to test each module independently
- Easy to maintain and modify
- Easy to reuse in other projects
- Clear separation of concerns

---

## Future Enhancement Ideas

1. **Database Integration**
   - Replace JSON with PostgreSQL/MongoDB
   - Persistent across sessions
   - Multi-user support

2. **Authentication**
   - User login system
   - Role-based access (Admin, User)

3. **Advanced Algorithms**
   - Quick Sort
   - Heap Sort
   - More searching techniques

4. **Visualization**
   - Sorting visualization (animated)
   - Algorithm complexity graphs

5. **Export Features**
   - PDF export
   - Excel export
   - CSV import

6. **Mobile Responsive**
   - Better mobile UI
   - Native mobile apps

---

**Happy Coding! 🚀**
