# practical_task_6.py

# === ЗАДАНИЕ 1 ===
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    print(row)
print("нечётные числа matrix")
for row in matrix:
    for n in row:
        if n % 2 != 0:
            print(n, end=" ")
print()
even_count = 0
for row in matrix:
    for n in row:
        if n % 2 == 0:
            even_count += 1
print("кол-во чётных:", even_count)

# === ЗАДАНИЕ 2 ===
matrix_1 = [[2,4,3,6],[5,7,1,5]]
matrix_2 = [[2,9,0,2],[3,4,7,6]]
answer = [[0,0,0,0],[0,0,0,0]]

for i in range(2):
    for j in range(4):
        answer[i][j] = matrix_1[i][j] * matrix_2[i][j]

print(answer)
for row in answer:
    print(row, "сумма строки:", sum(row))

# === ЗАДАНИЕ 3 ===
fruits = [['Banana','apple'],['apricot','Avocado'],['lime','lemon'],['Mango','grapes']]
for row in fruits:
    for item in row:
        if item[0].isupper():
            print(item)

# === ЗАДАНИЕ 4 ===
random_elements = [
    ['toy','bee','cheese','ear'],
    [False,'word','0110110',10],
    ['happiness','(」°ロ°)」','luck',None],
    ['car','<- code ->',4.7,True]
]

for i, row in enumerate(random_elements):
    if i % 2 == 1:
        print(row)

# === ЗАДАНИЕ 5 ===
rows = 2
cols = 3
values = [[2,1,5],[67,-1,0]]

print("Ваш двумерный массив:")
for row in values:
    print(row)
