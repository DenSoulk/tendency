#самый длинный отрезок
import random 
lst = []
lenght = []
n = int(input())
count =0
for i in range(n):
    a = random.randint(0,1)
    lst.append(a)
for i in lst:
    if i == 1:
        lenght.append(count)
    count += 1
print(lst)
print(F"самый длинный отрезок {max(lenght)-min(lenght) + 1}")

















