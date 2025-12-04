# practical_task_5.py

# === ЗАДАНИЕ 1 ===
m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']
m.remove(0.25)
m.remove(15)
m.remove('10')
print(m)

# === ЗАДАНИЕ 2 ===
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del abc[1:5]
print(abc)

# === ЗАДАНИЕ 3 ===
numbers = [1, 4]
numbers.insert(1, 2)
numbers.insert(2, 3)
print(numbers)

# === ЗАДАНИЕ 4 ===
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]

non_negative = []
for num in mass:
    if num >= 0:
        non_negative.append(num)

mass = non_negative
mass.sort()
print(mass)

mass.sort(reverse=True)
print(mass)

# === ЗАДАНИЕ 5 ===
negatives = []
positives = []
zeros = []

count = 7
numbers_input = [-3, 0, 5, 0, -7, 10, 0]

for num in numbers_input:
    if num < 0:
        negatives.append(num)
    elif num > 0:
        positives.append(num)
    else:
        zeros.append(num)

sum_negatives = sum(negatives)

if len(positives) > 0:
    avg_positives = sum(positives) / len(positives)
else:
    avg_positives = 0

for i in range(len(zeros)):
    zeros[i] = '*'

print(sum_negatives)
print(avg_positives)
print(len(zeros))
print(zeros)
