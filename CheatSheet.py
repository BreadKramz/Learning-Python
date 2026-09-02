# ==========================================
# PYTHON DATA TYPES CHEAT SHEET
# ==========================================


# ==========================================
# 1. STRING (str)
# ==========================================

name = "Mark"
course = "Computer Science"

print("STRING:")
print(name)
print(type(name))


# ==========================================
# 2. INTEGER (int)
# ==========================================

age = 21
score = 100

print("\nINTEGER:")
print(age)
print(type(age))


# ==========================================
# 3. FLOAT (float)
# ==========================================

grade = 95.5
price = 99.99

print("\nFLOAT:")
print(grade)
print(type(grade))


# ==========================================
# 4. BOOLEAN (bool)
# ==========================================

is_student = True
is_logged_in = False

print("\nBOOLEAN:")
print(is_student)
print(type(is_student))


# ==========================================
# 5. LIST (list)
# ==========================================

grades = [85, 90, 88, 92]

print("\nLIST:")
print(grades)
print(grades[0])
print(type(grades))


# ==========================================
# 6. TUPLE (tuple)
# ==========================================

coordinates = (10, 20)

print("\nTUPLE:")
print(coordinates)
print(coordinates[0])
print(type(coordinates))


# ==========================================
# 7. SET (set)
# ==========================================

numbers = {1, 2, 3, 3, 4}

print("\nSET:")
print(numbers)
print(type(numbers))


# ==========================================
# 8. DICTIONARY (dict)
# ==========================================

student = {
    "name": "Mark",
    "age": 21,
    "course": "Computer Science"
}

print("\nDICTIONARY:")
print(student)
print(student["name"])
print(student["course"])
print(type(student))


# ==========================================
# 9. RANGE (range)
# ==========================================

numbers_range = range(5)

print("\nRANGE:")
print(numbers_range)
print(type(numbers_range))

for number in numbers_range:
    print(number)


# ==========================================
# 10. COMPLEX (complex)
# ==========================================

complex_number = 3 + 2j

print("\nCOMPLEX:")
print(complex_number)
print(type(complex_number))


# ==========================================
# 11. NONE (NoneType)
# ==========================================

result = None

print("\nNONE:")
print(result)
print(type(result))


# ==========================================
# 12. BYTES (bytes)
# ==========================================

data = b"Hello"

print("\nBYTES:")
print(data)
print(type(data))


# ==========================================
# 13. BYTEARRAY (bytearray)
# ==========================================

byte_data = bytearray(5)

print("\nBYTEARRAY:")
print(byte_data)
print(type(byte_data))


# ==========================================
# 14. FROZENSET (frozenset)
# ==========================================

fixed_numbers = frozenset([1, 2, 3])

print("\nFROZENSET:")
print(fixed_numbers)
print(type(fixed_numbers))


# ==========================================
# 15. MEMORYVIEW (memoryview)
# ==========================================

memory_data = memoryview(b"Hello")

print("\nMEMORYVIEW:")
print(memory_data)
print(type(memory_data))


# ==========================================
# SUMMARY
# ==========================================

print("\n==========================================")
print("PYTHON DATA TYPES")
print("==========================================")

print("str        -> Text")
print("int        -> Whole numbers")
print("float      -> Decimal numbers")
print("bool       -> True / False")
print("list       -> Ordered, changeable collection")
print("tuple      -> Ordered, unchangeable collection")
print("set        -> Unique values")
print("dict       -> Key/value pairs")
print("range      -> Sequence of numbers")
print("complex    -> Complex numbers")
print("NoneType   -> No value")
print("bytes      -> Immutable binary data")
print("bytearray  -> Mutable binary data")
print("frozenset  -> Immutable set")
print("memoryview -> View of binary data")
