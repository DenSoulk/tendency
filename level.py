N = int(input("Ведите число: "))
n = str(N)
answer = 0
n = n[::-1]
leng = len(n)
for i in range(leng):
    q = int(n[i])-(i+1)
    if q>answer:
        answer = q

print(answer)
