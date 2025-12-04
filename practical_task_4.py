# practical_task_4_two_random_variants.py
# Варианты 3 и 7

# === ВАРИАНТ 3 ===

# ЗАДАНИЕ 1
num = -2
if num > 0:
    print(num - 1, num, num + 1)
else:
    num = 1
    print(num - 1, num, num + 1)

# ЗАДАНИЕ 2
filename = "file.py"
ext = filename.split(".")[-1]
if ext == "doc":
    print("Word file")
elif ext == "py":
    print("Python file")
elif ext == "txt":
    print("Text file")
else:
    print("Unknown")

# ЗАДАНИЕ 3
a = 5
b = 5
c = 8
if a == b == c:
    print("Равносторонний")
elif a == b or b == c or a == c:
    print("Равнобедренный")
else:
    print("Разносторонний")

# === ВАРИАНТ 7 ===

# ЗАДАНИЕ 1
s = "мария"
last = s[-1]
if last in ["я", "и", "е", "ю"]:
    print(True)
else:
    print(False)

# ЗАДАНИЕ 2
x = 3
y = 4
z = 5
if x > 0 and y > 0 and z > 0 and (x + y > z) and (x + z > y) and (y + z > x):
    print(True)
else:
    print(False)

# ЗАДАНИЕ 3
n = 32
last_digit = n % 10
if last_digit == 0:
    print(n ** 10)
elif last_digit == 1:
    print(n % 3)
elif last_digit == 2:
    print(n // 2)
else:
    print(n ** 2)
