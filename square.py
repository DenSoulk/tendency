#Дан рандомный двумерный массив N*N заполененный 0 и 1.
# Вычислить площадь самого большого квадрата с вероятность 80% на точке х, у будет 1
import random
N = int(input())
lst= []
for i in range(N):
    row =[]
    for j in range(N):
        if random.randint(0,100)> 20:
            row.append(1)
        else:
            row.append(0)
    lst.append(row)

max_per = 0
for i in range(N):
    per = 0
    for j in range(N):
        if lst[i][j] ==1:
            leng = 0
            for k in range(j, N):
                try:
                    if lst[i][k] and lst[i+leng][j] and lst[i+leng][k]:
                        per = leng
                        if per>max_per:
                            max_per = per
                    leng += 1
                except:
                    continue

for i in lst:
    print(i)

print(max_per*4)
