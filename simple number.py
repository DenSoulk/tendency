import time

def find_simple(start_n, end_n, break_flag, lst):
    for i in range(start_n, end_n+1 ):
        flag = 0
        for j in range(2,i):
            if i%j ==0:
                flag = 1
                break
        if flag ==0:
            lst.append(i)
            if break_flag:
                break

        if end_n in lst:
            if not break_flag:
                print("Простое")
            return end_n+1
        else:
            if break_flag:
                print("Не простое")
            return end_n

n = int(input("Ведите число: "))

p = 0
lst = []

start_n = find_simple(2, n, False, lst)

find_simple(start_n, 100000, True, lst)

if abs(lst[len(lst)-1]-n) < abs(lst[len(lst)-2]-n):
    print("Ближайшее простое: ", lst[len(lst)-1])
else:
    print("Ближайшее простое: ", lst[len(lst)-2])

print(lst)