# practical_task_7.py

# === ЗАДАНИЕ 1 ===
table = [
    ['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
    ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
    ['my_song.mp3', 'anapa-2003.jpg', 'cs_1.6.exe', 'folder', 'cheat.txt'],
    ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4', 'array.py'],
    ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']
]

for row in table:
    print(row)

new_table = []
for row in table:
    temp = []
    for item in row:
        if item != 'folder':
            temp.append(item)
    new_table.append(temp)

for row in new_table:
    for i in range(len(row)):
        if row[i] == 'data.accdb':
            row[i] = 'data.sql'

print()
for row in new_table:
    print(row)

py_files = []
for row in table:
    for item in row:
        if item.endswith('.py'):
            py_files.append(item)

print()
print(*py_files)

js_files = []
for row in table:
    for item in row:
        if item.endswith('.js'):
            js_files.append("new_" + item)

print(*js_files)

# === ЗАДАНИЕ 2 ===
word_numb = ["ноль","один","два","три","четыре","пять","шесть","семь","восемь","девять"]
n = 5
if n <= 9:
    for i in range(n):
        print(word_numb[i])
else:
    print("Введите число <= 9")

# === ЗАДАНИЕ 3 ===
bin_sy = ['11011111','11011101','11000111','11011100','11011110']
dec = []
for b in bin_sy:
    dec.append(int(b,2))
print(dec)
print(max(dec))
print(min(dec))

# === ЗАДАНИЕ 4 ===
A = [
    [-446, 281, -80],
    [465, 432, -122],
    [13, "error", 8]
]

for i, row in enumerate(A):
    for j, val in enumerate(row):
        if isinstance(val, str):
            A[i][j] = len(val)

total = 0
for row in A:
    for v in row:
        total += v
print(total)

# === ЗАДАНИЕ 5 ===
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

diag = matrix[0][0] + matrix[1][1] + matrix[2][2]
print(diag)
