from datetime import date
day = int(input())
month = int(input())
year = int(input())
day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month == 12:
    pay_day = date(year+1, 1, 15)  #сб = 5 вс = 6
    if pay_day.weekday() > 4:
            before = (4 - pay_day.weekday())*(-1)
            pay_day = date(year+1, 1, 15-before)

if day > 15:
    if month < 12:
        pay_day = date(year, month+1, 15)   #сб = 5 вс = 6
        if pay_day.weekday() > 4:
            before = (4 - pay_day.weekday())*(-1)
            pay_day = date(year, month+1, 15-before)
    else:
        pay_day = date(year, 1, 15)   #сб = 5 вс = 6
        if pay_day.weekday() > 4:
            before = (4 - pay_day.weekday())*(-1)
            pay_day = date(year, 1, 15-before)
else:
    pay_day = date(year, month, 15)
    if pay_day.weekday() > 4:
            before = (4 - pay_day.weekday())*(-1)
            pay_day = date(year, month, 15-before)

  
today = date(year, month, day)

print(pay_day - today)


    

