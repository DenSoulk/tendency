#калькулятор из десятичной системы счисления в любую
a = int(input("Введите число в десятичной системе счисления:"))
n = int(input("Введите систему счисления:"))
perevod = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","G","K","L","M","N","O","P"]   
b = a // n
lst = []
lst.insert(0, perevod[a%n])
while b!= 0:
    lst.insert(0, perevod[b%n])
    b = b//n
print("".join(lst))
  