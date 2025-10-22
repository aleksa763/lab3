lines = []
while True:
    line = input("Введите строку чисел через пробел (пустая строка — конец): ")
    if line == "":
        break
    lines.append(line)
matrix = [[int(num) for num in line.split()] for line in lines]
print("Результат:")
for row in matrix:
    print(row)
