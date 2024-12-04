"""Даны двумерные массивы А и В
Данниые на вход:
кол-во стррок и столбов и ограничение на рандом
Данные на выход:
перемножить и сложить массивы А и В; Вывести сумму главной диагонали
"""import random
lstA = []
lstB = []
lst_increase = []
lst_addition = []
strings = int(input())
pillar = int(input())
R = int(input())

def sozdanie(listic):
    for j in range(pillar):
        lst1 = []
        for q in range(strings):
            lst1.append(random.randint(1, R))
        listic.append(lst1)


sozdanie(lstA)
sozdanie(lstB)



for i in range(pillar):
    lst = []
    for j in range(strings):
        try:
            lst.append(lstA[i][j] * lstB[i][j])   
        except IndexError:
            continue
    lst_increase.append(lst)


for i in range(pillar):
    lst = []
    for j in range(strings):
        try:
            lst.append(lstA[i][j] + lstB[i][j])   
        except IndexError:
            continue
    lst_increase.append(lst)

summaA = 0
summaB = 0
for i in range(pillar):
    summaA += lstA[i][i]
for i in range(pillar):
    summaB += lstB[i][i]




dop_summaA = 0
dop_summaB = 0
for i in range(pillar):
    dop_summaA += lstA[i][strings-i-1]
for i in range(pillar):
    dop_summaB += lstB[i][strings-i-1]




#ПРИНТЫ
print("Массив А")
for i in range(pillar):
    print(lstA[i])
print('\n')

print("Массив В")
for i in range(pillar):
    print(lstB[i])
print('\n')

print("Результат умножения")
for i in range(pillar):
    print(lst_increase[i])
print('\n')

print("Результат сложения")
for i in range(pillar):
    print(lst_increase[i])
print('\n')

print(F"Cумма элементов главной диагонали массива А \n{summaA} \n\nCумма элементов главной диагонали массива В\n{summaB}\n")
print(F"Cумма элементов побочной диагонали массива А \n{dop_summaA} \n\nCумма элементов побочной диагонали массива В\n{dop_summaB}")
