import random
lst =[]
max = 0
n = int(input())
count= 0
for i in range(n):
    lst.append(random.randint(0,100))
for item in lst:
    count = 0
    for item2 in lst:
        count += item2
        if count % 5 ==0 and max < count:
            max = count
    print(lst)   
    lst.pop(0)

print(max)
