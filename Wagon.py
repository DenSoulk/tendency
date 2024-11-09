a = int(input())
lst=["W","M","A","A","M","W","W","M","A","A","M","W"]
count = list(range(11,0, -2))
b = lst[(a-1)%12]
if a %12 <= 6:
    another_seat = a + count[(a%6)-1]
if a %12 > 6:
    count.reverse()
    another_seat = a - count[(a%6)-1]
print(F"{another_seat}{b}")