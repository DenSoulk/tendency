a = int(input())
perevod = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]   
b = a // 16
lst = []
lst.insert(0, perevod[a%16])
while b!= 0:
    lst.insert(0, perevod[b%16])
    b = b//16
print("".join(lst))
  