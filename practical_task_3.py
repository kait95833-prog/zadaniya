# practical_task_3.py  (без import math)

# === ЗАДАЧА 1 ===
minutes = 90
hours = minutes // 60
mins = minutes % 60
print(hours)
print(mins)

# === ЗАДАЧА 2 ===
a = 7
b = 9
h = 6

if h < a:
    print("Недосып")
elif h > b:
    print("Пересып")
else:
    print("Это нормально")

# === ЗАДАЧА 3 ===
# Формула Герона без math: sqrt(x) = x ** 0.5

a_side = 3
b_side = 4
c_side = 5

p = (a_side + b_side + c_side) / 2
area = (p * (p - a_side) * (p - b_side) * (p - c_side)) ** 0.5
print(area)

# === ЗАДАЧА 4 ===
figure = "circle"  # triangle / rectangle / circle

if figure == "triangle":
    a = 3
    b = 4
    c = 5
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)

elif figure == "rectangle":
    a = 5
    b = 6
    print(a * b)

elif figure == "circle":
    r = 5
    print(3.14 * r * r)

# === ЗАДАЧА 5 ===
n = 23

if 11 <= n % 100 <= 14:
    word = "программистов"
else:
    last = n % 10
    if last == 1:
        word = "программист"
    elif last in [2, 3, 4]:
        word = "программиста"
    else:
        word = "программистов"

print(n, word)

# === ЗАДАЧА 6 ===
ticket = "123015"
first = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
last = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

if first == last:
    print("Счастливый")
else:
    print("Обычный")
