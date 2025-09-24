import random

temps = [15.5, 16.2, 14.8, 17.1, 18.0, 19.3, 20.1, 21.5, 22.3, 23.1,
         24.0, 25.2, 26.4, 27.1, 28.3, 29.0, 30.2, 28.5, 27.7, 26.9,
         25.6, 24.4, 23.8, 22.1, 21.3, 20.5, 19.8, 18.6, 17.4, 16.0]

average_temp = sum(temps) / len(temps)
print("Средняя температура за месяц:", average_temp)

B = [[random.randint(-10, 10) for _ in range(5)] for _ in range(5)]

print("\nМассив B:")
for row in B:
    print(row)

count = 0
for i in range(5):
    for j in range(i):
        if B[i][j] > 0:
            count += 1

print("\nКоличество положительных элементов слева от диагонали:", count)
