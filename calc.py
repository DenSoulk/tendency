#из любой системы счисления в 10чную
N = int(input("Ведите число: "))
S = int(input("В какой системе счисления данное число: "))
n = str(N)
answer = 0
n = n[::-1]
leng = len(n)
for i in range(leng):
    answer += int(n[i])*S**i
print(answer)
